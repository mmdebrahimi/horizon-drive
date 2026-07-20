# Force Metrology Subsystem — Optimization Memo

**Project:** horizon-drive Phase-1 (detect-or-null anomalous thrust from RT copper cavity, ~10–15 W RF @ 1.836 GHz)
**Subsystem:** torsion balance + displacement readout
**Target signal:** ≈12 µN → ≈8 µm arm deflection at ±15 cm
**Prime directive:** MEASUREMENT QUALITY. The enemy is false positives — chiefly thermal center-of-mass (CoM) drift mimicking thrust.
**Date:** 2026-07-20

---

## 1. Overview

The reference instrument for this subsystem is the **TU Dresden SpaceDrive** balance (Kößling & Tajmar). Two published designs anchor every decision here:

- **SpaceDrive thrust balance (Acta Astronautica 161, 2019):** automated torsion balance, **100 nN** resolution, **10 kg** experiment capacity, laser-interferometer readout, electromagnetic (voice-coil) in-situ calibration, adjustable **eddy-current magnetic damping**, tilt control, EM shielding, **three liquid-metal feedthroughs** (≤500 V/200 kHz; ≤30 kV DC/AC; RF ≤3 GHz). Crucially: the thruster can be **rotated 180° in vacuum** to reverse thrust direction and expose thermal drift. Their verdict on EMDrive/Mach-effect: **only thermal drift, no real thrust.**
- **nano-Newton torsion balance (Rev. Sci. Instrum. 93, 074502, 2022):** a **torsional-spring** variant, **2 kg** capacity, **linear 0.01–300 µN**, off-the-shelf calibrated EM actuator, adaptable eddy-current brake, four coaxial liquid contacts.

**Sizing sanity check (independently recomputed).** For a tungsten fibre, torsion constant κ = πG r⁴ / (2L). With G≈161 GPa, d=0.90 mm (r=0.45 mm), L=300 mm:
κ = π(161e9)(4.5e-4)⁴ / (2·0.30) ≈ **3.5×10⁻² N·m/rad**.
Torque from 12 µN at 0.15 m = 1.8×10⁻⁶ N·m → θ = τ/κ ≈ **5.2×10⁻⁵ rad** → tip deflection 0.15·θ ≈ **7.8 µm**. Confirms the prior 8 µm sizing and the ~7900× floor margin.

**Key design consequence of that margin:** the 0.90 mm fibre is *far* stronger than needed. Cross-section 6.4×10⁻⁷ m²; at ~2 GPa drawn-tungsten working stress it holds >1000 N (~100 kg). A few-kg cavity+counterweight loads it to <5% of yield. The fibre diameter here is set by **stiffness/robustness/seismic-immunity, not load**. Because κ ∝ r⁴, this is the single highest-leverage tuning knob — but with 7900× margin you should deliberately *spend* sensitivity to buy stability (short period, low sway, easy handling). Estimated torsional period T=2π√(I/κ) ≈ 7 s for I≈0.045 kg·m² — a stiff, well-behaved balance.

---

## 2. Optimized Component List

### 2.1 Torsion fibre (suspension)

| Option | Spec | κ / notes | Price | Buy/DIY |
|---|---|---|---|---|
| **Tungsten wire, 0.90 mm × 300 mm (baseline)** | drawn W, G≈161 GPa | κ≈3.5e-2 N·m/rad, 7.8 µm/12µN, T≈7 s. Robust, easy to clamp. | ~$20–60/m (Goodfellow/Luma/eBay lab W wire) | **Buy wire, DIY assembly** |
| Tungsten 0.25–0.50 mm | thinner | κ drops as r⁴ (0.5 mm → ~16× more sensitive, ~3× longer period, more sway). Only if margin shrinks. | ~$20–50/m | Buy |
| Gold-coated tungsten, 20–60 µm | ultra-sensitive (grav/Casimir class) | κ ~1e-6–1e-9; **overkill** and fragile for a 12 µN / multi-kg payload | ~$100+/spool | Buy |
| Fused-silica fibre | highest Q, lowest thermoelastic loss | superior thermal noise floor but hard to clamp multi-kg; deferred | specialty | Not now |

**Recommendation:** keep **0.90 mm tungsten**. **Anneal under load** (pass ~a few hundred mA while suspended) to relieve internal stress and stabilize κ / reduce zero-drift — standard practice in Casimir/gravity balances. Crimp into a copper clamp/screw rather than glue.

### 2.2 Beam / arm material (low-CTE — thermal-drift critical)

