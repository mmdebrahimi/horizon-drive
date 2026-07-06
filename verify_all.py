"""One-command reproducibility harness for the whole Horizon-Drive package.

Clone the repo, run `python verify_all.py`, and watch every headline number in
the three articles + the decisive-experiment design reproduce from the code, and
every computational artifact pass its own self-checks. This is the differentiator
of an honest package: the claims are not asserted, they are recomputed.

Runs in ~1 minute. Exit 0 == everything reproduces.
"""
from __future__ import annotations
import subprocess, sys, math, os

ROOT = os.path.dirname(os.path.abspath(__file__))
RO = os.path.join(ROOT, "research_outputs")
c = 2.998e8
eta = 0.0072
ok = []

def check(name, cond, detail=""):
    ok.append(cond)
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))

print("=" * 70)
print("HORIZON-DRIVE REPRODUCIBILITY HARNESS")
print("=" * 70)

# ---- 1. shared-constant cross-check: recompute every headline number --------
print("\n[1] Headline numbers recomputed from first principles")
# eta calibrated to Eagleworks (1.2 mN/kW at Q=5e4)
eta_cal = 1.2e-3 * c / (1e3 * 5e4)
check("eta calibration = 0.0072", abs(eta_cal - eta) < 5e-5, f"{eta_cal:.4f}")
# thrust law: 240 N per 1 kW cell at Q=1e10
F_cell = eta * 1e3 * 1e10 / c
check("240 N per 1 kW cell (Q=1e10)", abs(F_cell - 240) < 2, f"{F_cell:.1f} N")
# craft: 62 cells, T/W 1.5 on a 1 t craft
tw_thrust = 1000 * 9.80665 * 1.5
n_cells = math.ceil(tw_thrust / F_cell)
check("62 cells for a 1 t craft at T/W 1.5", n_cells == 62, f"{n_cells} cells")
# max hover mass of 62 cells
m_hover = 62 * F_cell / 9.80665
check("62 cells hover up to ~1.5 t", 1500 < m_hover < 1550, f"{m_hover:.0f} kg")
# decisive experiment (P=10 W)
check("Phase-1 signal ~12 uN (Q=5e4)", abs(eta*10*5e4/c - 1.2e-5) < 1e-7, f"{eta*10*5e4/c*1e6:.1f} uN")
check("photon floor ~33 nN (10 W)", abs(10/c - 3.34e-8) < 1e-9, f"{10/c*1e9:.1f} nN")
check("Phase-3 signal ~2.4 N (Q=1e10)", abs(eta*10*1e10/c - 2.40) < 0.05, f"{eta*10*1e10/c:.2f} N")

# ---- 2. run every computational artifact (each self-asserts) ----------------
print("\n[2] Computational artifacts (each runs its own assertions)")
scripts = [
    ("decisive_test_budget.py", "signal/noise budget"),
    ("decisive_test_sim.py", "measurement digital-twin"),
    ("phase1_balance_sizing.py", "Phase-1 balance sizing"),
]
for fname, desc in scripts:
    path = os.path.join(RO, fname)
    r = subprocess.run([sys.executable, path], capture_output=True, text=True)
    check(f"{fname} ({desc})", r.returncode == 0,
          "OK" if r.returncode == 0 else r.stderr.strip().splitlines()[-1] if r.stderr else "nonzero exit")

# ---- 3. device_sim digital twin (quick fault campaign) ----------------------
print("\n[3] Flight digital-twin (quick Monte-Carlo fault campaign)")
try:
    sys.path.insert(0, ROOT)
    from device_sim.montecarlo import campaign
    s = campaign(n_runs=6, duration=30, dt=0.02, max_quench=6, base_seed=7)
    check("device_sim: 0 divergences", s.diverged == 0, f"diverged={s.diverged}")
    check("device_sim: survival >= 0.8", s.survival_rate >= 0.8, f"{s.survival_rate*100:.0f}%")
except Exception as e:
    check("device_sim campaign", False, f"{type(e).__name__}: {e}")

# ---- verdict ---------------------------------------------------------------
print("\n" + "=" * 70)
if all(ok):
    print(f"ALL {len(ok)} CHECKS PASSED -- the entire package reproduces from the code.")
    sys.exit(0)
else:
    print(f"FAILURES: {ok.count(False)} of {len(ok)} checks failed.")
    sys.exit(1)
