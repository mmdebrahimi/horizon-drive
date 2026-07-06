"""Decisive-test signal / systematics / noise budget.

Proves (or refutes) that the definitive tapered-cavity-thrust experiment can
resolve the predicted QI signal and, crucially, that its power comes from the
Q-SCALING DISCRIMINATOR, not from raw sensitivity.

Claim under test:  F = eta * P * Q / c   (eta calibrated to Eagleworks:
1.2 mN/kW at Q = 5e4  ->  eta ~ 0.007).

Everything here is order-of-magnitude by design; the point is the RATIOS and how
they scale with Q. Run:  python decisive_test_budget.py
"""
from __future__ import annotations
import math

c = 2.998e8            # m/s
g = 9.81               # m/s^2

# --- calibrate eta to the Eagleworks claim -------------------------------
F_eag, P_eag, Q_eag = 1.2e-3, 1.0e3, 5.0e4      # 1.2 mN at 1 kW, Q~5e4
eta = F_eag * c / (P_eag * Q_eag)
# sanity: reproduce the claim
assert abs(eta * P_eag * Q_eag / c - F_eag) < 1e-9

# --- experiment operating point ------------------------------------------
P = 10.0               # W CW input, held FIXED across all phases (the key)

# Three Q phases (the escalation ladder). Q held to conservative values.
phases = [
    ("Phase 1  copper, 300 K", 5.0e4),
    ("Phase 2  Nb, 4 K",       1.0e8),
    ("Phase 3  Nb 2K / Nb3Sn", 1.0e10),
]

# --- systematics models (all scale with P, i.e. FLAT in Q) ----------------
# Photon-recoil floor (fundamental, unavoidable):
F_photon = P / c
# Thermal radiometric recoil: asymmetric IR from a body dissipating ~P in vacuum.
# k_rad = fractional front/back radiation asymmetry (order 1). All input power is
# dissipated as wall heat at steady state REGARDLESS of Q -> flat in Q.
k_rad = 2.0
F_thermal = k_rad * P / c
# Thermal-expansion CoM-drift artifact: large but LOW FREQUENCY -> rejected by
# AC modulation + lock-in, so it is a drift to null, not a sensitivity floor.
F_expansion_drift = 1.0e-6      # ~1 uN-equivalent slow drift (handled by modulation)

# --- torsion-balance metrology -------------------------------------------
# Force-noise spectral density at the ~0.01-0.1 Hz modulation band.
S_force = 1.0e-8       # N/sqrt(Hz)  (a good sub-uN torsion balance)
SNR = 5.0

def integ_time(F_target: float) -> float:
    """Averaging time (s) to reach SNR against balance noise for a DC-ish force."""
    return (SNR * S_force / F_target) ** 2

# --- report ---------------------------------------------------------------
def line(*cols, w=(26, 12, 12, 12, 12, 12)):
    print("".join(str(x).ljust(wi) for x, wi in zip(cols, w)))

print(f"eta (calibrated to Eagleworks) = {eta:.4f}")
print(f"Fixed input power P = {P:.0f} W CW")
print(f"Photon-recoil floor  F=P/c        = {F_photon*1e9:8.1f} nN")
print(f"Thermal radiometric (k_rad={k_rad}) = {F_thermal*1e9:8.1f} nN   (scales with P, FLAT in Q)")
print(f"Balance noise density             = {S_force:.0e} N/sqrt(Hz)")
print()
line("phase", "Q", "F_QI", "F_QI/phot", "t@SNR5", "v_break")
line("", "", "(N)", "(x floor)", "(s)", "(m/s)")
print("-" * 90)
rows = []
for name, Q in phases:
    F_QI = eta * P * Q / c
    ratio_photon = F_QI / F_photon           # = eta*Q
    ratio_thermal = F_QI / F_thermal
    t = integ_time(F_QI)
    v_break = P / F_QI                        # thermodynamic break-even speed
    rows.append((name, Q, F_QI, ratio_photon, ratio_thermal, t, v_break))
    line(name, f"{Q:.0e}",
         f"{F_QI:.3e}", f"{ratio_photon:.1e}",
         f"{t:.1e}", f"{v_break:.1f}")

print("-" * 90)
print()
print("KEY RESULTS")
print(f"  * Sensitivity is NOT the limit: even the photon floor ({F_photon*1e9:.0f} nN) is")
print(f"    resolvable at SNR {SNR:.0f} in {integ_time(F_photon):.1f} s. The QI signals need ms.")
print( "  * The experiment is limited ENTIRELY by systematics control, not noise.")
print( "  * Q-scaling discriminator: F_QI/F_thermal grows from "
      f"{rows[0][4]:.0f}x (Phase 1) to {rows[-1][4]:.1e}x (Phase 3),")
print( "    because F_QI ~ Q while every systematic ~ P (flat in Q).")
print( "    No known false-positive tracks cavity Q linearly -> this is the killer test.")
print(f"  * Even Phase 1 (cheap copper, 300 K) beats the thermal floor by {rows[0][4]:.0f}x,")
print( "    so it decisively replicates-or-refutes Eagleworks with a proper null suite.")
print(f"  * Thermodynamic self-check: a POSITIVE Phase-3 result (F={rows[-1][2]:.2f} N) implies")
print(f"    energy break-even at {rows[-1][6]:.0f} m/s -> either artifact, or the momentum")
print( "    is drawn from a reaction reservoir (inertia-modifier, NOT reactionless).")

# --- machine-checkable assertions (the 'bar') -----------------------------
assert F_photon > 0
# every phase's predicted signal must clear the thermal systematic by >= 10x
for name, Q, F_QI, rp, rt, t, v in rows:
    assert rt >= 10.0, f"{name}: signal only {rt:.1f}x thermal (need >=10x)"
# the Q-scaling ratio must span >= 4 orders across the ladder
span = rows[-1][3] / rows[0][3]
assert span >= 1e4, f"Q-scaling span only {span:.1e} (need >=1e4)"
print()
print(f"BUDGET OK: all phases clear thermal by >=10x; Q-scaling span = {span:.1e}. "
      "Design is resolution-capable.")
