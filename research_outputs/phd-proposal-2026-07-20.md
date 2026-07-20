# PhD Research Proposal

## A Precision Null-Test of Claimed Anomalous Thrust in Resonant Microwave Cavities via a Quality-Factor-Scaling Discriminator

**Discipline:** Experimental physics / precision measurement (breakthrough-propulsion metrology)
**Draft:** 2026-07-20 · **Companion technical package:** github.com/mmdebrahimi/horizon-drive (reproducible, 19-check harness)

> **Framing note (deliberate).** This is proposed as a **precision-metrology thesis**, not a "build an anti-gravity drive" project. The deliverable is a *definitive measurement* plus a *novel artifact-rejection methodology* that is publishable and valuable **regardless of the sign of the result** — a clean, well-characterised null is a real contribution to the field, as the TU Dresden SpaceDrive nulls demonstrate. The extraordinary-claim posture is maintained throughout.

---

## Abstract
Several groups have reported anomalous thrust from resonant microwave cavities (the "EmDrive" class), inconsistent with conservation of momentum for a closed system. The most sensitive independent tests (TU Dresden, ~5 nN floor) have returned **null** results, attributing prior positive claims to thermal drift and electromagnetic feed-through. This thesis proposes a **decisive, methodologically novel null-test**: rather than seeking a single-point thrust, it measures the **scaling of any force with the cavity quality factor Q at fixed dissipated power** — the one signature that a genuine cavity effect (F ∝ Q) shares while *every* known environmental artifact remains flat in Q. The programme develops a cryogenically-tunable apparatus spanning **Q ≈ 3×10⁴ (copper, 300 K) → ~10⁵ (copper, 4 K) → ~10¹⁰ (Nb₃Sn, 4 K)** and applies an **orthogonal discriminator stack** (pressure-independence, 180° rotation, current-polarity reversal, constant-dissipated-power modulation, dual traceable force calibration, symmetric null-control cavity). The result is either the most stringent bound to date, or — improbably — a Q-scaling detection that survives every discriminator.