| Material | CTE (10⁻⁶/K) | Verdict | Price |
|---|---|---|---|
| **CFRP tube (quasi-iso or axial layup)** | ~0 axial (tunable via layup) | **RECOMMENDED.** Stiff, light (low I → short period), non-magnetic, near-zero axial CTE. | $30–150 tube; ~$300+ custom layup |
| Invar-36 | ~1.0 | Good CTE + machinable BUT **ferromagnetic** — unacceptable near an RF cavity / voice-coil / eddy-brake; itself a thrust-artifact source. **Avoid.** | $$ (heavy) |
| Zerodur | ~0.02 | Lowest CTE but brittle, hard to clamp a multi-kg cavity to. Reserve for optic mounts, not the load-bearing arm. | $$$ |
| ALLVAR Alloy 30 | negative, non-magnetic Ti alloy | Interesting for a CTE-compensating standoff, not the whole arm. | $$$ niche |

**Recommendation:** **CFRP arm**, non-magnetic hardware (brass/PEEK/Ti fasteners) throughout the moving assembly. Mount cavity and counterweight symmetrically so bulk thermal expansion is common-mode about the fibre axis.

### 2.3 Displacement readout (compared)

| Option | Resolution | Cost | Complexity | Drift behaviour | Verdict |
|---|---|---|---|---|---|
| **(a) Optical lever — laser + PSD/QPD** | Sub-µm easily. 5.2e-5 rad tip angle → doubled on reflection → **~100 µm spot shift over 1 m arm**. QPD ~30× more sensitive than lateral PSD for a small centered spot. | **$400–1500 DIY** (HeNe or stabilized diode $100–600; Thorlabs **PDP90A** lateral PSD ~$1k or **PDQ80A** quad ~$1k; mirror + long path free) | **Low** | **Weak point:** laser pointing/thermal beam-path drift adds directly to the signal — the same class of artifact you're hunting. Mitigate with short, thermally-stabilized, enclosed path + stabilized source. | **Phase-1 default** — cheap, ample resolution given 100× headroom. |
| **(b) Fibre/laser interferometer** | pm–sub-nm (homodyne). Absolute displacement. | **$$$ buy** (attocube IDS3010 / SmarAct PICOSCALE — quote-only, ~$25–60k class; ultrastable-laser homodyne can be lower DIY but hard) | **High** | **Best drift immunity** — measures true displacement, not beam angle; the sensor is what SpaceDrive uses. Fibre feedthrough into vacuum is clean. | **Upgrade path** if optical-lever drift limits the null. |
| **(c) Capacitive** | sub-nm in clean env (Micro-Epsilon **capaNCDT 6500**, Lion Precision) | **$$ buy** (~$3–8k controller+probe, quote-only) | Medium | Small standoff (~<1 mm gap) risks mechanical/electrostatic coupling to the arm and adds a force; **electrostatic pull is itself a systematic**. Sensitive to humidity. | Not ideal near a moving low-force arm; skip. |

**Recommendation:** **Start with (a) optical lever** (resolution is a non-issue at 100× headroom; cost is trivial), architected so an **interferometer (b) drops in later** without rebuilding the balance. Fix the laser and PSD to the seismically isolated frame (not the vacuum chamber wall), enclose and purge/insulate the beam path, and stabilize the source. If residual readout drift ever approaches the 12 µN equivalent, migrate to a homodyne fibre interferometer.

### 2.4 Damping — eddy-current (magnetic), removable

- Copper or aluminium vane on the arm passing between **NdFeB magnets**; adjust gap to tune damping factor (SpaceDrive/2022 "adaptable eddy-current brake"). Critically damped for settling, then **backed off/removed during force runs** so the magnet field can't couple to the RF cavity or DC currents.
- Parts: N52 magnets + Cu vane + micrometer stage. **DIY, ~$50–150.**
- Keep magnets and any ferrous mass **off the moving assembly** and well away from the cavity — magnetic coupling is a documented false-positive channel.

### 2.5 In-situ calibration

- **Electrostatic comb / parallel-plate actuator** or **voice-coil** delivering known µN-scale force steps (SpaceDrive uses a calibrated EM actuator). Enables absolute force scaling and a live check of κ each run. **DIY voice coil + calibrated current, ~$100–300**, or buy a small calibrated actuator.
- Electrostatic-fin calibration (LISA-style) avoids any magnetic element — preferable near the RF cavity.

### 2.6 Vibration / seismic isolation

