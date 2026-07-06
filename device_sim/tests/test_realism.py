"""Realistic-effects tests: thrust-slew, sensor noise + estimator, MC campaign."""
import numpy as np
from device_sim.sim import run
from device_sim.sensors import SensorNoise
from device_sim.actuator import SlewActuator
from device_sim.montecarlo import campaign


# --- actuator ---

def test_slew_lags_then_tracks():
    act = SlewActuator(n=1, bandwidth_hz=10.0)
    dt = 0.02
    cmd = np.array([1.0])
    a1 = act.update(cmd, dt)[0]
    assert 0.0 < a1 < 1.0                 # first step lags (not instant)
    for _ in range(50):
        a = act.update(cmd, dt)[0]
    assert a > 0.99                       # converges to the command


def test_hover_holds_with_slew():
    for f in (10.0, 50.0, 100.0):
        r = run(target_pos=np.array([0, 0, 0.]), start_pos=np.array([0, 0, -2.]),
                duration=40, dt=0.02, slew_hz=f)
        assert not r.diverged
        assert r.max_pos_err < 0.1


# --- sensors + estimator ---

def test_estimator_holds_under_noise():
    r = run(target_pos=np.array([0, 0, 0.]), start_pos=np.array([0, 0, -2.]),
            duration=40, dt=0.02, sensor_noise=SensorNoise(), use_estimator=True, seed=1)
    assert not r.diverged
    assert r.max_pos_err < 0.15           # holds within 15 cm despite noisy sensing


def test_full_realistic_stack_survives_quench():
    r = run(target_pos=np.array([2, 0, 0.]), start_pos=np.zeros(3),
            duration=40, dt=0.02, slew_hz=20, sensor_noise=SensorNoise(),
            use_estimator=True, quench_at=15, quench_cells=5, seed=2)
    assert not r.diverged
    assert r.max_pos_err < 0.25           # slew + noise + estimator + 5 dead cells


# --- Monte-Carlo (small, fast) ---

def test_monte_carlo_high_survival():
    # duration=30 s is enough for the worst random +/-3 m target + quench to settle
    # (the full 40-run campaign at these settings gives 100% survival, worst 0.28 m).
    s = campaign(n_runs=6, duration=30, dt=0.02, max_quench=6, base_seed=7)
    assert s.diverged == 0                # nothing ever flies apart
    assert s.survival_rate >= 0.8         # robust across randomized faults
