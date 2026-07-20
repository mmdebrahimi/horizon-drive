# Horizon-Drive — Vacuum System Optimization Memo

**Subsystem:** Vacuum (chamber · pumping · gauging · pump-to-balance vibration decoupling · cleanliness)
**Date:** 2026-07-20
**Scope:** Phase-1 detect-or-null of ~12 µN claimed anomalous thrust from a room-temperature Cu TM010 cavity (~1.836 GHz, Q₀≈27k, 10–15 W RF).
**Design axiom:** The enemy is the false positive. The vacuum subsystem exists almost entirely to *kill* the gas-mediated artifacts (radiometric/Knudsen force, natural convection, ionic-wind coupling, oil-contamination signal drift) that produced the discredited EmDrive/Eagleworks results. Measurement cleanliness > convenience > cost.

---

## Overview

The vacuum subsystem must reach and *hold* **<1×10⁻⁶ torr** cleanly, quietly, and without introducing hydrocarbons — because the dominant historical false positives are pressure-dependent thermal/gas forces that vanish only deep in the free-molecular regime. Three coupled requirements:

1. **Deep free-molecular vacuum (≤10⁻⁶ torr).** At 10⁻³ torr (roughing only) the residual gas can generate radiometric/convective forces *larger than the 12 µN signal* (quantified below). This is the single most important null-test constraint.
2. **Oil-free gas path.** No oil-sealed rotary vane on the foreline without heavy mitigation; backstreaming hydrocarbons condense on the warm cavity and can *fake* pressure-/temperature-correlated forces and slow outgassing drift. Prefer a fully dry stack (turbo + dry diaphragm/scroll).
3. **Mechanical decoupling of the pump from the torsion balance.** A running turbopump/backing pump injects vibration at 10⁻⁴–10⁻³ g levels; edge-welded bellows + a physically separate pump stand keep pump lines from short-circuiting the balance's isolation.

The good news: the target pressure is modest by UHV standards (10⁻⁶ torr is "high vacuum," not UHV), the chamber is small, and gas load is low (clean metal cavity, no process gas). A single ~70 L/s turbo on a dry backing pump reaches 10⁻⁶ torr on a well-prepared small chamber in tens of minutes — no ion pump, no cryo, no LN₂ trap needed for Phase-1.

---

## Optimized component list (vendor / model / price)

Prices are rough 2026 street/used estimates; vacuum gear sells largely by quote, so ranges reflect labx/eBay/dealer refurb spreads.

### 1. Chamber

Torsion balance needs internal volume for a ~0.3–0.5 m arm + the cavity + counterweight, so a small spherical/bell chamber is too tight. Target a **stainless (304/316L) cylindrical or box chamber, ~450–600 mm ID**, electropolished interior, multi-port.

| Item | Vendor / model | Rough price | Notes |
|---|---|---|---|
| Chamber | Kurt J. Lesker standard **cylindrical multiport** (~18–24 in, ISO-K + CF ports) or **box chamber** | New ~$4k–9k; **used/surplus ~$1.5k–4k** (eBay/EquipNet/BMI Surplus) | Order/spec extra ports; 304 SS, EP finish. Spherical only if arm fits. |
| Alt. chamber | Surplus semiconductor/LEYBOLD/MDC cylindrical chamber | **~$800–2.5k used** | Best value; verify port count + flange condition. |

**Port layout (plan before buying):** one large pumping port (ISO-K 63/100 or CF 6") low on the wall facing the turbo throat; RF feedthrough port (CF 2.75"); DC power/thermocouple feedthrough port; ≥2 optical viewports (interferometer/optical-lever readout of the balance + IR camera for thermal witness); gauge port (KF/CF); vent/purge valve port; spare blank. Keep the RF feedthrough and pumping port on opposite sides so pump lines don't wrap the balance.

### 2. Feedthroughs & viewports (Kurt J. Lesker or MDC/surplus)

