"""Signal-to-artifact ratio vs cavity quality (Q) — the 'how good must we build' calc.

CENTRAL PHYSICS:
  Signal    F_sig = eta * P * Q / c      -> scales with Q AND power.
  Artifacts (thermal, EM, radiometric) scale with DISSIPATED POWER or are fixed
  -> they do NOT grow with Q.
Therefore SNR = F_sig / A_floor scales with Q at fixed power. Raising POWER does
NOT help (it lifts the power-scaling artifacts too). **Q is the only clean lever.**

This answers: at what QUALITY (Q) does the signal reliably beat the environment,
and is a room-temp copper test enough, or must we go cryogenic / superconducting.
Exit 0 == checks pass.
"""
c = 2.998e8
eta = 0.0072
P = 10.0                       # W dissipated (fixed; more power doesn't help SNR)

def signal_N(Q, P=P):
    return eta * P * Q / c     # Newtons

# Residual artifact FLOOR after the full mitigation stack (the KEY uncertainty).
# Raw artifacts ~15-44 uN at 10 W; the discriminator stack suppresses them, but
# HOW WELL is the open question. Bracket it:
FLOOR_OPT  = 0.3e-6            # N, optimistic (well-built, Tajmar-class ~0.1-0.3 uN)
FLOOR_PESS = 3.0e-6           # N, pessimistic (imperfect mitigation ~1-3 uN)

rungs = [
    ("Room-temp copper", 2.7e4),
    ("Cryo copper ~4 K (RRR)", 1.0e5),
    ("Niobium / Nb3Sn (SC)", 1.0e10),
]

def snr(Q, floor):
    return signal_N(Q) / floor

print("=" * 72)
print("SIGNAL-vs-ENVIRONMENT  (P=10 W fixed; Q is the only clean lever)")
print("=" * 72)
print(f"{'rung':<26}{'Q':>10}{'signal':>11}{'SNR(opt)':>10}{'SNR(pess)':>11}")
for name, Q in rungs:
    s = signal_N(Q)
    print(f"{name:<26}{Q:>10.0e}{s*1e6:>9.1f}uN{snr(Q,FLOOR_OPT):>10.0f}{snr(Q,FLOOR_PESS):>11.1f}")

print(f"\nResidual artifact floor assumed: {FLOOR_OPT*1e6:.1f} uN (opt) .. "
      f"{FLOOR_PESS*1e6:.1f} uN (pess)  <-- the key uncertainty")

# Required Q for a target SNR, at each floor
def Q_needed(target, floor, P=P):
    # F_sig = eta*P*Q/c = target*floor  ->  Q = target*floor*c/(eta*P)
    return target * floor * c / (eta * P)

print("\nQ REQUIRED to reach a target SNR (at P=10 W):")
for target in (10, 100):
    qo = Q_needed(target, FLOOR_OPT); qp = Q_needed(target, FLOOR_PESS)
    print(f"  SNR >= {target:>3}:  Q >= {qo:.1e} (opt floor) .. {qp:.1e} (pess floor)")

print("""
READING:
  * Room-temp copper (Q~2.7e4): SNR ~2..22 -> WORKS ONLY IF mitigation is good;
    MARGINAL if not. This is exactly the user's worry -- thin, mitigation-dependent.
  * Cryo copper (Q~1e5): SNR ~8..80 -> CONFIDENT across the mitigation uncertainty,
    WITHOUT a superconductor. This is the sweet spot to 'beat the environment'.
  * Niobium (Q~1e10): SNR ~1e6 -> UNAMBIGUOUS, mitigation-irrelevant. Overkill for
    DETECTION; that margin is what the propulsion-grade craft needs, not the test.

KEY: SNR>=10 needs Q ~ 1e4..1.3e5  -> reachable at CRYO-COPPER, no SC needed.
     SNR>=100 needs Q ~ 1e5..1.3e6 -> approaching the superconductor rung.
POWER is NOT a lever (artifacts scale with it); SIZE is a weak lever (Q~1/sqrt(f)).
TEMPERATURE (which raises Q via lower surface resistance) is THE lever.
BONUS: going cryogenic ALSO gives ultra-high vacuum for free (cryopumping) ->
       the cryostat replaces the separate turbo/chamber, folding two costs into one.
""")

# self-checks
assert snr(2.7e4, FLOOR_PESS) < 10,  "room-temp Cu should be marginal at pessimistic floor"
assert snr(1e5, FLOOR_PESS) >= 8,    "cryo-Cu should clear SNR~8 even pessimistically"
assert snr(1e10, FLOOR_OPT) > 1e5,   "Nb should be absurdly clean"
assert Q_needed(10, FLOOR_PESS) < 2e5, "SNR>=10 must be reachable below the SC rung"
assert abs(signal_N(5e4)-12e-6) < 1e-6, "sanity: 12 uN at Q=5e4, P=10W"
print("All checks passed.  (exit 0)")
