"""Material efficiency comparison for the resonant cavity (Q, price ignored).

Cavity Q ~ G / Rs  (G = geometry factor, fixed).  Rs = surface resistance.
For a NORMAL conductor  Rs = sqrt(pi f mu0 / sigma)  ->  Q ~ sqrt(sigma).
For a SUPERCONDUCTOR    Rs collapses to nano-ohms   ->  Q jumps ~10^6.

So the only way to *dramatically* beat copper is to leave the normal-metal
regime entirely (cryogenic superconductor). Among room-temp metals nothing is
more than a few % better than copper. This script shows both facts.
"""
import math

f = 1.836e9
mu0 = 4*math.pi*1e-7

def Rs_normal(sigma):
    return math.sqrt(math.pi*f*mu0/sigma)

# room-temperature conductivities (S/m, ~20C, annealed)
metals = {
    "Silver":            6.30e7,
    "Copper (OFHC)":     5.80e7,
    "Gold":              4.10e7,
    "Aluminium":         3.50e7,
    "Brass (70/30)":     1.60e7,
}
Rs_Cu = Rs_normal(metals["Copper (OFHC)"])
Q_Cu_room = 27000.0   # our design baseline

print("="*70)
print("ROOM-TEMPERATURE NORMAL METALS  (Q ~ sqrt(sigma), copper = 1.00x)")
print("="*70)
print(f"{'material':<16}{'sigma (S/m)':>13}{'Rs (mOhm)':>12}{'Q vs Cu':>10}{'-> Q':>10}")
for name, sig in sorted(metals.items(), key=lambda kv: -kv[1]):
    Rs = Rs_normal(sig)
    rel = Rs_Cu/Rs                     # Q ratio = Rs_Cu/Rs = sqrt(sig/sig_Cu)
    print(f"{name:<16}{sig:>13.2e}{Rs*1e3:>12.2f}{rel:>9.3f}x{rel*Q_Cu_room:>10.0f}")

print(f"\n  Copper Rs at {f/1e9:.3f} GHz = {Rs_Cu*1e3:.2f} mOhm")
print("  -> Silver, the best normal metal, buys only ~4% Q. Room temp is a wall.")

print("\n" + "="*70)
print("SUPERCONDUCTORS  (leave the normal-metal regime -> Rs in nano-ohms)")
print("="*70)
# representative RF surface resistances at ~1.3-2 GHz (literature order-of-magnitude)
sc = {
    "Nb  @2.0K (standard EP)":      1.0e-8,   # ~10 nOhm
    "Nb  @2.0K (N-doped, SOTA)":    5.0e-9,   # ~5 nOhm
    "Nb3Sn @4.2K":                  1.5e-8,   # ~15 nOhm, easier cooling
    "Cu  @300K (reference)":        Rs_Cu,
}
Rs_ref = sc["Cu  @300K (reference)"]
print(f"{'material/temp':<26}{'Rs (Ohm)':>12}{'Rs vs Cu':>12}{'-> Q ~':>12}")
for name, Rs in sc.items():
    ratio = Rs_ref/Rs
    print(f"{name:<26}{Rs:>12.1e}{ratio:>11.0f}x{ratio*Q_Cu_room:>12.2e}")

print("\n  -> Nb at 2 K gives Rs ~10^6x lower than copper -> Q ~ 10^10,")
print("     which is exactly the Q the propulsion claim needs.")

# sanity
assert Rs_normal(metals["Silver"]) < Rs_Cu < Rs_normal(metals["Aluminium"])
assert 8e-3 < Rs_Cu < 14e-3
print("\nSanity checks passed.")