| Item | Model / spec | Rough price |
|---|---|---|
| RF power feedthrough | KJL **SMA coaxial, 40 GHz, CF 2.75", double-ended**, 50 Ω, leak <5×10⁻¹⁰ mbar·L/s | New ~$300–700; used ~$150–350 |
| DC / thermocouple feedthrough | KJL multipin or coax CF/KF | ~$150–400 |
| Optical viewport | KJL **CF 2.75" fused-silica/Kodial viewport** (×2) | ~$150–400 each; used ~$80–200 |
| Vent/purge valve | KF25 all-metal or dry-N₂ leak valve | ~$100–300 |

### 3. Pumping stack — OIL-FREE (primary recommendation)

**Turbo + dry backing, fully hydrocarbon-free.** Two equally good routes:

| Option | Vendor / model | Speed | Rough price |
|---|---|---|---|
| **A (recommended, turnkey)** | **Pfeiffer HiCube 80 Eco** pumping station = HiPace 80 turbo (**67 L/s N₂, ISO-63**) + **MVP diaphragm** backing + DCU control | 67 L/s | Refurb/used **~$6.5k–10.8k**; new ~$7.9k |
| **B** | **Agilent TwisTorr 74 FS** turbo (60–70 L/s, ISO-63/CF, floating suspension = low-vib) + **IDP-3 dry scroll** backing + controller + air-cool kit (Ideal Vacuum package P1012551) | 60–70 L/s | New station quote ~$8k–12k; **used pump ~$2k–4k**, IDP-3 ~$2k–3k used |

Both are magnetically/mechanically suspended, oil-free on the pumped side → no turbo-oil backstreaming. **Diaphragm** backing (Option A) is the cleanest and quietest; **dry scroll** (Option B, IDP-3) gives lower backing pressure and more headroom if outgassing is higher than expected. Either reaches ≤10⁻⁶ torr on this small clean chamber.

**Explicitly avoid** an oil-sealed rotary-vane backing pump. If cost forces one (e.g., a free surplus Edwards RV/E2M), it MUST get: (a) a **molecular-sieve (13X) foreline adsorption trap**, (b) an **anti-suck-back / foreline isolation valve** (backstreaming spikes on power loss — oil floods up the foreline into the turbo and chamber), and (c) acceptance that it's second-best. The whole point of Phase-1 is a *clean* null; don't reintroduce the contamination variable to save a few hundred dollars.

### 4. Gauging — wide-range Pirani + cold-cathode combo

| Item | Vendor / model | Range | Rough price |
|---|---|---|---|
| Combo gauge | **Pfeiffer PKR 361** ActiveLine FullRange (Pirani + cold-cathode in one head), CF 2.75" or KF25 | atmosphere → ~7.5×10⁻¹⁰ torr | New ~$1k–1.5k; **used ~$400–700** |
| Alt combo | Agilent **FRG-700** / Inficon **BPG400** inverted-magnetron + Pirani | atm → ~10⁻⁹ torr | Used ~$400–800 |
| Display/controller | Pfeiffer TPG 361/362 single/dual, or read via station DCU | ~$500–900 new; used ~$200–400 |

