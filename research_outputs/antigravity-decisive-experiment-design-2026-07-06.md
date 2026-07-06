# The Decisive Experiment: Proving (or Killing) the Tapered-Cavity Inertia Effect

**Compiled 2026-07-06 · Soraya (decompose + --plan) · supersedes/extends `antigravity-decisive-test-design-spec-2026-07-04.md`**

> **What this is.** A complete, build-ready experimental design whose *only* purpose is to settle — to publishable, referee-proof standard — whether a tapered superconducting RF cavity produces anomalous axial thrust, as quantised inertia (QI) and the EmDrive claims predict via `F = η·P·Q/c`. It is engineered to be **decisive in both directions**: a clean null to the stated floor *falsifies the linear-Q thrust claim by up to seven orders of magnitude*; a positive result that survives the full discriminator suite is a genuine new-physics discovery. Numbers here are computed in `decisive_test_budget.py` (run it), not asserted.

---

## 0. The one idea the whole experiment is built on

Every previous attempt (Eagleworks positive, Dresden/Tajmar null) drowned in **systematics** — thermal expansion, air currents, magnetic interaction of feed currents with Earth's field, centre-of-mass drift. Sensitivity was never the problem. So this design does not chase sensitivity. It chases a **discriminator that no systematic can fake**:

> **Hold input power `P` fixed. Sweep cavity quality factor `Q` across 10⁴ → 10¹⁰. The QI law predicts thrust `F ∝ Q` — a 10⁶× rise. Every known false positive scales with *dissipated power ≈ P* and is therefore FLAT in Q.**

At steady state a critically-coupled cavity dissipates *all* its input power as wall heat **regardless of Q**, so thermal, radiometric, magnetic, and feed-line artifacts are all pinned to `P` and do not move as `Q` climbs. A real QI thrust rides a straight line of slope +1 in log(F) vs log(Q); a systematic is a flat line. **That separation is the experiment.**

---

## 1. F1 — The claim and its falsifiable predictions

**Primary hypothesis (H1).** A tapered (frustum) resonant cavity of quality factor `Q`, fed CW power `P`, produces a steady axial force `F = η·P·Q/c` directed toward the narrow end, with `η ≈ 0.0072` (calibrated so the formula reproduces the Eagleworks claim of 1.2 mN/kW at Q ≈ 5×10⁴).

**The six discriminating predictions** — each one separates H1 from the systematics that mimic a thrust:

| # | Prediction | If TRUE (QI) | If systematic | Discriminates against |
|---|---|---|---|---|
| P1 | **Q-scaling:** F ∝ Q at fixed P | slope +1 over 6 decades | flat (∝P) | thermal, magnetic, feed — *all of them* |
| P2 | **Power-scaling:** F ∝ P at fixed Q | slope +1 | thermal also ∝P (degenerate) | balance nonlinearity only |
| P3 | **Geometry reversal:** flip cavity end-for-end | thrust sign flips | unchanged (lab-fixed) | drafts, ambient-field, tilt |
| P4 | **Symmetric-cavity null:** cylinder, same Q & P | F → 0 | thrust persists | anything not geometry-dependent |
| P5 | **Resonance dependence:** detune off-resonance at same delivered/dumped power | F → 0 (needs stored field) | unchanged (same heat) | thermal, radiometric |
| P6 | **McCulloch knife-edge:** axial length = small-end diameter | thrust *reverses* (QI-specific) | no special behaviour | confirms the *mechanism*, not just "a force" |

P1 and P5 are the killers. P6 is the signature that would distinguish *McCulloch's QI specifically* from a generic anomalous thrust.

---

## 2. Verified signal / systematics / noise budget

Computed in `decisive_test_budget.py` at **P = 10 W CW** (chosen to keep cryogenic heat load modest while making the signal enormous):

| Phase | Cavity / temp | Q | Predicted F (QI) | × photon floor | × thermal floor | Integration @ SNR 5 |
|---|---|---|---|---|---|---|
| **1** | Copper, 300 K | 5×10⁴ | **12 µN** | 360× | 180× | 17 µs |
| **2** | Niobium, 4 K | 1×10⁸ | **24 mN** | 7.2×10⁵× | — | ~ps (trivial) |
| **3** | Nb 2 K / Nb₃Sn 4 K | 1×10¹⁰ | **2.4 N** | 7.2×10⁷× | 3.6×10⁷× | ~fs (trivial) |

