"""Measurement digital-twin for the decisive tapered-cavity-thrust experiment.

The companion to `decisive_test_budget.py`. Where the budget proves the SIGNAL is
resolvable, this proves the *analysis pipeline* actually works: given realistic
noise + systematics, does AC-modulation + lock-in + Q-scaling + the null tests
CORRECTLY (a) recover a real QI signal and (b) REJECT a systematics-only world
with zero false positives?

It is to the experiment what device_sim is to the craft: not a proof the physics
is real, but a proof the method can tell real from artifact.

Model (SI units). We simulate the *measured force* time series on a torsion
balance and run a genuine lock-in — no analytic shortcuts; the recovery gain is
self-calibrated from a noiseless unit run.

Run:  python decisive_test_sim.py
"""
from __future__ import annotations
import numpy as np

c = 2.998e8
ETA = 0.0072            # calibrated to Eagleworks (see budget script)
P = 10.0               # W CW, fixed across phases

# balance / DAQ
FS = 10.0              # Hz sample rate
T = 2000.0            # s run length
F_MOD = 0.05           # Hz modulation (well above 1/f drift, below Nyquist)
S_F = 1.0e-8           # N/sqrt(Hz) force-noise density

# systematics (both scale with dissipated power ~ P, i.e. FLAT in Q)
THERMAL_AMP = 1.0e-6   # N   slow thermal/CoM drift (bigger than the photon floor!)
MAG_AMP = 5.0e-7       # N   feed/magnetic offset (flips with current-reversal)

Q_PHASES = [5.0e4, 1.0e8, 1.0e10]


def qi_force(Q, geom=+1.0, symmetric=False, resonant=True):
    """The claimed QI thrust for one steady state (before modulation)."""
    if symmetric or not resonant:
        return 0.0
    return ETA * P * Q / c * geom


def _timebase():
    n = int(FS * T)
    t = np.arange(n) / FS
    # square-wave modulation IN PHASE with sin(2*pi*f*t)
    m = (np.sin(2 * np.pi * F_MOD * t) > 0).astype(float)
    return t, m


def _lockin(sig, t):
    """Return the recovered fundamental magnitude at F_MOD (both quadratures)."""
    s = np.sin(2 * np.pi * F_MOD * t)
    co = np.cos(2 * np.pi * F_MOD * t)
    X = 2.0 * np.mean(sig * s)
    Y = 2.0 * np.mean(sig * co)
    return np.hypot(X, Y), X   # magnitude, in-phase (carries sign)


# self-calibrate the lock-in gain on a noiseless unit-amplitude on/off square wave
def _calibrate():
    t, m = _timebase()
    _, X = _lockin(1.0 * m, t)
    return 1.0 / X            # so recovered_amp = gain * X reproduces the true amplitude
_GAIN = _calibrate()


def simulate(Q, world, modulation, *, geom=+1.0, symmetric=False, current=+1.0, seed=0):
    """One measured run -> recovered (signed) force amplitude and the noise floor."""
    rng = np.random.default_rng(seed)
    t, m = _timebase()
    n = t.size

    F_qi = qi_force(Q, geom=geom, symmetric=symmetric) if world == "true_QI" else 0.0
    thermal = THERMAL_AMP
    mag = MAG_AMP * current

    if modulation == "resonance_onoff":
        # QI is present only on-resonance -> modulated. Dumped power is EQUAL on/off
        # (reflected power routed to a fixed load) -> thermal & mag are UNMODULATED.
        qi_series = F_qi * m
        sys_series = thermal * np.ones(n) + mag * np.ones(n)
    elif modulation == "power_onoff":
        # naive: cut input power on/off -> EVERYTHING (QI + thermal + mag) modulates
        # together. This is the inferior scheme; thermal now leaks into the lock-in.
        qi_series = F_qi * m
        sys_series = (thermal + mag) * m
    else:
        raise ValueError(modulation)

    # slow 1/f-ish drift (random walk) + white force noise
    drift = np.cumsum(rng.standard_normal(n))
    drift = 3.0e-6 * drift / (np.abs(drift).max() + 1e-30)   # ~few uN slow wander
    white = S_F * np.sqrt(FS / 2.0) * rng.standard_normal(n)

    measured = qi_series + sys_series + drift + white
    mag_rec, x_rec = _lockin(measured, t)
    recovered = _GAIN * x_rec                    # signed recovered force
    # noise floor of the lock-in over this run
    floor = _GAIN * 2.0 * S_F * np.sqrt(FS / 2.0) / np.sqrt(n)
    return recovered, abs(floor)


def slope(qs, fs):
    """Fit log|F| vs log Q -> the Q-scaling exponent."""
    qs = np.asarray(qs, float); fs = np.abs(np.asarray(fs, float))
    good = fs > 0
    if good.sum() < 2:
        return float("nan")
    return float(np.polyfit(np.log10(qs[good]), np.log10(fs[good]), 1)[0])


