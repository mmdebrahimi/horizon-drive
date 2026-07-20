# Subsystem Optimization Memo — Calibration / Force Traceability

**Project:** Horizon-drive Phase-1 decisive experiment (detect-or-null ~12 µN anomalous thrust)
**Subsystem:** Calibration / force traceability (deflection → newtons)
**Date:** 2026-07-20
**Optimize for:** measurement quality; prices noted

---

## Overview

The horizon-drive only produces a *deflection* (~8 µm arm displacement for a claimed 12 µN). A result — detection **or** null — is only credible if that deflection is converted to newtons through a **traceable, redundant** calibration. A single calibration method is not defensible: any single actuator can carry an uncharacterized systematic (charge leakage, gap error, thermal creep, laser mispointing) that biases the newtons-per-micron scale factor and cannot be caught internally.

This memo specifies **two independent absolute force references** plus **continuous in-situ calibration**:

1. **Electrostatic actuator** — a fringing-field / comb capacitor applying a known force `F = ½·V²·(dC/dx)`. Voltage traceable to a Josephson-referenced DMM; capacitance gradient measured with a traceable LCR meter. This is the workhorse: it spans the full 0.2–30 µN band that brackets the 12 µN claim, it is non-contact and vacuum-compatible, and its `V²` law lets you sweep force cleanly.
2. **Photon-pressure cross-check** — a calibrated laser reflecting off a mirror on the arm, `F = (1+R)·P/c ≈ 2P/c`. This is a **first-principles absolute** force: it depends only on measured optical power `P`, the (exact) speed of light `c`, and mirror reflectivity `R`. No mechanical or electrical actuator constant enters. It anchors the *bottom* of the force range (nN → sub-µN) with a completely orthogonal physics.
3. **In-situ continuous calibration** — the electrostatic actuator is pulsed at a frequency `f_ES` **distinct** from the RF on/off modulation `f_RF`, and (intermittently) the photon-pressure tone at a third frequency `f_PP`. Lock-in / FFT separation tracks the newtons-per-micron scale factor and its drift **live, during the run**, rather than only in a before/after bracket.

The design principle mirrors NIST's own metrology program: NIST compared an Electrostatic Force Balance against a photon-pressure reference at the ~10 nN level and demonstrated SI-traceable agreement — establishing "a link between mass, force and laser power within the SI" (Shaw et al., *Metrologia* 56 025002, 2019). We reproduce that two-reference architecture one to two decades higher in force, where SNR is far more favorable.

---

## Optimized component list (parts / prices)

### A. Electrostatic actuator (primary reference + in-situ cal tone)

| Item | Specific part | Role | ~Price (USD) |
|---|---|---|---|
| HV amplifier / source | **Trek 601C** (0 to ±1 kV, ±10 mA, DC-stable; built-in V & I monitors, DC accuracy <0.1% FS) — now Advanced Energy | Drives the actuator plates; monitor outputs feed closed-loop control | $6–9 k (quote) |
| Precision source + leakage meter | **Keithley 6487** picoammeter/voltage source (505 V source, 20 fA–20 mA, 10 fA res, 5½ digit) | Alternative low-V source; **measures actuator leakage current** to bound charge-drift systematic | $7,680 new / ~$3–4 k used |
| Capacitance-gradient metrology | Traceable LCR meter (e.g. Keysight E4980A-class) | Measures `dC/dx` vs. vane position → the traceable actuator constant | $8–15 k (or rent/borrow) |
| Actuator geometry | Custom fringing-field capacitor: a thin grounded **vane on the arm dipping between two fixed driven plates** (LISA/Cavendish-style), OR a **MEMS-style comb**. Comb preferred: force is **independent of the electrode gap** (unlike parallel-plate `F ∝ 1/d²`) | The moving element | machine-shop, ~$200–2 k |
| DVM for voltage traceability | 6½-digit DMM w/ NIST-traceable cal cert (e.g. Keysight 34465A) | Pins applied `V` to the SI volt | $2–4 k |