| Option | Perf | Price | Notes |
|---|---|---|---|
| **Minus-K negative-stiffness platform** | 0.5 Hz natural freq; 10–100× better than air, no air/electricity, **vacuum-compatible** | quote-only (~$3–8k class) | **Recommended** — passive, clean, proven in CUORE/JWST GSE. |
| Pneumatic optical table | good >few Hz | $2–6k | Needs compressed air; weaker at low freq. |
| Active piezo table | best low-freq, but limited dynamic range | $$$$ | Overkill for a stiff 7 s-period balance. |

**Recommendation:** **Minus-K passive platform** under the vacuum chamber, plus improve balance symmetry (the other seismic-coupling remedy). A stiff balance (short period) is already relatively seismic-immune; don't over-invest.

**Rough Phase-1 build budget (DIY-leaning):** fibre + CFRP arm + eddy damper + voice-coil cal ≈ **$300–800**; optical-lever readout ≈ **$400–1500**; Minus-K isolation ≈ **$3–8k** (or pneumatic ~$2–6k). Interferometer upgrade is the big deferred cost.

---

## 3. THE Null-Test-Critical Optimization — thermal-drift-rejecting geometry

**This is the single most important thing in the subsystem.** SpaceDrive's decisive artifact was **thermal drift**: RF power heats the cavity, its CoM shifts, and on a torsion arm a CoM shift about the suspension axis produces a slow deflection **indistinguishable from steady thrust** unless the geometry breaks the symmetry between them.

Two mutually reinforcing geometric defenses, both taken from Tajmar's design:

1. **In-vacuum 180° thrust reversal (the core discriminator).** Mount the cavity on a rotatable fixture so its thrust axis can be flipped **without breaking vacuum or re-trimming the balance**. A **genuine thrust reverses sign** with the cavity; a **thermal/CoM-drift artifact does not cleanly reverse** (it tracks the balance/heat-path frame, not the thrust axis). Take every measurement in ≥2 (ideally 3) orientations. **A signal that fails to invert is an artifact — full stop.** This is what nulled the EMDrive.

2. **Counterbalanced / suspension-point placement to null the thermal CoM lever arm.** Hang the cavity and a **thermally matched counterweight symmetrically** about the fibre axis so bulk expansion is common-mode (produces no net torque). In the inverted/double-pendulum arrangement, the hot mass is positioned so its thermal excursion has **near-zero moment arm** about the rotation axis, while real thrust (a horizontal force at radius) retains full moment arm. This decouples the heat-driven displacement from the force-driven displacement geometrically, before any data analysis.

**Supporting practices that make the geometry work:**
- **Low-CTE non-magnetic arm (CFRP)** so the arm itself doesn't warp asymmetrically under the thermal gradient.
- **Thermal instrumentation:** thermocouples/thermistors on cavity, arm, and counterweight to *measure* the drift and correlate it out; run RF-off "dummy-heater" runs that inject the same heat with no RF to map the pure thermal response.
- **Power/CoM symmetry:** route RF and DC via **liquid-metal / coaxial-liquid feedthroughs on the rotation axis** so cable stiffness and I²R heating don't add an off-axis force or torque.
- **Duty-cycle / modulation:** pulse the RF and look for the force at the switching frequency, where slow thermal drift has little power — separates a fast force response from the slow thermal tail.

**Acceptance criterion for a real detection:** a deflection that (i) **inverts sign under 180° cavity rotation**, (ii) is **absent in matched dummy-heater runs**, (iii) tracks RF **on/off modulation** faster than the thermal time constant, and (iv) survives the electrostatic in-situ **force calibration** scaling. Anything failing (i) is thermal.

---

## 4. Open Risks

1. **Optical-lever beam-path drift** masquerades as thrust — same artifact class as the enemy. Mitigate (enclosed short path, stabilized source, isolated mounting) or move to interferometer. Highest-priority readout risk.
2. **Magnetic coupling:** NdFeB damping magnets, voice-coil, or any ferrous fastener interacting with the RF cavity/DC currents → spurious force. Keep all magnetics off the moving assembly, damping removed during runs, prefer electrostatic calibration.
3. **Feedthrough force/thermal coupling:** power leads exert stiffness and inject heat off-axis. Liquid-metal/coax-liquid on-axis contacts are the SpaceDrive answer; a DIY version (mercury-free galinstan cups) is non-trivial and a build risk.
4. **Fibre zero-drift / creep** if un-annealed; anneal-under-load and allow settling; monitor κ via periodic calibration.
5. **Stiff-balance sensitivity trade:** 0.90 mm fibre spends most of the 7900× margin on robustness. If Phase-1 signal is smaller than modeled, have a thinner-fibre swap plan (κ ∝ r⁴).
6. **Vacuum requirement:** thermal-drift discrimination and buoyancy/convection control effectively **require vacuum** (SpaceDrive ran in vacuum). Air runs will be convection-artifact-limited — budget for a chamber.
7. **Capacitive readout electrostatic force** (if ever used) adds a systematic — reason it's deprioritized here.