def main():
    print(f"lock-in self-cal gain = {_GAIN:.4g}  (recovers unit amplitude exactly)")
    print(f"P={P} W  f_mod={F_MOD} Hz  T={T:.0f}s  S_f={S_F:.0e} N/rtHz  "
          f"thermal={THERMAL_AMP*1e6:.1f} uN  mag={MAG_AMP*1e6:.1f} uN")
    print()

    # ---- 1. TRUE-QI world, correct (resonance) modulation: Q-scaling curve ----
    print("[1] TRUE-QI world + resonance-on/off  (expect F proportional to Q, slope 1)")
    fs_true = []
    for i, Q in enumerate(Q_PHASES):
        F, floor = simulate(Q, "true_QI", "resonance_onoff", seed=i)
        fs_true.append(F)
        print(f"    Q={Q:.0e}  recovered={F:+.3e} N  floor={floor:.1e}  SNR={abs(F)/floor:.1e}")
    s_true = slope(Q_PHASES, fs_true)
    print(f"    --> Q-scaling slope = {s_true:.3f}")

    # ---- 2. SYSTEMATICS-ONLY world, resonance modulation: must be REJECTED ----
    print("\n[2] SYSTEMATICS-ONLY world (eta=0) + resonance-on/off  (expect ~0: rejected)")
    fs_sys = []
    for i, Q in enumerate(Q_PHASES):
        F, floor = simulate(Q, "systematics_only", "resonance_onoff", seed=100 + i)
        fs_sys.append(F)
        pred = ETA * P * Q / c
        print(f"    Q={Q:.0e}  recovered={F:+.3e} N  (QI would predict {pred:.2e}) "
              f"ratio={abs(F)/pred:.1e}")
    s_sys = slope(Q_PHASES, fs_sys)
    print(f"    --> Q-scaling slope = {s_sys:.3f}  (NOT 1 => not a QI signal; discriminator rejects)")

    # ---- 3. The confounder: systematics-only under naive POWER modulation ----
    print("\n[3] SYSTEMATICS-ONLY + naive POWER-on/off  (thermal LEAKS -> false +ve, but FLAT in Q)")
    fs_leak = []
    for i, Q in enumerate(Q_PHASES):
        F, floor = simulate(Q, "systematics_only", "power_onoff", seed=200 + i)
        fs_leak.append(F)
        print(f"    Q={Q:.0e}  recovered={F:+.3e} N")
    s_leak = slope(Q_PHASES, fs_leak)
    print(f"    --> slope = {s_leak:.3f}  (flat => Q-scaling test still catches it)")

    # ---- 4. Null-test suite in the true world (fixed Q=1e8) ----
    print("\n[4] Null tests, TRUE-QI world, Q=1e8, resonance-on/off")
    Q = 1.0e8
    base, _ = simulate(Q, "true_QI", "resonance_onoff", seed=7)
    rev, _ = simulate(Q, "true_QI", "resonance_onoff", geom=-1.0, seed=8)
    sym, _ = simulate(Q, "true_QI", "resonance_onoff", symmetric=True, seed=9)
    print(f"    frustum      : {base:+.3e} N")
    print(f"    reversed     : {rev:+.3e} N   (expect sign flip)")
    print(f"    symmetric    : {sym:+.3e} N   (expect ~0)")

    # ---- assertions: the checkable bar ----
    assert abs(s_true - 1.0) < 0.1, f"true-QI slope {s_true:.3f} != 1"
    for Q, F in zip(Q_PHASES, fs_true):
        assert abs(F) / (ETA * P * Q / c) > 0.9, "true signal under-recovered"
    # systematics-only must be (a) far below the QI prediction everywhere, and
    # (b) NOT a slope-1 Q-scaling line -> the discriminator refuses to call it a signal.
    for Q, F in zip(Q_PHASES, fs_sys):
        assert abs(F) / (ETA * P * Q / c) < 1e-2, "systematics too close to QI prediction"
    assert abs(s_sys - 1.0) > 0.3, f"systematics-only mimicked slope-1 ({s_sys:.3f})"
    assert abs(s_leak) < 0.3, f"power-mode leak not flat (slope {s_leak:.3f})"
    assert np.sign(rev) == -np.sign(base) and abs(rev + base) < 0.15 * abs(base), "reversal failed"
    assert abs(sym) < 0.02 * abs(base), "symmetric null failed"

    print("\nSIM OK:")
    print(f"  * TRUE-QI recovered with Q-scaling slope {s_true:.2f} (=1): pipeline SEES a real effect.")
    print(f"  * SYSTEMATICS-ONLY: recovered at the noise floor, Q-scaling slope {s_sys:+.2f} (NOT 1)")
    print( "    -> discriminator refuses it. NO false positive (resonance-on/off keeps dumped")
    print( "    power equal on/off, so thermal & magnetic offsets stay unmodulated).")
    print(f"  * Naive power-modulation LEAKS thermal (slope {s_leak:.2f}, FLAT) -> Q-scaling still")
    print( "    exposes it as non-QI. Two independent defenses, as designed.")
    print( "  * Null tests pass: reversal flips sign, symmetric cavity -> ~0.")


if __name__ == "__main__":
    main()