Fixed floors (flat in Q): **photon-recoil `P/c` = 33 nN**; **thermal radiometric ≈ 67 nN**; balance force-noise ≈ 1×10⁻⁸ N/√Hz.

**What the budget proves:**
1. **Sensitivity is not the limiting factor.** Even the 33 nN photon floor resolves at SNR 5 in **2.2 s**; the QI signals are µN-to-Newton and resolve essentially instantly. The experiment is **100 % systematics-limited** — which is exactly why the design below is a *null-test suite*, not a sensitivity chase.
2. **Even Phase 1 is decisive.** Cheap room-temperature copper already predicts **12 µN — 180× the thermal floor** — so Phase 1 alone replicates-or-refutes Eagleworks with far better systematic control than Eagleworks had.
3. **The Q-scaling span is 2×10⁵×** across the ladder. No known systematic tracks cavity Q; a straight `F ∝ Q` line is unforgeable.
4. **Thermodynamic self-check.** A positive Phase-3 result (2.4 N at 10 W → 0.24 N/W) implies energy break-even at **4.2 m/s**. Per Higgins, that is either an artifact *or* proof the momentum is drawn from a reaction reservoir — i.e. an **inertia modifier, not a reactionless drive**. The design therefore includes a momentum-accounting test for any positive result (§7).

---

## 3. F2 — The cavity specimen set

Four cavities, fabricated to identical SRF standard so only the tested variable differs:

| Cavity | Geometry | Role |
|---|---|---|
| **A · Frustum** | truncated cone: big-end Ø 160 mm, small-end Ø 90 mm, length 120 mm | the device under test (P1–P3, P5) |
| **B · Cylinder** | right cylinder, matched volume & Q, same resonant mode | the symmetric null (P4) |
| **C · Knife-edge frustum** | axial length set = small-end diameter (90 mm) | McCulloch reversal signature (P6) |
| **D · Reversed mount** | Cavity A in a flip fixture | geometry reversal (P3) — same cavity, not a new one |

**Fabrication (bulk Nb variants):** RRR ≥ 300 niobium, ~3–4 mm wall, spun half-shells electron-beam-welded in vacuum; then the full SRF surface ritual — buffered chemical polish (~150 µm), 600–800 °C hydrogen-degas bake, light electropolish, high-pressure ultrapure-water rinse in a cleanroom, clean assembly. Each cavity carries an adjustable power coupler, a **piezo tuner** (mandatory — off-resonance = zero field = zero signal), and two field probes. A **copper twin of A** (identical geometry) is made for Phase 1.

**Q characterization (gate before any thrust run):** measure `Q₀(T)` for every cavity by the standard decay/bandwidth method at each operating temperature; **freeze the measured Q** as the abscissa of the Q-scaling plot. A cavity whose Q is not reproducible to ±10 % is rejected. Target/expected: copper 5×10⁴ (300 K), Nb 10⁸ (4 K), Nb 10¹⁰ (2 K) or Nb₃Sn 10¹⁰ (4.4 K).

---

## 4. F3 — Thrust metrology

**Instrument:** a **torsion balance** — the gold standard for DC sub-µN thrust — not a beam balance (torsion rejects vertical thermal-expansion drift). Cavity mounted at radius `r ≈ 0.3 m` on a low-thermal-expansion (carbon-fibre / Zerodur) arm suspended by a thin torsion fibre (tungsten or a cross-flexure pivot).

- **Readout:** homodyne/Michelson **laser interferometer** on the arm tip (or a fibre-optic displacement sensor), sub-nm resolution → force noise ≈ 1×10⁻⁸ N/√Hz in the 0.01–0.1 Hz band. A capacitive pickoff is the cryogenic-compatible backup.
- **In-situ calibration (two independent methods, must agree):** (a) an **electrostatic comb/plate actuator** delivering NIST-traceable known forces across the µN range; (b) a **calibrated photon-pressure source** — a laser of known power reflected off the arm gives `F = 2P_laser/c`, tying the force scale to first principles. Calibrate before *and* after every run; drift > 2 % voids the run.
- **The cryogenic force-decoupling problem (the hardest single engineering item):** for Phases 2–3 the cavity must be at 4 K / 2 K on a *moving* balance arm. Cool it through **flexible thermal straps** (braided OFHC copper / high-purity Al) whose parasitic stiffness and thermally-driven creep are the dominant balance systematic. Mitigations: (i) route straps along the torsion axis so their force arm ≈ 0; (ii) characterize the strap force-vs-temperature transfer function on a dummy mass and subtract it; (iii) run the cryocooler compressor **off-balance** with vibration-isolated, force-decoupled transfer lines; (iv) as a cross-check, a **conduction-cooled cold-finger on the fixed frame** with the cavity radiatively/weakly coupled. This item gets a dedicated commissioning campaign before any physics run.