---

## 5. Sources (URLs)

- SpaceDrive thrust balance, IAC/Acta Astronautica (100 nN, 10 kg, 180° reversal, liquid-metal feedthroughs, "only thermal drifts"): https://tu-dresden.de/ing/maschinenwesen/ilr/rfs/ressourcen/dateien/forschung/folder-2007-08-21-5231434330/ag_raumfahrtantriebe/IAC-The-SpaceDrive-Project-Thrust-Balance-Development-and-New-Measurements-of-the-Mach-Effect-and-EMDrive-Thrusters.pdf?lang=en
- SpaceDrive, ScienceDirect (Acta Astronautica 161, 2019): https://www.sciencedirect.com/science/article/abs/pii/S009457651832071X
- SpaceDrive, ADS record: https://ui.adsabs.harvard.edu/abs/2019AcAau.161..139K/abstract
- Kößling & Tajmar, "Design and performance of a nano-Newton torsion balance," Rev. Sci. Instrum. 93, 074502 (2022) — torsional spring, 2 kg, linear 0.01–300 µN, eddy brake, 4 coaxial liquid contacts: https://pubs.aip.org/aip/rsi/article/93/7/074502/2849025/Design-and-performance-of-a-nano-Newton-torsion (DOI 10.1063/5.0086975)
- "A thousand times better instrument…" (interferometer readout, nano-newton motivation): https://www.nextbigfuture.com/2019/06/a-thousand-times-better-instrument-will-investigate-emdrive-and-mach-propulsion.html
- Torsion fibre physics — κ ∝ r⁴, tungsten low-dissipation, annealing, diameter/load examples (Casimir 60 µm; grav 20 µm): https://arxiv.org/pdf/1508.07259 ; https://arxiv.org/pdf/hep-ph/0405262 ; https://phys.libretexts.org/Bookshelves/Classical_Mechanics/Classical_Mechanics_(Tatum)/20:_Miscellaneous/20.03:_Shear_Modulus_and_Torsion_Constant
- Micro-Newton torsion thrust stands, tungsten-fibre + optical readout: https://www.researchgate.net/publication/221800884_A_torsion_balance_for_impulse_and_thrust_measurements_of_micro-Newton_thrusters ; https://electricrocket.org/IEPC/235_2.pdf
- Thermal-noise decoupling in a torsion balance: https://www.researchgate.net/publication/353494640_Thermal_Noise_Decoupling_of_Micro-Newton_Thrust_Measured_in_a_Torsion_Balance
- Displacement readout — Thorlabs PSDs (PDP90A lateral 750 nm res, PDQ80A quad, quad ~30× more sensitive): https://www.thorlabs.com/NewGroupPage9_PF.cfm?Guide=10&Category_ID=220&ObjectGroup_ID=4400
- Homodyne fibre interferometry, picometer displacement (ultrastable laser): https://arxiv.org/pdf/2411.06658 ; nonlinearity correction: https://www.researchgate.net/publication/253279100_Fine_correction_of_nonlinearity_in_homodyne_interferometry
- Capacitive sub-nm sensors: https://www.micro-epsilon.com/displacement-position-sensors/capacitive-sensor/capaNCDT-Sensoren/ ; https://www.lionprecision.com/products/capacitive-sensors/
- Low-CTE beam materials (CFRP tunable, Invar magnetic, Zerodur brittle, ALLVAR): https://www.nature.com/articles/s41598-024-65836-1 ; https://allvaralloys.com/carbon-fiber-reinforced-polymers-cfrp-vs-allvar-near-zero-thermal-expansion-materials/
- Vibration isolation — Minus-K negative stiffness (0.5 Hz, no air/electricity, vacuum, CUORE/JWST); active vs pneumatic: https://www.minusk.com/content/technology/how-it-works_passive_vibration_isolator.html ; https://www.opticaltable.com/blog-detail/active-vs-pneumatic-vibration-isolation-for-optical-tables-a-deep-dive-and-selection-guide
- Cryogenic torsion balance, passive isolation + seismic-coupling remedies: https://arxiv.org/pdf/2206.02890
