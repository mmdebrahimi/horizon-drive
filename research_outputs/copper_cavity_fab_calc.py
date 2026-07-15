"""Fabrication calc for the buildable copper thrust-cell (inertia-modifying element).

Grounds the machinist dimensions: resonant frequency of the cavity mode, the
copper Q you can actually expect at room temperature (so nobody over-promises),
the RF drive power for a target stored energy, and the wall-loss heat the bench
must dissipate. Copper tier only -- no niobium, no cryogenics, no HF.

Run:  python copper_cavity_fab_calc.py
"""
from __future__ import annotations
import math

c = 2.998e8
mu0 = 4e-7 * math.pi
eps0 = 8.854e-12

# --- geometry (from the design; frustum approximated as a right cylinder of
#     the mean radius for the TM010 mode estimate) ---------------------------
d_big = 0.160            # m  large-end diameter
d_small = 0.090         # m  small-end diameter
length = 0.120          # m  axial length
a_mean = 0.25 * (d_big + d_small) / 2 + 0.25 * (d_big + d_small) / 2  # = mean radius
a_mean = ((d_big + d_small) / 2) / 2                                   # mean radius (m)

# TM010 resonant frequency of a cylindrical pillbox: f = 2.405 c / (2 pi a)
j01 = 2.405
f_res = j01 * c / (2 * math.pi * a_mean)

# --- copper surface resistance at f_res, room temp ------------------------
sigma_cu = 5.96e7        # S/m  copper conductivity (300 K)
omega = 2 * math.pi * f_res
delta = math.sqrt(2 / (omega * mu0 * sigma_cu))     # skin depth
Rs = 1 / (sigma_cu * delta)                          # surface resistance (ohm)

# --- geometry factor + Q (pillbox TM010, closed-form) ---------------------
# G = eta0 * j01 / (2 * (1 + a/L)) with eta0 = 377 ohm  (standard pillbox result)
eta0 = math.sqrt(mu0 / eps0)
G = eta0 * j01 / (2 * (1 + a_mean / length))
Q0 = G / Rs

# --- drive: stored energy + wall loss at a target field -------------------
P_drive = 10.0           # W CW (matches the decisive-test operating point)
U_stored = Q0 * P_drive / omega          # J stored in the cavity at steady state
P_wall = P_drive                         # at critical coupling, all drive -> wall heat

print("COPPER THRUST-CELL FABRICATION CALC (room temperature)")
print(f"  geometry: big {d_big*1000:.0f} mm / small {d_small*1000:.0f} mm / L {length*1000:.0f} mm")
print(f"  mean radius a          = {a_mean*1000:.1f} mm")
print(f"  TM010 resonant freq    = {f_res/1e9:.3f} GHz   (target machining sets this)")
print(f"  skin depth @ f_res     = {delta*1e6:.2f} um   -> polish + plate matter")
print(f"  surface resistance Rs  = {Rs*1e3:.2f} mohm")
print(f"  geometry factor G      = {G:.0f} ohm")
print(f"  EXPECTED copper Q0     = {Q0:,.0f}   (room-temp; ~1e4, NOT the 1e10 SRF dream)")
print(f"  stored energy @ {P_drive:.0f} W    = {U_stored*1e3:.2f} mJ")
print(f"  wall heat to remove    = {P_wall:.0f} W  (all drive power at critical coupling)")
print()

# --- assertions: the numbers must be sane + machinable --------------------
assert 1e9 < f_res < 6e9, f"f_res {f_res/1e9:.2f} GHz outside a practical RF band"
assert 5e3 < Q0 < 5e4, f"copper Q {Q0:.0f} not in the realistic room-temp range"
assert delta < 5e-6, "skin depth implausibly large"
print("FAB CALC OK: cavity resonates in the low-GHz band, room-temp copper Q ~1e4")
print("  (this is the HONEST Q -- the 240 N/kW thrust needs Q=1e10, which needs the")
print("   niobium/cryogenic tier; the copper cell is what you build to TEST the effect,")
print("   where the predicted signal is ~12 uN, not thrust you can feel).")
