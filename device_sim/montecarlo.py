"""Monte-Carlo fault-injection campaign.

Runs many randomized realistic flights (slew + sensor noise + estimator) with
random quench times/counts and random targets, and reports the survival rate +
position-error distribution. This is how you'd characterise the fault tolerance
of the control architecture before betting hardware on it.
"""
from __future__ import annotations
from dataclasses import dataclass, field
import numpy as np
from device_sim.sim import run
from device_sim.sensors import SensorNoise


@dataclass
class CampaignStats:
    n_runs: int
    survived: int
    survival_rate: float
    pos_err: np.ndarray            # per-run hold pos-error (m)
    max_quench: int
    settle_threshold: float
    diverged: int
    worst_err: float

    def summary(self) -> str:
        pe = self.pos_err
        return (f"Monte-Carlo fault campaign: {self.n_runs} runs\n"
                f"  survival rate     : {self.survival_rate*100:.1f}%  "
                f"({self.survived}/{self.n_runs} held < {self.settle_threshold} m)\n"
                f"  diverged          : {self.diverged}\n"
                f"  pos-error (m)     : mean {pe.mean():.3f}  median {np.median(pe):.3f}  "
                f"p95 {np.percentile(pe,95):.3f}  worst {self.worst_err:.3f}\n"
                f"  max cells quenched: {self.max_quench}")


def campaign(n_runs: int = 40, duration: float = 30.0, dt: float = 0.02,
             max_quench: int = 8, settle_threshold: float = 0.5,
             slew_hz: float = 20.0, base_seed: int = 100) -> CampaignStats:
    rng = np.random.default_rng(base_seed)
    errs = np.zeros(n_runs)
    survived = 0
    diverged = 0
    sn = SensorNoise()
    for i in range(n_runs):
        target = np.array([rng.uniform(-3, 3), rng.uniform(-3, 3), rng.uniform(-1, 1)])
        qc = int(rng.integers(0, max_quench + 1))
        qat = float(rng.uniform(8, duration * 0.6)) if qc > 0 else None
        r = run(target_pos=target, start_pos=np.zeros(3), duration=duration, dt=dt,
                slew_hz=slew_hz, sensor_noise=sn, use_estimator=True,
                quench_at=qat, quench_cells=qc, seed=int(rng.integers(0, 1 << 31)))
        errs[i] = r.max_pos_err if np.isfinite(r.max_pos_err) else 1e9
        if r.diverged:
            diverged += 1
        if (not r.diverged) and r.max_pos_err < settle_threshold:
            survived += 1
    return CampaignStats(
        n_runs=n_runs, survived=survived, survival_rate=survived / n_runs,
        pos_err=errs, max_quench=max_quench, settle_threshold=settle_threshold,
        diverged=diverged, worst_err=float(errs[np.isfinite(errs)].max()),
    )


if __name__ == "__main__":                          # pragma: no cover
    print(campaign().summary())
