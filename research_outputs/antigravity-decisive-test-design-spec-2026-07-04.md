# Anti-Gravity — Decisive-Test Design Spec (converting the external wall to a buildable design)

> Captured 2026-07-04. Hand-authored engineering-design memo (schema-drift by design). Converts the "external wall" from the inertia-thread closeout (`antigravity-inertia-thread-recommendations-resolved-2026-07-04.md`) into a concrete, costed experiment design. Numbers verified `/tmp/thrust_balance.py` (exit 0; CODATA). North star: `plans/Anti_Gravity_idea-anchor.md`.
> **Integrity note (verify-in-batch catch):** the first pass of this noise budget mis-framed the Q-enhanced number as an uncontested "signal." Corrected: the Q-enhancement is precisely the *disputed* physics; the honest test resolves whether *any* thrust exceeds the undisputed bare-photon floor, with artifacts nulled below it.

---

## What this memo is (and is not)

This is the **code-closable half** of the one live thread (D1, inertia-from-vacuum / horizon drive). An agent cannot *run* a thrust experiment (external wall: physical rig + hardware budget), but it *can* fully **design** it — derive the noise budget, identify the dominant artifact, and specify the isolation that would make the test decisive. That design is below. It is not a claim that QI works; it is the spec for the measurement that would settle it.

---

## The two reference scales (the honest framing)

For a bench device at $P_{\rm in}=100$ W:

| Scale | Value | Status |
|---|---|---|
| **Bare photon-rocket floor** $P/c$ | **0.33 µN** | REAL, undisputed — *any* powered radiating device produces this |
| QI/EmDrive Q-enhanced claim ($Q=10^3$–$10^4$) | 0.33 – 3.3 mN | **DISPUTED** — the Q-enhancement IS the contested QI-specific physics |

**The decisive question is not "is there thrust?" (the 0.33 µN photon floor guarantees a tiny yes) — it is "is there thrust *exceeding* the bare-photon floor?"** i.e. does the Q-enhancement exist. That reframing is what makes the test well-posed.

---

## Noise budget — artifacts are CO-SCALE with the claim (why naive tests are worthless)

All computed for the 100 W / 0.01 m² device (`/tmp/thrust_balance.py`):

| Artifact | Magnitude | vs 0.33 µN photon floor |
|---|---|---|
| **[A4] EMI — Lorentz force on power leads** (10 A, 10 cm, Earth's 50 µT) | **50 µN** | **SWAMPS by 150×** — the dominant artifact |
| [A2] Outgassing "rocket" @ HV ($10^{-3}$ Pa) | 0.64 µN | SWAMPS |
| [A1] Thermal photon-recoil, 10% radiative asymmetry | 0.033 µN | below floor |
| [A2] Outgassing @ UHV ($10^{-8}$ Pa) | $6\times10^{-6}$ µN | negligible |
| [A2] Outgassing @ VHV ($10^{-6}$ Pa) | $6\times10^{-4}$ µN | below floor |

**The core insight:** the *claimed* QI thrust (µN–mN) and the lab *artifacts* (µN–mN) are the **same order of magnitude**. A naive setup has **S/N ≈ 1** — it fundamentally cannot distinguish a real signal from EMI + outgassing + thermal recoil. **This is exactly why every historical "positive" (Shawyer, NASA Eagleworks) evaporated** — they measured at S/N≈1 and mistook artifacts for thrust.

---

## Derived isolation spec (to make the test decisive — S/N ≥ 10 on the photon floor)

Artifacts must be nulled to **< 33 nN** (10× below the 0.33 µN bare-photon floor), then look for thrust *above* the floor:

| Subsystem | Requirement | Kills |
|---|---|---|
| **Vacuum** | ≤ $10^{-8}$ Pa (UHV, baked) | A2 outgassing → sub-nN; A3 radiometric → sub-nN |
| **Thermal** | radiative shroud, ΔT < 0.05 K, symmetric emission geometry | A1 recoil → sub-nN |
| **EMI (dominant)** | superconducting or tightly-twisted/balanced leads + µ-metal shield + **current-reversal null** | A4 (the 50 µN worst case) → sub-nN |
| **Readout** | torsion balance, **≤ 3 nN resolution**, in-vacuum interferometric pickoff | — |
| **Controls (decisive)** | (i) **orientation-flip** — real thrust reverses, artifacts don't; (ii) **dummy ohmic load** — same heat, no cavity; (iii) **Q-detune** — same power, no resonance | separates real thrust from heat/EMI |

---

## The result this design already implies

**Tajmar/Dresden (2018–21) built approximately this** (vacuum, shielding, orientation-flip, dummy-load controls) and measured **NULL** — the thrust dropped to the artifact floor and the QI-specific Q-enhancement did not appear. So:

- The bottleneck was **never an energy wall** (unlike Higgs/warp) — the horizon drive is energetically plausible (§REC1 of the closeout: ~4 MV/m suffices).
- It was **never un-testable** — the decisive test is a well-specified UHV torsion-balance measurement.
- It is a **precision wall that the best experiment has already pushed to null.** The honest state of D1: the one anti-gravity corner not refuted by *derivation* has been driven to null by *experiment*, at the ~µN sensitivity achieved so far. A decisive *positive* would require beating Tajmar — artifacts < 33 nN AND a thrust reproducibly above the bare-photon floor under orientation-flip. No such result exists.

---

## Honest close

**The entire anti-gravity investigation now terminates on a single sentence:** every corner is walled off by orders-of-magnitude, symmetry, or experimental null — and the *most* open corner (inertia-from-vacuum) is the one whose "no" is a **precision-limited experimental null**, not a fundamental impossibility. That is the most that can honestly be said. The remaining move — *beat Tajmar with a < 33 nN artifact floor* — is a real hardware experiment (external wall: apparatus + budget), fully specified above but not runnable in this environment.

**What this memo does NOT claim:** that QI is correct, that a better experiment would find thrust, or that the orbs are real. It claims — by derivation + verified noise budget — that the decisive test is *specified*, that its dominant artifact is *EMI on the leads*, and that the best existing version of it returned *null*.

---

## Appendix — verified (script `/tmp/thrust_balance.py`, exit 0)

| Quantity | Value | Role |
|---|---|---|
| Bare photon-rocket floor (100 W) | 0.33 µN | the undisputed bar |
| QI Q-enhanced claim ($Q=10^4$) | 3.3 mN | disputed multiplier |
| EMI artifact (10 A leads, Earth field) | 50 µN | **dominant** — must null to <33 nN |
| Outgassing @ HV vs UHV | 0.64 µN → $6\times10^{-6}$ µN | vacuum spec driver |
| Decisive artifact floor target | < 33 nN | 10× below photon floor |
| Readout resolution needed | ≤ 3 nN | torsion-balance spec |