**Geometry sizing (parallel-plate sanity check, gap-sensitive variant):** two 10 mm × 10 mm plates, gap `d` = 2 mm, moving vane. `F = ½·ε₀·A·V²/d²`. With `A` = 1×10⁻⁴ m², `d` = 2×10⁻³ m → `F = 1.11×10⁻¹⁰·V²` N. **V ≈ 330 V gives 12 µN**; V ≈ 100 V gives ~1.1 µN. Modest, safe voltages. **But** the parallel-plate force pulls the vane and changes `d` (nonlinear, gap-critical) — so the deliverable design is the **fringing-field / comb** version where force is set by the measured `dC/dx` and is gap-insensitive. `dC/dx` is *measured*, never assumed — that is what makes it traceable.

### B. Photon-pressure cross-check (orthogonal absolute reference)

| Item | Specific part | Role | ~Price (USD) |
|---|---|---|---|
| Calibration laser | **All-fiber 1064 nm, 1–10 W, single-mode**, integrated temp control (BeamQ mrphotonics-class) — best power stability | Provides the calibrated `P` | ~$9,990 |
| Budget laser option | AeroDIODE / BWT 1064 nm 10 W fiber-coupled diode (broader 3.5 nm linewidth) + driver | Lower cost, needs external power stabilization | $995–2,990 (+ driver) |
| Traceable power meter | **Thermopile** w/ NIST-/PTB-traceable cert: Thorlabs C-series, **Gentec-EO UP19K-50W**, or **Newport 919P** (919P calibrates at 1070 nm — closest to 1064) | Pins `P` to the SI watt (→ kilogram / Planck constant); anneal to <2–3% | $1.5–4 k + ~$300/yr recal |
| High-reflectivity mirror | Dielectric HR (R > 0.999) or DBR mirror bonded to the arm; measure `R` in-situ (incident vs. reflected power) | Doubles momentum transfer; `R` enters the force directly | $100–500 |
| Beam pickoff / monitor PD | Wedge pickoff + amplified photodiode | Continuous relative-power monitor during modulation | $300–800 |
| Beam modulator | Direct laser current modulation OR AOM | Chops photon force at `f_PP` for lock-in | $0 (direct) – $3 k (AOM) |

### C. Readout (shared) — deflection sensor

| Item | Specific part | Role | ~Price (USD) |
|---|---|---|---|
| Optical-lever PSD | **Thorlabs PDP90A** lateral-effect PSD (320–1100 nm; few-nm/√Hz, beam-shape-independent) — preferred for absolute displacement; or **PDQ80A** quadrant (10–100 nm/√Hz, best in nulling regime) | Reads arm angle via optical lever | ~$1–1.5 k |
| Readout laser + lever optics | Low-power (<5 mW) 635 nm diode + long lever arm `L` | Angular amplification of the 8 µm deflection | $200–500 |
| Lock-in / DAQ | 2-channel lock-in (e.g. Zurich MFLI) or multi-channel DAQ + software lock-in | Separates `f_RF`, `f_ES`, `f_PP` tones | $2–8 k |

**Indicative subsystem total:** ~$35–55 k new; ~$15–25 k with used HV/LCR/laser and a DIY comb.

---

## The single null-test-critical optimization

> **Two independent absolute force references — electrostatic and photon-pressure — must agree to < 2 % in an overlapping force band. Agreement is the license to quote a 12 µN number; disagreement is the discovery of an uncharacterized systematic.**

Why this is *the* optimization and not just a nice-to-have:

