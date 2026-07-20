"""Resolves the taper-vs-pillbox design fork with the QI geometry factor.

McCulloch's quantised-inertia (QI/MiHsC) thrust law for an EmDrive-family
cavity is  F = (P*Q*L/c) * (1/Ds - 1/Db),  Ds/Db = small/big end diameter.
The bracket is the GEOMETRY FACTOR. For a symmetric cavity (Ds == Db) it is
EXACTLY ZERO -> a cylinder/pillbox produces no thrust under this theory. The
frustum asymmetry is not a fabrication convenience; it IS the mechanism.

This script computes the geometry factor for HD-CU-CAV-001's frustum, shows
the pillbox null, and (honestly) flags that the QI absolute-thrust magnitude
is a DIFFERENT calibration from the horizon-drive's F = eta*P*Q/c law -- so we
compare GEOMETRY DEPENDENCE (which both share: symmetric -> zero), not the
absolute number.  Exit 0 == checks pass.
"""
import math

c = 2.998e8

# HD-CU-CAV-001 frustum (m)
Ds = 0.090   # small end (base) diameter
Db = 0.160   # big end (mouth) diameter
L  = 0.120   # axial length

def qi_geometry_factor(ds, db, length):
    """L * (1/Ds - 1/Db)  [dimensionless-ish, 1/m * m]; zero iff ds==db."""
    return length * (1.0/ds - 1.0/db)

G_frustum = qi_geometry_factor(Ds, Db, L)
G_pillbox = qi_geometry_factor(0.125, 0.125, L)   # Ds==Db -> must be 0

print("=" * 64)
print("TAPER-vs-PILLBOX FORK  --  QI geometry factor")
print("=" * 64)
print(f"HD-CU-CAV-001 frustum: Ds={Ds*1e3:.0f} mm, Db={Db*1e3:.0f} mm, L={L*1e3:.0f} mm")
print(f"  1/Ds - 1/Db = {1/Ds:.3f} - {1/Db:.3f} = {1/Ds-1/Db:.3f} /m")
print(f"  geometry factor G = L*(1/Ds-1/Db) = {G_frustum:.4f}   (NONZERO -> thrust allowed)")
print(f"\nsymmetric pillbox (Ds==Db):")
print(f"  geometry factor G = {G_pillbox:.4f}   (EXACTLY ZERO -> NO thrust by construction)")

print("\n" + "-" * 64)
print("DECISION:")
print("  * KEEP THE FRUSTUM. Under QI/MiHsC the asymmetry is the mechanism;")
print("    a pillbox is a null-by-design.")
print("  * The pillbox becomes the ideal NULL-CONTROL article: same material,")
print("    same finish, same drive -> must read ZERO. A nonzero pillbox reading")
print("    would flag a systematic (thermal/ionic/EM), exactly what we must rule out.")

print("\nHONESTY NOTE:")
print("  QI's absolute thrust (F=PQL/c * dG) is a DIFFERENT calibration from the")
print("  horizon-drive law F=eta*P*Q/c (eta fit to Eagleworks' MEASURED 1.2 mN/kW).")
print("  They disagree on MAGNITUDE by ~1-2 orders; we rely only on the GEOMETRY")
print("  DEPENDENCE both share: symmetric cavity -> zero. Magnitude is not claimed here.")
print("  Caveat: QI is a fringe theory; high-precision tests (Tajmar) found NO thrust")
print("  to the nN floor. This resolves 'which geometry IF the effect is real', not")
print("  'the effect is real'.")

# self-checks
assert abs(G_pillbox) < 1e-12,       "pillbox geometry factor must be exactly 0"
assert G_frustum > 0.5,              "frustum geometry factor should be clearly nonzero"
assert 1/Ds > 1/Db,                  "small end must allow fewer Unruh waves (higher 1/D)"
print("\nAll self-checks passed.  (exit 0)")