---

## 5. F4 — The null-test matrix (the heart of the experiment)

Each row is a control whose *QI response* and *systematic response* differ. A claimed thrust must pass **all** of them.

| Test | Procedure | QI predicts | Systematic predicts | Kills |
|---|---|---|---|---|
| **T1 Q-scaling** | Cavity A, fixed P = 10 W, run at Q = 5×10⁴ / 10⁸ / 10¹⁰ | F ∝ Q (slope +1) | flat | the master test |
| **T2 Power-scaling** | Cavity A, fixed Q, sweep P = 1–20 W | F ∝ P | thermal also ∝P | balance nonlinearity |
| **T3 Resonance on/off** | Detune ±several bandwidths at **equal delivered+dumped power** (reflected power sent to a fixed matched load so wall+load heat is unchanged) | F → 0 off-resonance | unchanged | thermal / radiometric |
| **T4 Geometry reversal** | Swap Cavity A ↔ D (flipped) | sign flips | unchanged | lab-fixed drafts, tilt, ambient field |
| **T5 Symmetric null** | Cavity B (cylinder), same Q & P | F = 0 | thrust persists | any non-geometry artifact |
| **T6 Knife-edge** | Cavity C (L = small-Ø) | thrust reverses | nothing special | confirms QI *mechanism* |
| **T7 Dummy-load** | Replace cavity with a resistive load dissipating the same P at the same location | F = 0 | thermal/EM reproduced | isolates & measures thermal+EM baseline |
| **T8 180° rotation** | Rotate whole balance 180° about vertical | thrust rotates with cavity | lab-fixed artifact does not | drafts, ambient field, floor tilt |
| **T9 Current-reversal** | Reverse any DC bias/control-current sense | unchanged | Lorentz artifact flips | magnetic interaction |

**Environment (kills the classic false positives):**
- **Vacuum < 10⁻⁶ torr** — eliminates air convection and radiometric-through-gas (the dominant Eagleworks-era artifact).
- **µ-metal magnetic shield** + twisted/superconducting leads + T9 — kills feed-current × Earth-field Lorentz forces.
- **Seismic isolation** (passive stack + active for the cryocooler) + AC modulation (§6) — kills vibration/microphonics.
- **Thermal:** all input power routed to a *fixed-frame* heat sink where possible; radiation shields between cavity and readout; the T7 dummy-load quantifies the residual thermal recoil directly.

---

## 6. F5 — Data acquisition, modulation, blinding, statistics

- **AC modulation + lock-in (non-negotiable):** never measure a DC thrust. Modulate the discriminating variable — **resonance on/off** (T3) or RF power — as a square wave at `f_mod ≈ 0.01–0.1 Hz` and synchronously demodulate the balance signal at `f_mod`. This rejects 1/f drift (thermal expansion, outgassing CoM creep), which is the enemy that faked every historical result.
- **Blind analysis:** the on/off (or high-Q/low-Q) labels are hidden from the analyst by a coded key; the predicted sign and magnitude are **pre-registered** before unblinding (Tajmar-grade rigour). Prevents the experimenter-expectation bias that produced the Eagleworks positive.
- **Statistics & integration:** balance noise gives SNR 5 on the photon floor in 2.2 s (§2), so integration time is never the constraint; runs are instead sized to beat *drift and systematic reproducibility*, typically many modulation cycles (hours) per point for a tight limit.
- **Detection definition (go/no-go):** a signal counts as a *candidate thrust* only if it is **≥ 5σ above the T7 dummy-load + T5 symmetric-null baseline** AND passes the discriminator gauntlet below.

