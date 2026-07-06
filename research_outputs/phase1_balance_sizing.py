"""Phase-1 torsion-balance sizing for the cheap (room-temperature copper) decisive test.

Grounds the build spec: given a target balance resonant frequency, it solves for a
real tungsten torsion fibre and reports the deflection produced by the predicted
12 uN QI signal and by the 33 nN photon floor, versus an interferometer's readout
resolution. Proves the cheap bench apparatus can actually see the signal with
enormous margin (the whole point: Phase 1 is systematics-limited, not sensitivity-
limited). Run:  python phase1_balance_sizing.py
"""
from __future__ import annotations
import numpy as np

c = 2.998e8
ETA = 0.0072

# --- operating point (Phase 1: copper, room temperature) ------------------
P = 10.0                 # W CW
Q_CU = 5.0e4             # copper cavity quality factor (Eagleworks-class)
F_signal = ETA * P * Q_CU / c        # predicted QI thrust (N)
F_photon = P / c                     # photon-recoil floor (N)

# --- balance geometry -----------------------------------------------------
r = 0.15                 # m, moment arm (cavity offset from fibre axis)
L_fib = 0.30             # m, torsion fibre length
G_W = 161e9              # Pa, shear modulus of tungsten
m_cav = 3.0              # kg, copper frustum
m_cw = 3.0               # kg, counterweight (balances the beam)
I_bal = (m_cav + m_cw) * r**2        # kg m^2, moment of inertia about fibre

# --- design knob: choose a target resonant frequency, solve for the fibre --
f_res = 0.08             # Hz  (period ~12.5 s)
f_mod = 0.02             # Hz  modulation, comfortably BELOW f_res (quasi-static)
omega = 2 * np.pi * f_res
kappa = omega**2 * I_bal             # required torsional stiffness (N m / rad)
# kappa = pi G d^4 / (32 L)  ->  solve for fibre diameter d
d_fib = (32 * L_fib * kappa / (np.pi * G_W)) ** 0.25

# --- deflections ----------------------------------------------------------
def deflection(F):
    tau = F * r                      # torque
    theta = tau / kappa              # angular deflection (rad)
    dx = r * theta                   # arm-tip linear displacement (m)
    return theta, dx

th_s, dx_s = deflection(F_signal)
th_p, dx_p = deflection(F_photon)

READOUT = 1e-9           # m, interferometer displacement resolution (~1 nm, conservative)
S_F = 1e-8               # N/sqrt(Hz) force-noise floor
def integ_time(F, snr=5):
    return (snr * S_F / F) ** 2

# --- report ---------------------------------------------------------------
print("PHASE-1 (copper, 300 K) torsion-balance sizing")
print(f"  predicted QI signal  F = {F_signal*1e6:6.2f} uN   (Q={Q_CU:.0e}, P={P:.0f} W)")
print(f"  photon-recoil floor    = {F_photon*1e9:6.1f} nN")
print()
print(f"  moment arm r           = {r*100:.0f} cm")
print(f"  fibre: tungsten, L     = {L_fib*100:.0f} cm, target f_res = {f_res} Hz")
print(f"    -> stiffness kappa   = {kappa:.3e} N m/rad")
print(f"    -> fibre diameter d  = {d_fib*1e3:.2f} mm      (machinable: {0.1 < d_fib*1e3 < 2.0})")
print(f"  moment of inertia I    = {I_bal:.3f} kg m^2  (resonant period {1/f_res:.1f} s)")
print()
print(f"  deflection @ 12 uN signal : theta = {th_s*1e3:.3f} mrad  ->  arm tip {dx_s*1e6:8.1f} um")
print(f"  deflection @ 33 nN photon : theta = {th_p*1e6:.3f} urad  ->  arm tip {dx_p*1e9:8.1f} nm")
print(f"  interferometer resolution : {READOUT*1e9:.1f} nm")
print(f"    -> signal / readout margin = {dx_s/READOUT:.1e}x   (photon floor {dx_p/READOUT:.1e}x)")
print()
print(f"  lock-in integration @ SNR 5: signal {integ_time(F_signal):.1e} s ; "
      f"photon floor {integ_time(F_photon):.1f} s")
print(f"  modulation f_mod = {f_mod} Hz  (< f_res {f_res} Hz: quasi-static, valid)")

# --- feasibility assertions (the bar) -------------------------------------
assert 0.1 < d_fib*1e3 < 2.0, f"fibre diameter {d_fib*1e3:.2f} mm out of machinable range"
assert dx_s / READOUT > 1e3, "signal deflection not comfortably above readout"
assert dx_p > READOUT, "photon floor below readout resolution"
assert f_mod < f_res, "modulation not below resonance (quasi-static invalid)"
print()
print("SIZING OK: a bench tungsten-fibre torsion balance resolves the 12 uN signal with")
print(f"  {dx_s/READOUT:.0e}x margin and even the photon floor by {dx_p/READOUT:.0f}x. Phase 1 is")
print("  entirely systematics-limited -> the null-test suite is the real work, not the balance.")