- The two references share **no common failure mode**. The electrostatic scale factor is set by `V` and `dC/dx` (electrical + geometric). The photon-pressure scale factor is set by `P`, `c`, and `R` (optical). A charge-leakage error, a gap-metrology error, or a comb-fringe-field error moves the electrostatic newtons-per-micron **but not** the photon-pressure one, and vice-versa (laser mispointing, absorption/heating, `R` error). If both independently reproduce the same newtons-per-micron on the *same balance* to <2%, the residual space for a hidden common-mode systematic in the **thrust** measurement collapses.
- **Overlap band:** photon pressure comfortably reaches ~0.3 µN at ~45 W or, at the project-matched 10–15 W, ~65–100 nN. The electrostatic actuator is fully linear-in-`V²` from ~0.1 µN up through 30 µN. **Cross-calibrate the electrostatic actuator against photon pressure in the 0.1–0.3 µN overlap**, confirm <2% agreement, then use the electrostatic `V²` law to extrapolate cleanly up to the 12 µN operating point (extrapolation over a well-behaved analytic law, anchored by an absolute reference at the low end).
- **Precedent / feasibility:** NIST achieved ~5% agreement at ~10 nN (Shaw et al. 2019), limited by nN-level SNR and alignment repeatability. Operating **2–3 decades higher in force (0.1–12 µN)** improves SNR by the same factor, so a **<2% cross-agreement target is realistic** — *provided* the thermopile power calibration (typically 2–3% commercial) is the limiting term and is beaten down (annual NIST-traceable recal, in-situ `R` measurement, integrating-sphere capture). **Honest flag:** if the thermopile stays at 3%, the photon reference alone can't certify <2% — treat 2% as the *design goal* and quote whatever combined uncertainty the budget actually delivers.

**Acceptance test:** sweep both actuators over 0.1–0.3 µN; fit newtons-per-micron for each; require |ratio − 1| < 0.02. If it fails, do **not** report a thrust number — chase the discrepancy (leakage current via the 6487, mirror heating/absorption, PSD linearity, arm nonlinearity) until it closes.

---

## Worked F = 2P/c numbers

`F = (1+R)·P/c`; for `R ≈ 1`, `F ≈ 2P/c`. With `c = 2.998×10⁸ m/s`, the coefficient `2/c = 6.671×10⁻⁹ N/W`.

Balance sensitivity (given): 12 µN → 8 µm ⇒ **0.667 µm/µN = 0.667 nm/nN** (arm displacement, before optical-lever gain).

| Laser power `P` | Photon force `F = 2P/c` | Arm deflection (0.667 nm/nN) | Notes |
|---|---|---|---|
| 1 W | 6.67 nN | 4.4 nm | floor; needs heavy averaging |
| 5 W | 33.4 nN | 22 nm | |
| **10 W** | **66.7 nN** | **44 nm** | matches RF power budget |
| **15 W** | **100 nN (0.10 µN)** | **67 nm** | matches RF power budget; **resolvable** |
| 45 W | 300 nN (0.30 µN) | 200 nm | top of practical CW fiber-diode range; solid overlap band |
| 150 W | 1.00 µN | 667 nm | needs high-power laser + water cooling |
| 1.5 kW | 10 µN | 6.7 µm | impractical bench laser |
| 150 kW | 1.0 mN | — | (illustrative — why photon pressure calibrates at nN–µN, not mN) |

**Reading the table:** to reach the *full* 12 µN with photons you'd need ~1.8 kW — impractical. That is exactly why photon pressure is used as a **sub-µN/nN absolute anchor**, not a full-scale actuator. A project-matched **10–15 W** calibration laser gives **~65–100 nN → 44–67 nm** of arm deflection, which the PSD/optical-lever resolves (lateral-effect PSD few-nm/√Hz; quadrant 10–100 nm/√Hz at 10–100 µW), especially with lock-in at `f_PP` and averaging. That force sits squarely in the electrostatic actuator's linear range, giving a clean <2% cross-check point. (Geometry note: keep **normal incidence** — off-axis by θ scales the useful normal force by `cos θ` and adds a tangential term; and use `1+R` not `2` once `R` is measured, e.g. R = 0.999 → factor 1.999.)