**Decision tree:**
```
Signal ≥ 5σ over baseline?  ── no ──▶  NULL. Report upper limit η(Q). Linear-Q claim
        │ yes                          falsified down to the achieved floor (see §8).
        ▼
Q-scaling slope = +1 (T1)? ── no ──▶  SYSTEMATIC (flat/other slope). Diagnose via T7.
        │ yes
Vanishes off-resonance (T3)
 AND symmetric null (T5)
 AND flips with geometry (T4)
 AND rotates 180° (T8)?     ── no ──▶  SYSTEMATIC. Not thrust.
        │ yes (ALL pass)
        ▼
   ANOMALOUS THRUST CONFIRMED  ─▶  proceed to §7 momentum accounting +
   independent-lab replication before any claim.
```

---

## 7. Protocol for a positive result (the part everyone forgets)

If a thrust passes §6, it is *extraordinary* and one more question is mandatory before any "anti-gravity" claim: **is it reactionless, or an inertia modifier?** The thermodynamic self-check (§2) says a reactionless 2.4 N at 10 W is perpetual motion, so a *real* effect must be exchanging momentum with something.

- **Momentum accounting:** instrument the surroundings — measure recoil on the vacuum chamber / a nearby witness mass / the RF ground return — for the missing momentum. A genuine inertia modifier changes the effective inertia of a reaction mass that *is* pushed conventionally; look for that reaction.
- **Energy accounting:** measure electrical input vs mechanical output vs waste heat to full closure; a violation is either an artifact or a Nobel.
- **Independent replication:** hand the frozen protocol + a specimen to ≥ 2 independent labs *before* publication. This is the step that both Eagleworks (skipped) and cold fusion (skipped) needed.

---

## 8. F6 — Facility, safety, and the escalation ladder

**Build the cheap decisive test first.** The three phases are a cost/risk ladder, and Phase 1 is already publishable:

1. **Phase 1 — copper, 300 K (weeks, bench-scale, low cost).** Torsion balance + copper frustum/cylinder + 10 W amp + turbo-pumped vacuum + µ-metal. Predicts 12 µN (180× thermal). **This alone decisively replicates-or-refutes Eagleworks with a proper null suite** — the highest-value, lowest-cost step. Do not proceed until Phase 1's systematics are closed.
2. **Phase 2 — Nb, 4 K (months, cryostat added).** Same balance, now with the force-decoupled cryogenic mount (§4). Predicts 24 mN. First test of the *Q-scaling line* (Phase 1 → Phase 2 spans 2000× in Q).
3. **Phase 3 — Nb 2 K or Nb₃Sn 4.4 K (the definitive point).** Predicts 2.4 N. Completes the Q-scaling curve over 2×10⁵× and reaches the regime where a positive result would be unmissable and a null would bury the linear-Q claim.

**Safety:** RF interlocks + shielding; SRF **quench** protection (a cell going normal dumps stored EM energy as heat — detect via reflected-power/temperature, trip in ms); cryogenic O₂-displacement/asphyxiation monitoring, over-pressure relief, cold-burn PPE; vacuum implosion protection. No high voltage exposed; no crewed anything (it's a bench experiment).

---

## 9. Honest framing — what each outcome means

- **Clean null across all three phases** (the *likely* outcome, given Dresden/Tajmar): the linear-Q tapered-cavity thrust claim is **falsified to η(Q) upper limits far below the prediction** — the single most valuable result the field could have, because it closes the "someone just hasn't run a clean high-Q version" loophole that keeps the dream alive. Publish the limit curve.
- **A signal that fails any discriminator:** a *systematic*, diagnosed and quantified (T7 tells you which one). Still a useful methods paper.
- **A signal that passes everything and replicates:** genuine new physics — then §7 decides whether it's an inertia modifier (the only thermodynamically-survivable reading) worth the entire engineering programme in the companion articles.

This experiment cannot make the effect real. It can only make the answer **unambiguous** — which, after decades of ambiguous EmDrive claims, is the whole point.

---

*Appendix — reproduce the numbers:* `python research_outputs/decisive_test_budget.py` (η calibration, per-phase F_QI, photon/thermal floors, integration times, Q-scaling span, thermodynamic break-even). All figures in §2 come from it; the script's assertions are the checkable bar for this design (all phases clear thermal ≥10×; Q-scaling span ≥10⁴×).*
