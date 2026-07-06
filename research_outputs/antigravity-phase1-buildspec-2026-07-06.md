# Phase-1 Turnkey Build Spec: The Cheap Decisive Test (Room-Temperature Copper)

**Compiled 2026-07-06 · Soraya (--until-mvp) · the buildable front end of `antigravity-decisive-experiment-design-2026-07-06.md`**

> **Why this is the move.** The full decisive experiment escalates copper → Nb 4 K → Nb 2 K. But **Phase 1 needs no cryogenics at all** — a room-temperature copper cavity on a bench torsion balance. It predicts a **12 µN** thrust (if the effect is real at the Eagleworks scale) that a bench balance resolves with **~7,900× margin**, and it applies **8 of the 9 null tests**. So Phase 1 alone *replicates-or-refutes the Eagleworks claim with far better systematics control than Eagleworks had* — the highest-value, lowest-cost, lowest-hazard step, and the one an ordinary optics/RF lab can build. The only discriminator it can't run is the master Q-scaling curve (that needs the cryogenic phases). All numbers below are grounded in `phase1_balance_sizing.py` (run it).

---

## 1. What you're building and what it decides

A **torsion-balance thrust stand** in vacuum carrying a **resonant copper cavity**, fed ~10 W CW, with the thrust read out interferometrically and the signal pulled out of drift by **AC modulation + lock-in**. Outcome:

- **Signal seen, passes the null suite →** escalate to Phase 2 (add cryostat) for the Q-scaling clincher.
- **Clean null to the floor →** the Eagleworks-scale tapered-cavity thrust is refuted with a proper null suite. (Honest scope: a Phase-1 null does not by itself kill *high-Q* QI — that needs Phases 2–3 — but it closes the "someone should just replicate Eagleworks cleanly" question, which is worth a paper.)

**Verified sizing (from `phase1_balance_sizing.py`):**

| Quantity | Value |
|---|---|
| Predicted QI signal (Q=5×10⁴, P=10 W) | **12.0 µN** |
| Photon-recoil floor (P/c) | 33 nN |
| Torsion fibre | tungsten, **Ø0.90 mm × 300 mm** |
| Stiffness κ / inertia I / period | 3.4×10⁻² N·m/rad / 0.135 kg·m² / **12.5 s** |
| Deflection @ 12 µN | 0.053 mrad → **7.9 µm** at the arm tip |
| Deflection @ 33 nN floor | 0.15 µrad → 22 nm |
| Interferometer resolution | ~1 nm → **signal margin ~7,900×** |
| Modulation f_mod | 0.02 Hz (below the 0.08 Hz resonance → quasi-static) |

The takeaway the sizing proves: **Phase 1 is systematics-limited, not sensitivity-limited.** The balance is easy; the null tests are the real work.

---

## 2. Bill of materials

**A. Torsion balance**
- Tungsten torsion fibre, **Ø0.90 mm, 300 mm** (annealed W wire; clamp both ends in collets).
- Beam: carbon-fibre or Zerodur rod, ~0.30 m, low-CTE. Cavity mount at **+15 cm**, matched counterweight at **−15 cm**.
- Top clamp on an x-y-tilt leveling stage; a fine rotation stage under the whole balance (for the T8 180° test).
- Optional eddy-current damper (a copper vane in a magnet gap) to tame the 12.5 s mode — but keep any magnet **off** during physics runs.

**B. Readout**
- Fibre-coupled homodyne/Michelson **interferometer** (or a commercial sub-nm fibre displacement sensor) aimed at the arm tip.
- Autocollimator as a coarse angular backup.

**C. Vacuum**
- Bell jar / small chamber + **turbomolecular pump + backing pump → < 1×10⁻⁶ torr** (kills air convection and radiometric-through-gas — the dominant Eagleworks-era artifact). Ion gauge.
- Pump on flexible bellows, mechanically decoupled from the balance table.

**D. Copper cavity set (OFHC copper, polished bore, low-GHz TM mode ≈ 2–3 GHz)**
| Cavity | Geometry | Purpose |
|---|---|---|
| A frustum | big Ø160 / small Ø90 / L120 mm | device under test |
| B cylinder | matched volume & Q | symmetric null (T5) |
| C knife-edge | frustum with L = 90 mm (= small Ø) | McCulloch signature (T6, optional) |
| D | A in a flip fixture | geometry reversal (T4) |

Each cavity: adjustable coupling loop/antenna + **piezo or stepper tuner** + field-pickup probe.

**E. RF chain** (amplifier sits **off** the balance; only a thin low-thermal-conductance coax crosses to the cavity)
- Low-GHz signal generator (phase-lockable) → **10–15 W GaN amplifier** → directional coupler (fwd/refl monitor) → **circulator + matched dump load** (routes reflected power to a *fixed* sink so on/off-resonance dumped power is equal) → cavity.
- Manual tuner or an LLRF loop to hold resonance; field probe → RF detector.

**F. Modulation + DAQ**
- RF switch (or a detune command) driven by a **0.02 Hz square wave**.
- Data logger ≥ 10 Hz: interferometer, fwd/refl power, 3–4 thermocouples/RTDs (cavity, coax, chamber, table).
- Lock-in (software or hardware) referenced to f_mod.

**G. Shielding / environment**
- **Mu-metal** shield around the balance; twisted/shielded signal leads.
- Vibration-isolated optical table.
- Radiation shields / thermal enclosure between the cavity and the readout optics.

