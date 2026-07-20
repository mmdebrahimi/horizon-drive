"""Design-review calcs for the HD-CU-CAV-001 copper resonant cavity.

Grounds the optimization review with executed numbers rather than assertions:
  - skin depth at the operating frequency
  - roughness -> Q degradation (Hammerstad) for Ra 0.4 / 0.8 / 1.6 um
  - aluminium-vs-copper Q ratio (does a cheap Al prototype still clear Q>=20k?)
  - electroplate thickness expressed in skin depths (is plated Cu 'as good as' solid?)
  - quarter-wave choke-joint length (relaxes the mouth-seam contact requirement)
  - TM010 pillbox reference size

All first-principles; no external deps.
"""
import math

f0    = 1.836e9          # Hz, design resonance
c     = 2.998e8
mu0   = 4*math.pi*1e-7
sig_Cu = 5.80e7          # S/m
sig_Al = 3.50e7          # S/m (~60% IACS)
Q_design = 27000.0       # solid-copper design target
GATE = 20000.0           # Stage-0 acceptance

def skin_depth(sigma, f=f0):
    return 1.0/math.sqrt(math.pi*f*mu0*sigma)

def rough_K(Ra_um, delta_m):
    # Hammerstad-Bekkadal: Rs_rough/Rs_smooth = 1 + (2/pi) atan(1.4 (rms/delta)^2)
    rms = 1.11*Ra_um*1e-6          # RMS ~ 1.11*Ra (Gaussian)
    return 1.0 + (2/math.pi)*math.atan(1.4*(rms/delta_m)**2)

d_Cu = skin_depth(sig_Cu)
d_Al = skin_depth(sig_Al)

print("="*66)
print("HD-CU-CAV-001  DESIGN-REVIEW CALCS")
print("="*66)
print(f"f0 = {f0/1e9:.3f} GHz   lambda = {c/f0*1000:.1f} mm")
print(f"skin depth: Cu {d_Cu*1e6:.2f} um   Al {d_Al*1e6:.2f} um")

print("\n[1] Surface finish -> Q  (solid-copper baseline Q0 = 27,000)")
for Ra in (0.4, 0.8, 1.6, 3.2):
    K = rough_K(Ra, d_Cu)
    Q = Q_design / K
    tag = "clears gate" if Q >= GATE else "BELOW GATE"
    print(f"   Ra {Ra:>4} um -> Rs x{K:.3f} -> Q ~ {Q:7.0f}   ({tag})")

print("\n[2] Aluminium prototype (Q ~ sqrt(sig_Al/sig_Cu) x copper)")
ratio = math.sqrt(sig_Al/sig_Cu)
Q_Al = Q_design*ratio
print(f"   Q_Al/Q_Cu = sqrt({sig_Al:.1e}/{sig_Cu:.1e}) = {ratio:.3f}")
print(f"   bare-Al cavity Q ~ {Q_Al:.0f}   ({'clears' if Q_Al>=GATE else 'below'} the {GATE:.0f} gate)")
print(f"   -> a cheap Al rig-shakedown cavity is {'viable' if Q_Al>=GATE else 'marginal'} for first light")

print("\n[3] Copper electroplate thickness vs skin depth (RF sees only the surface)")
for t_um in (5, 15, 25, 50):
    print(f"   {t_um:>2} um Cu plate = {t_um/(d_Cu*1e6):4.1f} skin depths"
          f"  ({'OK (>5)' if t_um/(d_Cu*1e6) > 5 else 'too thin'})")
print("   -> plated/electroformed Cu on a cheap substrate ~= solid-Cu Q (bulk is irrelevant)")

print("\n[4] Quarter-wave choke joint at the mouth seam (kills seam-contact loss)")
lam = c/f0
print(f"   lambda/4 = {lam/4*1000:.1f} mm  choke groove depth in the flange")
print("   -> presents ~0 ohm at the seam without metal-to-metal contact; relaxes flatness spec")

print("\n[5] TM010 pillbox reference (if the taper is NOT mechanistically required)")
a = 2.405*c/(2*math.pi*f0)
print(f"   pillbox radius a = {a*1000:.1f} mm  (dia {2*a*1000:.0f} mm) for TM010 at f0")
print("   straight cylindrical bore is FAR easier to mirror-finish than a blind cone")

# sanity assertions
assert 1.4 < d_Cu*1e6 < 1.7
assert rough_K(0.4, d_Cu) < rough_K(0.8, d_Cu) < rough_K(1.6, d_Cu)
assert Q_Al < Q_design
print("\nAll sanity checks passed.")