## 1. Background & motivation
- **The claim.** Microwave power in an asymmetric (truncated-cone) resonant cavity is reported to produce net thrust orders of magnitude above the photon limit F = P/c. Proposed mechanisms (e.g. McCulloch's quantised inertia) predict F ∝ P·Q·(geometry).
- **State of the art.** TU Dresden's SpaceDrive programme built torsion balances resolving ~5–100 nN and found **no thrust** for EmDrive- and Mach-Effect-class devices once thermal and EM systematics were controlled, bounding any effect ≥ orders of magnitude below prior claims.
- **The gap.** Prior tests (positive and null) largely evaluate a **single operating point**. No programme has systematically **varied Q while holding dissipated power fixed** and tested the **F ∝ Q** prediction directly — even though that scaling is the sharpest discriminator between a real cavity effect and a power-driven artifact. This thesis closes that gap.

## 2. Research questions & hypotheses (falsifiable)
- **RQ1.** Does the measured force on a resonant cavity scale with Q at fixed dissipated power? **H1 (test hypothesis):** F = η·P·Q/c with η ≠ 0. **H0 (null):** F consistent with zero / photon-limit, flat in Q.
- **RQ2.** Do all candidate systematics (thermal, EM, radiometric) remain flat in Q, as predicted? (Validates the discriminator.)
- **RQ3.** What is the tightest bound on η achievable across the copper→cryo-copper→superconducting Q-ladder?

## 3. Novelty & contribution (why this is a PhD, not a replication)
1. **The Q-scaling discriminator.** Varying Q at fixed dissipated power and fitting F(Q) isolates a real cavity effect from all flat-in-Q artifacts — a discriminator not previously applied to this problem.
2. **An orthogonal artifact-rejection stack.** A signal is accepted only if it survives *all* of: pressure-independence, 180° cavity-frame rotation, drive-current-polarity reversal, constant-dissipated-power lock-in, dual traceable force calibration agreeing <2%, and a symmetric null-control ("pillbox") cavity that must read zero. (A quantitative artifact budget shows several systematics individually exceed the target signal, so the *stack*, not any single check, is the contribution.)
3. **The cryogenic Q-ladder.** Extending from copper to Nb₃Sn spans ~6 orders of magnitude in Q, turning "detect a force" into "measure a slope" — a far stronger and more general test. *Methodology transfers to any resonant-cavity propulsion claim.*

## 4. Methodology
- **Apparatus** (fully specified in the technical package): cryostat (4 K, closed-cycle; cryopumps to ultra-high vacuum) → high-RRR copper cavity (frustum) + symmetric pillbox null-control → traceable RF chain (constant dissipated power, reflected power to a fixed off-balance dump) → PLL frequency-lock → cryo-compatible torsion balance (optical-lever → interferometer, in-vacuum 180° rotation) → dual force calibration (electrostatic + photon-pressure, traceable) → mu-metal + coaxial-zero-loop EM control → software lock-in with blind, randomized scheduling.
- **Campaign:** validate the force chain against a **known-answer control** (a Biefeld–Brown "lifter," which must read zero in vacuum) → characterise Q at 300 K and 4 K → run **F vs Q at fixed power**, interleaving the pillbox null and all reversal tests each session → (conditional) coat/swap to Nb₃Sn for the high-Q rung.
- **Acceptance:** a detection requires a statistically significant F ∝ Q slope AND a flat pillbox null AND survival of every reversal; anything less is reported as a bound.

## 5. Feasibility, risk & resources
- **Signal vs environment (computed).** Target signal ~6–24 µN (copper→cryo-copper, 10 W). After the full mitigation stack the residual artifact floor is ~0.3–3 µN, giving SNR ~2–22 (copper, marginal) to ~8–80 (cryo-copper, confident). **Q is the only clean lever** (power and size are not); this motivates the cryogenic design.
- **Cost/scale.** Detection rig ~$75–170k (calibration + cryostat dominate); Nb₃Sn upgrade +$40–100k via SRF collaboration. **Matches an equipped precision-measurement / SRF group** — not a garage build.
- **Primary risks + mitigations:** cryocooler vibration (negative-stiffness isolation, soft cold link); thermal drift (constant-power lock-in + fibre thermometry + dummy-heater nulls); EM feed-force (coaxial routing + polarity reversal). Each maps to a subsystem in the package.

## 6. Indicative timeline (3.5–4 yr)
| Year | Milestone |
|---|---|
| 1 | Literature + apparatus design; build/commission the torsion balance + RF chain; lifter known-answer validation |
| 2 | Room-temperature copper campaign; artifact-budget verification; first F(Q) points + methods paper on the discriminator stack |
| 3 | Cryostat integration; cryo-copper Q-ladder; full reversal matrix; bound or candidate signal |
| 4 | (Conditional) Nb₃Sn high-Q rung via SRF collaboration; final analysis; thesis + results paper |

## 7. Expected outcomes & significance
- **Most likely:** the tightest published bound on anomalous resonant-cavity thrust, plus a **reusable Q-scaling + orthogonal-discriminator methodology** for the whole breakthrough-propulsion metrology field. Publishable and citable independent of sign.
- **Improbable but transformative:** a Q-scaling force surviving every discriminator — which would itself demand extraordinary independent replication.
- **Transferable skills/IP:** precision force metrology, SRF cavity operation, cryogenic systems, lock-in/blind-analysis methodology — valuable to gravitational-wave, electric-propulsion, and metrology programmes.

## 8. Honesty & scientific ethics
The prior probability, given the Dresden nulls and momentum conservation, is strongly against a positive result; the proposal is written to **deliver a credible answer either way** and to *disprove* a signal as readily as confirm it. All causal claims are held as falsifiable hypotheses; no result is reported as established without surviving the full discriminator stack and independent scrutiny.

---
### Key references
- Tajmar et al., *The SpaceDrive Project — thrust-balance development and new EmDrive/Mach-Effect measurements*, Acta Astronautica (2018) + follow-ups (null results, ~5 nN floor).
- Bahder & Fazi, *Force on an Asymmetric Capacitor*, US Army Research Laboratory (2001).
- McCulloch, *Testing quantised inertia on the emdrive*, EPL/arXiv:1604.03449 (F ∝ P·Q·geometry; symmetric ⇒ 0).
- Full technical basis + reproducible calculations: github.com/mmdebrahimi/horizon-drive.

*This proposal is a draft for discussion with prospective supervisors; scope/cost/timeline are to be co-refined with the host group.*
