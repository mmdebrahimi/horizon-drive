# Copper Resonant Cavity — Design-Review & Optimizations

**Date:** 2026-07-20 · **Subject:** HD-CU-CAV-001 (room-temperature test article)
**Grounding calcs (both exit 0):** `cavity_design_review_calcs.py`, `cavity_material_comparison.py`
**Companions:** `copper-cavity-machinist-spec-2026-07-15.md`, `antigravity-cavity-chamber-deep-dive-2026-07-06.md`

> Purpose: capture the optimization pass on the cavity + measurement chain, before committing ~$2k to machining. Every number here is recomputed by the two scripts; this memo is the interpretation.

---

## The load-bearing numbers (recomputed, not asserted)

| Quantity | Value | Source |
|---|---|---|
| Operating frequency (TM010) | 1.836 GHz (λ = 163 mm) | design |
| Copper skin depth @ 1.836 GHz | **1.54 µm** | `cavity_design_review_calcs.py` |
| Surface finish → Q (Hammerstad) | Ra 0.4 µm → **Q≈25,100** · 0.8 µm → **21,150** · 1.6 µm → **16,000 (FAILS gate)** | idem |
| Bare-aluminium cavity Q | **~21,000** (just clears the 20k gate) | idem |
| Cu electroplate ≥ 15 µm = 9.7 skin depths | ≈ solid-copper Q | idem |
| λ/4 choke-joint groove depth | **40.8 mm** | idem |
| TM010 pillbox equivalent diameter | **125 mm** (if the taper is not required) | idem |
| Material ladder (Q) | Cu **2.7×10⁴** → cryo-Cu ~10⁶ → **Nb/Nb₃Sn ~10¹⁰** | `cavity_material_comparison.py` |

**Finish is genuinely load-bearing:** ≤ 0.8 µm is mandatory to clear Q ≥ 20,000; "as-machined" 1.6–3.2 µm fails. This validates the machinist spec's Ra ≤ 0.4 µm insistence.

---

## Optimizations — ranked by impact

### Tier 0 — the strategic fork (design-authority call, NOT mine)
**Is the truncated-cone taper mechanistically required?**
- If the effect is a **McCulloch-QI / EmDrive-family** mechanism, the frustum *asymmetry is the mechanism* → **keep the cone.**
- If it's a **shape-agnostic scalar inertia-modifier** (F = η·P·Q/c), the cone buys nothing → a **cylindrical pillbox (Ø125 mm)** is higher-Q and *trivially* mirror-finished (a straight bore laps; a 120 mm blind cone is the hardest possible finish).
- **Read:** the effect is calibrated to the Eagleworks *frustum*, so the taper is probably load-bearing — but confirm before machining, because a pillbox eliminates the single hardest fabrication step.

### Tier 1 — fabrication (attacks the cost driver)
The RF field only penetrates **1.54 µm**; the bulk metal is irrelevant to Q. Two consequences:
1. **Electroform on a polished mandrel instead of machining solid OFHC.** Diamond-turn/polish the *outside* of an aluminium mandrel (convex, easy to mirror-finish), electroform 200–500 µm of copper, dissolve the mandrel → the inner RF surface is a perfect mirror negative. **Eliminates the "polish a 120 mm deep blind tapered bore" problem** — exactly the feature the online quoter flagged as most expensive. **Strongest single recommendation.**
2. **Or: bright-copper-plated aluminium.** Machine a cheap Al cone, bright-plate ≥ 15 µm (= 9.7 skin depths, Q ≈ solid Cu). Bright/leveling plating reaches near-mirror *without* mechanical polishing.

### Tier 2 — EM refinements (raise + stabilize Q)
3. **λ/4 choke joint at the mouth seam (40.8 mm groove).** Wall current crosses the body↔cap seam; seam resistance caps Q *and* makes Q depend on gasket pressure (run-to-run scatter that mimics signal drift). A choke groove presents ~0 Ω without metal-to-metal contact → higher, **reproducible** Q, and it relaxes the flange-flatness spec (cheaper machining).
4. **Reconsider the on-axis threaded tuner.** On-axis sits at the TM010 E-field antinode; a threaded gap there is an RF discontinuity = loss + spurious modes, capping the Q you're trying to measure. Prefer a smooth bellows-sealed plunger or a side-wall tuner at a lower-field point.
5. **Mode-chart before trusting any Q.** A frustum has a dense spectrum; confirm the target mode is isolated (no near-degenerate mode within a few linewidths) or the Q-scaling discriminator is corrupted.

### Tier 3 — the measurement chain (where experiments like this actually die)
6. **Vary Q at FIXED DISSIPATED POWER, not fixed input power.** The discriminator is F ∝ Q while thermal systematics ∝ P_dissipated. Change Q at fixed *input* power and dissipated power moves with it → confounded. Hold P_dissipated constant (trim the drive) and vary Q → F ∝ Q is cleanly isolated. Subtle and essential.
7. **PLL-lock the drive to the cavity.** Copper CTE ≈ 17 ppm/°C: a few °C of RF heating detunes the cavity → stored energy drifts → looks like thrust. A phase-locked loop tracking the resonance holds stored energy constant — removes the #1 artifact better than chasing the tuner by hand.
8. **Prototype the whole rig with a cheap cavity first.** Bare-Al Q ≈ 21,000 just clears the gate — good enough to shake down vacuum + RF + balance + lock-in before buying the mirror-copper article. De-risks the ~$2k spend. *(See also the Biefeld–Brown lifter as an even cheaper known-answer calibration article: `biefeld-brown-replication-assessment-2026-07-20.md`.)*

---

## Material efficiency — "is anything better than copper?" (price ignored)

- **Room temperature:** copper is already optimal. Silver buys only **~4% Q**; gold and everything else are *worse* (`cavity_material_comparison.py`). Room temp is a hard ceiling at Q ≈ 27,000.
- **To dramatically win you must leave the normal-metal regime** — surface resistance drops from milli-ohms to nano-ohms (~10⁶×):
  - **Niobium @ 2 K** → Q ~10¹⁰–10¹¹ (the SRF-accelerator standard; the Q the propulsion claim needs).
  - **Nb₃Sn @ 4.2 K** → same Q, but ordinary liquid helium instead of superfluid (~10× less cryo complexity). **Best target for a Q-only test.**
- **Avoid the high-Tc trap:** YBCO at 77 K has milli-ohm GHz surface resistance (~1000× worse than Nb) — great for filters, useless for a high-Q cavity.
- **The reframe:** the material ladder (Cu 2.7×10⁴ → cryo-Cu ~10⁶ → Nb ~10¹⁰) **is the Q-axis of the decisive experiment.** The real cliff is the cryogenics, not the metal.

---

## Net recommendation
Highest-leverage moves before machining: **(1) electroform/plate instead of machining solid copper** (dissolves the cost driver), **(2) λ/4 choke joint** (reproducible Q), **(3) fixed-dissipated-power Q-scaling + PLL lock** (so the measurement can't be faked by thermal drift). **Prototype in aluminium (or a Biefeld–Brown lifter) first** to validate the apparatus. Confirm the **taper-vs-pillbox** question (Tier 0) with the effect's theory before committing geometry.

*All numbers reproduced by `cavity_design_review_calcs.py` + `cavity_material_comparison.py` (both exit 0, wired into `verify_all.py`). This is the room-temperature test article; propulsion-grade Q needs the niobium/cryo path (a separate specialist build).*