---

## In-situ continuous calibration (frequency plan)

Run three well-separated tones, all at or below the torsion resonance (`f₀ ≈ 0.1 Hz` typical), resolved by lock-in / FFT so the scale factor and drift are tracked **live**:

- `f_RF` — the anomalous-thrust modulation (RF cavity on/off), e.g. 0.005–0.01 Hz.
- `f_ES` — electrostatic cal tone, e.g. 0.03–0.05 Hz (distinct, non-harmonic vs `f_RF`).
- `f_PP` — photon-pressure tone (intermittent absolute check), e.g. 0.02 Hz.

Because the known electrostatic force is injected continuously at `f_ES`, the newtons-per-micron transfer function is measured **during** the thrust run; slow drift (thermal, suspension creep, PSD gain) is common to signal and cal and divides out. Ensure `f_ES`, `f_PP` are **not** harmonics of `f_RF` (avoids cross-contamination), and keep all below `f₀` to stay on the flat part of the mechanical transfer function.

---

## Traceability chain & uncertainty budget

**Electrostatic path:** `F = ½·V²·(dC/dx)`
- `V` → 6½-digit DMM, NIST-traceable → SI volt (Josephson). ~0.1%.
- `dC/dx` → traceable LCR meter, measured vs. position. ~1–2% (dominant).
- Alignment / vane geometry, edge effects. ~0.5–1%.
- **Combined ≈ 1.5–2.5%.**

**Photon path:** `F = (1+R)·P/c`
- `P` → NIST-/PTB-traceable thermopile → SI watt (→ kilogram / Planck const). **2–3% commercial** (the limiter; NIST radiation-pressure work pushes lower).
- `R` → measured in-situ (incident vs reflected). ~0.1%.
- `c` → exact. Incidence angle `cos θ` → keep normal, <0.2%.
- Absorption/heating of mirror, diffuse reflection → treat explicitly (as NIST did). ~0.5–1%.
- **Combined ≈ 2.5–3.5%.**

**Cross-check statement:** the two chains meet only through the *balance's* newtons-per-micron. Their agreement at the <2% goal (see caveat above about the thermopile term) is the experiment's single most important validation datum. **Deliverable uncertainty budget** should tabulate every term and quote the RSS; do not claim a 12 µN detection tighter than the calibration cross-agreement supports.

---

## Open risks

1. **Thermopile power calibration is the uncertainty floor (~2–3%).** May prevent a genuine <2% photon-vs-electrostatic agreement. Mitigation: annual NIST-traceable recal, integrating-sphere full-beam capture, in-situ `R`, and treat 2% as a *goal* not a guarantee. This is the honest bottleneck.
2. **Electrostatic charge / leakage drift.** Dielectric charging or surface leakage shifts the actuator constant. Mitigation: monitor leakage with the Keithley 6487 (10 fA res), use `V²` symmetry (±V) to cancel patch-potential offsets, guard rings.
3. **Parallel-plate gap sensitivity** (`F ∝ 1/d²`). Small gap errors → large force errors, and the attractive force moves the vane. Mitigation: use the **comb / fringing-field** geometry (gap-independent) and *measure* `dC/dx`.
4. **Mirror heating / photon-beam thermal artifact** masquerading as thrust (radiometric/outgassing force on the illuminated arm). Mitigation: vacuum, low absorption HR coating, modulate at `f_PP` and check phase, null test with beam dumped before the mirror.
5. **PSD nonlinearity & optical-lever calibration.** The nm-per-volt of the readout is itself a calibration; a lateral-effect PSD (linear, beam-shape-independent) is safer than quadrant for absolute displacement. Cross-check PSD scale with a piezo of known travel.
6. **Frequency-plan cross-talk.** If `f_ES`/`f_PP` land on harmonics of `f_RF` or near `f₀`, tones leak. Mitigation: choose incommensurate frequencies, verify orthogonality in a no-RF dry run.
7. **Extrapolation from 0.3 µN cross-check up to 12 µN.** Relies on the electrostatic `V²` linearity holding over ~40×. Mitigation: verify linearity across the *full* electrostatic range independently (it does not require photons), so photons anchor absolute scale and the sweep proves linearity.