One PKR 361 covers the whole pumpdown from atmosphere into high vacuum with a single head — critical, because you need to *log pressure continuously against the thrust trace* to prove the signal is (or isn't) pressure-correlated. Mount it on its own port, not in the pump line, so it reads chamber pressure, not foreline pressure. A cheap second Pirani on the foreline is useful for backing-pump health.

### 5. Pump-to-balance vibration decoupling (measurement-critical)

| Item | Model / spec | Rough price |
|---|---|---|
| Flexible coupling | **Edge-welded (formed) bellows**, ISO-63/CF, ~150–250 mm free length | New ~$400–900; used ~$150–400 |
| Pump mounting | Turbo + backing pump on a **separate, floor-standing frame**, not bolted to the chamber/optical table | shop-built ~$100–300 |
| Elastomer/spring pump feet | Sorbothane pads or spring isolators under the pump frame | ~$50–200 |
| (Optional) balance feet | Passive spring/eddy-current damping under the balance table | — (balance subsystem) |

**Decoupling rules:** (1) route the turbo→chamber connection through an **edge-welded bellows** to break the vibration path; tune length so it isn't pulled taut (a taut/stiff bellows transmits vibration; a too-soft one collapses under the ~atmospheric compressive load — bellows rigidity is a real design tradeoff). (2) Put the **entire pump stack on its own stand on the floor**, mechanically independent of the balance's isolation table. (3) Run the turbo on **air cooling with the fan on a decoupled bracket** (or water cooling) so fan imbalance doesn't couple in. (4) Consider **gating strategy**: reach base pressure, then measure with the turbo at steady state (never spin-up/down during a thrust run) — steady rotor = narrowband, predictable vibration you can notch-filter.

### 6. Cleanliness / bakeout

- **No bakeout hardware required for 10⁻⁶ torr** with a clean metal chamber — but do a mild bake (heater tape or oven, ~80–120 °C for a few hours) after any chamber open to drive off water, the dominant gas load. Water outgassing, not pump speed, sets your pumpdown time.
- **Glove-handle the cavity and internals**, solvent-clean (IPA/acetone) + vacuum-dry; avoid fingerprints and machining oils on the copper.
- **All-metal or fluoroelastomer (Viton) seals**; prefer CF/copper-gasket on ports near the cavity. Viton on KF ports is fine for 10⁻⁶ torr.
- **Dry-N₂ backfill** on venting to avoid pulling in humid room air (shortens next pumpdown).

**Indicative total (used/refurb-heavy build):** chamber+ports ~$2.5k–5k · pumping station ~$6.5k–11k · gauge+display ~$0.7k–1.5k · bellows/isolation ~$0.5k–1.2k → **~$10k–19k**. A scrounged surplus turbo + dry scroll + used chamber can push the low end toward ~$6k–8k.

---

## The single null-test-critical optimization

**Reach and continuously verify ≤1×10⁻⁶ torr, with the pressure trace logged against the thrust trace — because the artifact that fakes ~12 µN of thrust is a *pressure-dependent gas force*, and it only falls decisively below the signal deep in the free-molecular regime.**

Why this, above everything else in the subsystem:

**The physics.** Air's mean free path λ scales as 1/P: ~68 µm at 760 mtorr, ~0.65 cm at 7.6 mtorr, and ~50 m at 10⁻⁶ torr. Two distinct gas artifacts track this:

- **Natural convection** (buoyancy-driven heat currents around the warm, RF-powered cavity) needs continuum flow (Kn = λ/D ≲ 0.01). It **ceases below ~1 torr** for cm-scale gaps. Roughing-pump-only tests (~10⁻³–10⁻² torr) still have appreciable gas; convective + thermal-plume forces on an asymmetric warm body are a classic thrust mimic.
- **Radiometric / Knudsen thermal-creep force** — the Crookes-radiometer effect — **peaks in the transition regime (Kn≈1**, i.e., ~0.1–1 torr for cm gaps) and falls off *linearly with P* in the free-molecular regime (free-molecular heat/momentum transfer H ∝ P). So ~10⁻³ torr sits near the *worst-case* radiometric peak, while 10⁻⁶ torr is three decades down the falloff.

**Order-of-magnitude quantification** (assumptions stated; a factor-of-few estimate, not a precise model). Radiometric edge force on a heated vane ≈ Δp·A, with Δp ≈ P·(ΔT/2T) in the transition/free-molecular edge. Take exposed cavity area A ≈ 100 cm² = 0.01 m², RF-driven surface ΔT ≈ 10 K, T = 300 K → (ΔT/2T) ≈ 0.017:

| Pressure | P (Pa) | Radiometric-scale force ≈ P·(ΔT/2T)·A | vs. 12 µN signal |
|---|---|---|---|
| **10⁻³ torr** (roughing only) | 0.133 | **~23 µN** | **~2× the signal — swamps it** |
| ~5×10⁻⁴ torr | 0.067 | ~11 µN | ≈ crossover (force = signal) |
| **10⁻⁶ torr** (target) | 1.3×10⁻⁴ | **~0.02 µN** | **~600× below signal** |

So the crossover where gas force ≈ the 12 µN signal lands near **~5×10⁻⁴ torr**, and you want a **≥100× margin below that → operate at ≤10⁻⁶ torr** (giving ~3 orders of headroom and covering the ΔT and area uncertainties). This is *exactly* the trap earlier EmDrive demonstrations fell into: at rough vacuum the residual-gas thermal force is comparable to, or larger than, the claimed thrust, so any warm asymmetric cavity "produces thrust."

**How the subsystem operationalizes it:** (1) the dry turbo stack gets you to ≤10⁻⁶ torr cleanly; (2) the PKR 361 logs pressure through the whole run; (3) the killer diagnostic — **sweep pressure (e.g., 10⁻² → 10⁻³ → 10⁻⁴ → 10⁻⁶ torr) at fixed RF power and watch the apparent thrust.** A real anomalous thrust is *pressure-independent*; a radiometric/convective artifact rises toward the ~0.1–1 torr peak and dies at 10⁻⁶ torr. That pressure-dependence sweep is the single most decisive false-positive discriminator the vacuum subsystem enables, and it's why deep, *measured*, *logged* vacuum — not merely "some vacuum" — is the linchpin.

---

## Open risks / unknowns

- **Balance-arm envelope vs. chamber size.** Final chamber ID depends on the mechanical subsystem's arm length and readout geometry. A 450–600 mm chamber assumed; confirm the torsion balance fits with clearance before purchase. TU Dresden used a ~0.9 m chamber — larger buys margin but costs vacuum time and money.
- **Outgassing load unknown until built.** Copper cavity + any polymer/adhesive internals set the real gas load. If base pressure stalls above 10⁻⁶ torr, first suspect water (bake harder) then virtual leaks / dirty internals, not pump speed. Budget for a mild bakeout even though "not required."
- **Bellows rigidity tuning is empirical.** The right free length/stiffness to isolate pump vibration without collapsing under atmospheric load must be tuned on the actual stand; may need iteration or a secondary passive isolator. Measure residual vibration with the balance in place.
- **Ionic wind / EM feedthrough are not fully a vacuum problem.** Vacuum suppresses ionic wind (needs gas) and convection, but EM feedthrough coupling to the balance is unaffected by pressure — the pressure-sweep null test does not discriminate EM artifacts. Coordinate with the RF-shielding and balance subsystems.
- **Radiometric estimate is order-of-magnitude.** The Δp·A model with assumed ΔT=10 K, A=100 cm² is a factor-of-few sizing, not a validated DSMC result. The *conclusion* (≥100× margin at 10⁻⁶ torr) is robust to these assumptions, but the exact crossover pressure is uncertain to ~×3.
- **Power-loss backstreaming (if any oil is present).** If a rotary-vane backing pump is ever used, a power failure floods oil up the foreline; an all-dry stack removes this failure mode entirely — a reason to pay for dry backing rather than mitigate an oil pump.
- **Gauge cross-calibration.** Cold-cathode gauges read gas-species-dependent and can drift/contaminate; cross-check the PKR 361 against a second gauge periodically, and never trust a single uncalibrated reading as proof of the null-test pressure.

---

## Sources (URLs)

- Tajmar et al., "High-accuracy thrust measurements of the EMDrive and elimination of false-positive effects," CEAS Space Journal (2022): https://link.springer.com/article/10.1007/s12567-021-00385-1
- "In a comprehensive new test, the EmDrive fails to generate any thrust," Phys.org (2021): https://phys.org/news/2021-04-comprehensive-emdrive.html
- Knudsen / radiometric thermal force, pressure & temperature-gradient dependence (Knudsen force review, ResearchGate): https://www.researchgate.net/publication/47651472_What_Determines_Knudsen_Force_At_The_Microscale
- Thermal transpiration / Knudsen microscale propulsion (Ronney, USC): http://ronney.usc.edu/Research/MicroFIRE/Knudsen.pdf
- Flow regimes / Knudsen number / mean free path vs pressure (ScienceDirect, "Molecular Regime overview"): https://www.sciencedirect.com/topics/engineering/molecular-regime
- Free-molecular heat transfer regime (DSPE thermomechanics): https://www.dspe.nl/knowledge/thermomechanics/chapter-2-in-depth/conduction-in-gasses/regime-1-free-molecular-heat-transfer/
- KJL characteristic dimensions / mean-free-path examples (0.65 cm ↔ 65 cm across 1 torr): https://de.lesker.com/newweb/technical_info/vacuumtech/basicvac_05_characdims.cfm
- Air-pressure dependence of natural-convection heat transfer (ResearchGate): https://www.researchgate.net/publication/45534616_Air_Pressure_Dependence_of_Natural-Convection_Heat_Transfer
- Pfeiffer HiCube 80 Eco pumping station (Provac / AVAC / LabX pricing): https://www.provac.com/products/pfeiffer-hicube-80-eco-pumping-station · https://avac.com/product/hi-cube-80-eco-turbo-pumping-station-w-hipace-80-turbo-pump-mvp-015-2-diaphram-pump-pms7310000/
- Agilent TwisTorr 74 FS turbo + IDP-3 dry scroll package (Ideal Vacuum): https://www.idealvac.com/en-us/Agilent-Varian-TwisTorr-74-FS-Turbo-Pump-Package-Deal-with-ISO-K-63-Inlet-and-IDP-3-Dry-Scroll-Backing-Pump-74FS-AG-Remote-Controller-and-Air-Cooling-Kit/pp/P1012551
- Agilent TwisTorr 74 FS (floating suspension, low vibration, no hydrocarbon contamination): https://www.agilent.com/en/product/vacuum-technologies/turbo-pumps-controllers/turbo-pumps/twistorr-74-fs-turbo-pump
- Pfeiffer PKR 361 Pirani/cold-cathode FullRange gauge (spec + pricing): https://highvacdepot.com/product/pfeiffer-pkr-361-gauge/ · https://www.pfeiffer-vacuum.com/en/products/measurement-analysis/measurement/activeline/activeline-gauges/16099/pirani-cold-cathode-gauge-pkr
- KJL spherical / cylindrical / box chambers + SMA 40 GHz feedthroughs + viewports: https://www.lesker.com/newweb/chambers/std_sphericalchamber.cfm · https://www.lesker.com/newweb/feedthroughs/coaxial-sma-feedthroughs-40ghz.cfm?pgid=cf-flange-double-ended · https://www.lesker.com/feedthroughs-viewports.cfm?section=vacuum-viewports
- Oil backstreaming / foreline traps / dry-pump advantage (DigiVac, KJL, Leybold): https://digivac.com/prevent-oil-backstreaming-in-high-vacuum-environments/ · https://www.lesker.com/blog/backstreaming-pump-oil-vapors-vacuum-systems · https://www.leybold.com/en/knowledge/vacuum-fundamentals/vacuum-generation/how-filters-work-in-rotary-pumps
- Torsion-balance thrust stand vibration isolation / bellows decoupling / eddy-current damping: https://pubs.aip.org/aip/rsi/article/93/11/114501/2849448/Validation-of-a-torsional-balance-for-thrust · https://www.sciencedirect.com/science/article/abs/pii/S0094576525008872
