# Taper-vs-Pillbox Fork — RESOLVED (keep the frustum)

**Date:** 2026-07-20 · **Resolves:** the Tier-0 open fork in `copper-cavity-design-review-2026-07-20.md`
**Grounding calc:** `cavity_geometry_factor_check.py` (exit 0) · **Status:** reasoned resolution (see honesty caveat)

---

## The question
The design review flagged an open fork: *is the truncated-cone taper mechanistically required, or would a cheaper, higher-Q, far-easier-to-mirror-finish cylindrical **pillbox** (Ø125 mm) do the same job?* Since a pillbox eliminates the single hardest/most-expensive fabrication step (the 120 mm deep blind tapered mirror bore), the answer materially changes the ~$2k machining decision.

## The answer: KEEP THE CONE — a pillbox is a null-by-design
The horizon-drive effect is calibrated to the Eagleworks **frustum**, i.e. the EmDrive-family / **quantised-inertia (QI/MiHsC)** mechanism. In that theory the thrust law is:

> **F = (P·Q·L/c) × (1/D_small − 1/D_big)**

The bracket is the **geometry factor**. Its physical meaning (QI): the metal walls act as an event horizon for Unruh radiation whose wavelengths must *fit* inside the cavity; **more waves fit at the wide end than the narrow end**, so photons there carry more inertial mass, and momentum conservation drives the cavity toward the narrow end. The **asymmetry breaks the Unruh-wavelength-cutoff symmetry** — it *is* the mechanism.

**Computed for HD-CU-CAV-001** (`cavity_geometry_factor_check.py`):
| Geometry | 1/D_s − 1/D_b | Geometry factor G = L·(…) | Thrust |
|---|---|---|---|
| **Frustum** (Ø90→Ø160, L=120) | 4.861 /m | **0.583** | allowed (nonzero) |
| **Pillbox** (D_s = D_b) | 0.000 /m | **0.000 (exact)** | **zero by construction** |

A symmetric cavity produces **exactly zero** thrust in this theory. So a pillbox would be higher-Q and trivially machined — and would **measure nothing**. It is not a valid substitute for the thrust article.

## The bonus: the pillbox becomes the ideal NULL-CONTROL
This resolution hands you a free, high-value control experiment. Build a **pillbox of the same material, finish, and drive** as the frustum:
- **QI predicts it reads exactly zero.** So does every mundane hypothesis.
- Therefore **any nonzero pillbox reading is a systematic** — thermal, ionic-wind, EM-feedthrough, or balance artifact — the exact false-positives that discredited earlier EmDrive claims.
- Run the **frustum vs the pillbox** back-to-back: a signal that appears in the frustum **and is absent in the pillbox** is the discriminating result; a signal in **both** is an artifact. This is a stronger control than on/off-resonance alone, and the pillbox is cheap + easy to make (unlike the frustum).

→ **Fabricate the frustum as the thrust article; fabricate a pillbox as the null-control.** The pillbox's easy machinability, which tempted us to replace the cone, instead makes it a cheap control.

## Honesty caveat (falsification rail — this is a reasoned resolution, not proof)
- **No cheap kill-test exists** for a theory-interpretation question, so this is published as a **reasoned assessment**, not established fact.
- **Two thrust laws, one shared property:** QI's absolute magnitude (F = PQL/c·ΔG) differs from the horizon-drive's calibrated F = η·P·Q/c (η fit to Eagleworks' *measured* 1.2 mN/kW) by ~1–2 orders. We rely **only on the geometry dependence both share** — symmetric ⇒ zero — **not** on either absolute number.
- **The effect itself is unconfirmed:** QI is a fringe theory conflicting with Newton's 3rd law / SR / GR / Noether; the most sensitive tests (Tajmar) found **no thrust to the nN floor**, limiting any effect ≥4 orders below the lab-scale prediction. This memo answers *"which geometry **if** the effect is real,"* not *"the effect is real."*

## Net
The taper is load-bearing, not a fabrication burden — **keep it.** Add a symmetric **pillbox null-control** (cheap, easy) to the build so the decisive test is frustum-vs-pillbox, not just on-vs-off resonance. This closes the last open design fork before machining.

### Sources
- McCulloch, *Testing quantised inertia on the emdrive*, EPL/arXiv 1604.03449 (thrust law F = PQL/c·(1/w_s − 1/w_b), symmetric ⇒ 0)
- McCulloch, *Testing quantised inertia on emdrives with dielectrics*, EPL 118 34003
- Tajmar et al. — high-precision null tests (nN floor); *Struggle* limits ≥4 orders below prediction
- Geometry factor computed in `cavity_geometry_factor_check.py`