---

## Sources

- Shaw, Stirling, Kramar, Williams, Spidell, Mirin — "Comparison of electrostatic and photon pressure force references at the nanonewton level," *Metrologia* 56(2) 025002 (2019). https://doi.org/10.1088/1681-7575/aaf9c2 · NIST page: https://www.nist.gov/publications/comparison-electrostatic-and-photon-pressure-force-references-nanonewton-level · PDF: https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=922358
- NIST Photoforce Project (radiation-pressure force ↔ laser power ↔ SI): https://www.nist.gov/programs-projects/photoforce-project
- NIST — Force Calibration Via Electrostatics (Electrostatic Force Balance): https://www.nist.gov/publications/force-calibration-electrostatics
- "Traceable force metrology for micronewton level calibration": https://www.researchgate.net/publication/237740921_Traceable_force_metrology_for_micronewton_level_calibration
- Electrostatic comb calibration on µN torsion thrust balance (2–30 µN, <0.21 µN res): https://doi.org/10.3390/aerospace9100545
- AIAA "Recommended Practice for Thrust Measurement in Electric Propulsion Testing" (electrostatic combs/plates for µN thrust-stand cal): https://arc.aiaa.org/doi/abs/10.2514/1.B35564
- Iwami et al., "Nanonewton thrust measurement of photon pressure propulsion using semiconductor laser," SPIE 8164 (2011) — 499 nN from 75 W optical, torsion thrust stand: https://ui.adsabs.harvard.edu/abs/2011SPIE.8164E..06I/abstract
- Chen & Pan, "Nanonewton force generation and detection based on a sensitive torsion pendulum" (radiation-pressure + capacitive actuation, gravitation reference): https://arxiv.org/pdf/0806.3300
- Optical force balance for the nanonewton range (Noviant et al., CNAM/HAL): https://cnam.hal.science/hal-05374727/file/1-s2.0-S0263224125031057-main.pdf
- Meta-study of laser power calibrations traceable to the kilogram: https://arxiv.org/pdf/1908.06139
- Thorlabs Position-Sensing Detectors (PDP90A lateral-effect, PDQ80A quadrant): https://www.thorlabs.com/NewGroupPage9_PF.cfm?Guide=10&Category_ID=220&ObjectGroup_ID=4400
- Trek 601C HV amplifier (0–±1 kV, <0.1% FS monitors), Advanced Energy: https://www.directindustry.com/prod/trek-inc/product-72064-1647624.html
- Keithley 6487 picoammeter/voltage source (505 V, 10 fA), pricing: https://www.testequipmentdepot.com/keithley-6487-single-channel-picoammetervoltage-source-with-gpib-rs-232-interfaces.html · datasheet: https://www.tek.com/en/datasheet/series-6400-picoammeters/6487-picoammeter-voltage-source
- All-fiber 1064 nm 1–10 W single-mode laser (~$9,990): https://beamq.com/1064nm-110w-singlemode-fibercoupled-laser-p-3042.html · AeroDIODE 10 W diode: https://shop.laserdiodesource.com/shop/1064nm-10w-fiber-coupled-laser-diode-aerodiode
- Gentec-EO UP19K-50W traceable thermopile: https://www.gentec-eo.com/products/up19k-50w-w5-d0 · Thorlabs C-series (NIST/PTB cert): https://www.thorlabs.com/NewGroupPage9_PF.cfm?ObjectGroup_ID=3333 · Newport 919P (1070 nm cal point): https://www.newport.com/f/919p-thermopile-power-sensors
