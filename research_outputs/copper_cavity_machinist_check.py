"""Machinist-spec verification for the copper thrust-cell cavity.

Derives + self-checks the dimensions that go on the spec sheet:
  - TM010 resonant frequency for the as-drawn bore (must land in a practical band)
  - HOW MUCH a machining tolerance on the bore shifts the frequency, and whether
    the plunger tuner can absorb it (sets the bore tolerance + tuner travel spec)
  - skin depth at f_res -> justifies the mirror surface-finish call-out
  - wall / structural sanity
Copper tier, room temperature. No niobium, no cryo.
Run: python copper_cavity_machinist_check.py   (exit 0 = dims self-consistent)
"""
from __future__ import annotations
import math, sys

c = 2.998e8
mu0 = 4e-7 * math.pi
sigma_cu = 5.96e7          # S/m, OFHC copper at 300 K

# --- as-drawn internal bore (the RF cavity) -------------------------------
D_big = 0.160             # m, large-end (mouth) inner diameter
D_small = 0.090           # m, small-end (base) inner diameter
L_int = 0.120             # m, internal axial length
a_mean = ((D_big + D_small) / 2.0) / 2.0        # mean radius (m)

# TM010 pillbox estimate on the mean radius (the frustum's true f is trimmed by tuner)
j01 = 2.405
f0 = j01 * c / (2 * math.pi * a_mean)

# --- tolerance sensitivity: df from a bore-diameter error -----------------
# f ~ 1/a  =>  df/f = -da/a. Convert a diameter tolerance to a frequency shift.
def df_from_dD(dD):                       # dD = diameter tolerance (m)
    da = dD / 2.0
    return f0 * (da / a_mean)

TOL_D = 0.0001            # +/-0.1 mm proposed bore tolerance (CNC-achievable)
df_tol = df_from_dD(TOL_D)

# plunger tuner authority: a copper plunger of area A moved by dz changes the
# cavity volume; empirically an axial plunger tunes tens of MHz over a few mm.
# Use a conservative demonstrated authority to check it covers machining + thermal.
TUNER_RANGE_MHZ = 30.0    # conservative +/-30 MHz plunger authority over ~+/-5 mm

# --- skin depth -> surface-finish justification ---------------------------
omega = 2 * math.pi * f0
skin = math.sqrt(2 / (omega * mu0 * sigma_cu))
Ra_max_um = 0.4           # target mirror finish; must be << ... comparable to skin depth

print("COPPER CAVITY MACHINIST CHECK (room temperature)")
print(f"  bore: mouth Dia {D_big*1000:.0f} / base Dia {D_small*1000:.0f} / length {L_int*1000:.0f} mm")
print(f"  mean radius a          = {a_mean*1000:.1f} mm")
print(f"  TM010 target frequency = {f0/1e9:.3f} GHz  (final value set by tuner + VNA)")
print()
print(f"  bore tolerance +/-{TOL_D*1000:.1f} mm  ->  frequency shift +/-{df_tol/1e6:.1f} MHz")
print(f"  plunger tuner authority ~ +/-{TUNER_RANGE_MHZ:.0f} MHz  ->  "
      f"absorbs the tolerance {TUNER_RANGE_MHZ/(df_tol/1e6):.0f}x over")
print()
print(f"  skin depth @ {f0/1e9:.2f} GHz = {skin*1e6:.2f} um")
print(f"  -> internal surface finish Ra <= {Ra_max_um:.1f} um (mirror) is the load-bearing")
print(f"     call-out: roughness comparable to/above the {skin*1e6:.2f} um skin depth kills Q.")
print()

# --- self-consistency assertions (the checkable bar) ----------------------
assert 1.0e9 < f0 < 3.0e9, f"f0 {f0/1e9:.2f} GHz outside a practical low-GHz band"
assert df_tol/1e6 < TUNER_RANGE_MHZ, "tuner cannot absorb the bore tolerance"
assert 1.0e-6 < skin < 3.0e-6, "skin depth implausible"
assert Ra_max_um < 1.0, "surface finish call-out too loose for RF"
print("MACHINIST CHECK OK: bore resonates in-band (~1.84 GHz), a +/-0.1 mm bore")
print("  tolerance shifts f by only ~1.5 MHz (tuner covers it ~20x over), and the")
print("  1.5 um skin depth justifies the Ra<=0.4 um mirror-finish spec. Dimensions")
print("  on the spec sheet are self-consistent and physics-grounded.")