**H. Calibration**
- **Electrostatic comb/plate actuator** on the beam (known force vs applied voltage).
- Calibrated laser + mirror on the arm for a **photon-pressure** cross-check (F = 2P/c).

---

## 3. Assembly & commissioning sequence

1. **Assemble + level** the balance in air; measure the free resonant period → confirm it's ~**12.5 s** (verifies κ and I match the sizing).
2. **Calibrate** the readout (nm/count) and the force scale (electrostatic actuator; photon-pressure cross-check). The two force calibrations **must agree to ≤ 2 %**.
3. **Fabricate + bench-tune** each copper cavity; measure Q (expect ~5×10⁴); record the resonant frequency + tuner range.
4. **Mount cavity A** + counterweight; re-balance; route the thin coax; with **RF off**, confirm zero static torque (no offset from the coax).
5. **Pump down** to < 1×10⁻⁶ torr; characterize the balance **noise floor** (target ≤ 1×10⁻⁸ N/√Hz) and the 1/f drift.
6. **Baseline the systematics with the DUMMY LOAD (T7):** feed the same 10 W into a resistive load at the cavity's location (no resonance) → measure the residual thermal/EM offset. *This is the number every candidate thrust is compared against.*
7. **Run the modulated measurement:** resonance on/off at 0.02 Hz, reflected power to the dump so dumped power is equal on/off; lock-in demodulate; **blind** the on/off labels.
8. **Run the null suite** (§4).
9. **Unblind; apply the go/no-go** (§5).

---

## 4. Null tests that apply at Phase 1 (8 of 9)

Reference the full matrix in the design doc §5. At room-temperature single-Q, these run:

| Test | What you do | Real-thrust signature |
|---|---|---|
| **T2 Power-scaling** | sweep P = 1–15 W at fixed Q | F ∝ P (linear) |
| **T3 Resonance on/off** | detune at equal dumped power | thrust vanishes off-resonance |
| **T4 Geometry reversal** | swap A ↔ D (flipped) | thrust flips sign |
| **T5 Symmetric null** | cavity B (cylinder) | thrust → 0 |
| **T6 Knife-edge** *(opt.)* | cavity C | thrust reverses |
| **T7 Dummy-load** | resistive load, same P | thrust = 0 (this is the baseline) |
| **T8 180° rotation** | rotate the whole balance | thrust rotates with the cavity |
| **T9 Current-reversal** | reverse DC bias/control sense | unchanged (flips a magnetic artifact) |

**Not at Phase 1:** **T1 Q-scaling** — the master discriminator — needs the cryogenic Phases 2–3 (you can't get Q from 10⁴ to 10¹⁰ at room temperature). Phase 1 gives one Q point plus these eight discriminators, which is already enough to cleanly separate a 12 µN thrust from systematics and to replicate/refute Eagleworks.

---

## 5. Go / no-go (Phase 1)

A **candidate thrust** requires **all** of:
- ≥ **5σ above the T7 dummy-load baseline**, AND
- vanishes off-resonance (T3), AND flips with geometry (T4), AND null for the cylinder (T5), AND rotates with the 180° test (T8), AND unchanged under current-reversal (T9), AND scales linearly with power (T2).

- **All pass →** provisional anomalous thrust at the Eagleworks scale. **Escalate to Phase 2** (add the cryostat) for the Q-scaling curve — the clincher.
- **Any fail →** systematic; the failing test tells you which (T7 quantifies thermal/EM directly).
- **Null to the floor →** publish the upper limit; the clean Eagleworks-replication result is itself valuable.

---

## 6. Safety, facility & cost tier

- **No cryogenics** — Phase 1's whole point. The hazardous, expensive cold chain is avoided entirely.
- **RF:** only 10–15 W at low GHz — shielded cavity, interlocked enclosure, no exposure. Modest.
- **Vacuum:** bell-jar implosion guard; standard turbo-pump practice.
- **Facility:** a modestly-equipped **optics/RF lab** — vibration-isolated table, turbo pump, interferometer, GaN amp + signal generator, DAQ, mu-metal. **No cleanroom** (copper, not SRF) and **no cryoplant**. Most university AMO/RF labs already have the bulk of this.
- **Cost tier:** the **low** tier — bench instruments + machined copper. (No dollar figure asserted here; price the BOM against your lab's existing kit — the design deliberately reuses standard equipment so the marginal cost is a few machined cavities + a fibre + a mount.)

---

## 7. Honest framing

Phase 1 is the **cheapest experiment that can move the needle**: it resolves the predicted signal with ~7,900× margin, applies eight independent discriminators, and settles the Eagleworks-replication question either way. What it *cannot* do alone is run the Q-scaling law that most powerfully separates QI from every systematic — that is the reason Phases 2–3 exist. Build this first; a clean result here (positive *or* null) is publishable and decides whether the cryogenic escalation is worth it.

---

*Appendix — reproduce the sizing:* `python research_outputs/phase1_balance_sizing.py` (fibre, stiffness, deflections, readout margin, integration times; asserts the bench balance resolves the signal and the photon floor). Signal/systematics context: `decisive_test_budget.py`; method validation: `decisive_test_sim.py`; full multi-phase design: `antigravity-decisive-experiment-design-2026-07-06.md`.
