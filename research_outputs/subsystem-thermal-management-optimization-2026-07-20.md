# Subsystem Optimization Memo — Thermal Management + Frequency Lock

**Experiment:** horizon-drive Phase-1 (detect-or-null ~12 µN claimed anomalous thrust)
**Cavity:** room-temp copper, 1.836 GHz, Q ≈ 27,000, 10–15 W RF dissipated
**Subsystem role:** kill the #1 false positive — RF heating → CTE detuning → stored-energy drift → COM shift that mimics thrust.
**Date:** 2026-07-20 · Personal research project · Optimize for measurement quality (prices noted, rough)

---

## 1. Overview

The dominant EmDrive-class false positive is thermal, confirmed by the Tajmar/TU-Dresden work: RF heats the copper, thermal expansion shifts the center of gravity, and a torsion/pendulum balance reads that COM shift as a thrust with the "correct" signature (it even reverses when the thruster is flipped). Once the Dresden group rebuilt around thermal-insensitive geometry, the anomalous thrust vanished to below the classical-radiation limit (link.springer.com/article/10.1007/s12567-021-00385-1).

Copper CTE ≈ 17 ppm/°C. At Q ≈ 27,000 the loaded linewidth is f/Q ≈ 1.836 GHz / 27,000 ≈ **68 kHz**. A 1 °C bulk temperature rise stretches the cavity by 17 ppm, moving the resonant frequency by ~17 ppm × 1.836 GHz ≈ **31 kHz — roughly half a linewidth per °C.** With a fixed-frequency drive, that alone drops stored energy by tens of percent while dumping the reflected power somewhere new. This is why **frequency lock is not optional**: without it, stored energy (hence any real thrust) is a runaway function of temperature and indistinguishable from the thermal-expansion artifact.

The subsystem has four jobs, in priority order:
1. **Track resonance** (PLL/dither lock) so stored energy stays constant despite detuning — decouples the real observable from temperature.
2. **Hold dissipated power constant** across the on/off modulation phases (dump-load balancing) so heat is common-mode.
3. **Symmetrize** heat deposition about the balance axis so any residual heating produces no net torque.
4. **Monitor** temperature at enough points to reconstruct the thermal-expansion artifact as an independent covariate and subtract/veto it.

---

## 2. Optimized component list (parts + rough prices)

### 2a. Frequency-lock chain (track resonance, hold stored energy constant)

**Recommended architecture: dither / reflected-power lock, not full PDH.** At Q ≈ 27,000 the 68 kHz linewidth is *broad* — this is a forgiving lock. Full Pound-Drever-Hall (EOM-equivalent sidebands, high-frequency demod) is designed for MHz-and-narrower optical/superconducting cavities and is overkill here. A **dither-lock** — small frequency dither, detect the component of reflected power at the dither frequency, demodulate to a bipolar error signal, integrate back onto the synthesizer's tuning word — is functionally low-frequency PDH, uses no EOM, and maps directly onto a microcontroller/FPGA. It is intensity-insensitive (derivative-based error), which matters because the PA output will drift with its own temperature.

| Item | Part / model | Rough price | Notes |
|---|---|---|---|
| Agile source (VCO+PLL synth) | ADF4351 eval module (35 MHz–4.4 GHz, SPI) | $30–60 | 1.836 GHz = 3.672 GHz VCO ÷2. Cheap start. Phase noise mediocre — fine for a Q=27k lock. |
| **Better source** | Windfreak SynthHD (v2) or SynthNV Pro | $600–1,300 | Cleaner phase noise, USB/software freq control, faster settling for the servo loop. Preferred for the real run. |
| Lock controller | Red Pitaya STEMlab 125-14 (FPGA + fast ADC/DAC) | $400–500 | Runs dither generation + demodulation + PID in the PyRPL framework; also doubles as the reflected-power lock-in. |
| — or simpler | Teensy 4.1 / STM32 + external DDS | $30–80 | Firmware dither-lock if bandwidth demands are modest (they are). |
| Directional coupler (fwd/refl pickoff) | Mini-Circuits ZUDC10-183+ (10 dB, 0.5–18 GHz) or RBDC9-182 | ~$80–150 | Taps forward + reflected power for the lock error signal and for a stored-energy proxy. |
| Isolator/circulator | SMA circulator, 1.7–2.0 GHz band (Pasternack / DiTom) | ~$150–300 | Protects PA from cavity reflection; port-3 → dump load. 18–20 dB isolation typ. |
| RF detectors (fwd/refl power) | Analog Devices ADL5904 / LTC5596 log detectors, or Schottky diode dets | $20–60 ea (×2) | Reflected-power minimum = on-resonance; forward−reflected ≈ delivered power for the stored-energy proxy. |
| 15 W PA | Mini-Circuits ZHL-class or Qorvo/CREE CGH40006S-based module | $300–900 | 1.836 GHz, 15 W. Mount OFF the balance if at all possible (Dresden lesson — see §3). |

**Stored-energy servo (second loop):** the dither lock keeps you *on* resonance; a slow outer loop should hold **delivered power** (forward − reflected, from the two detectors) constant by trimming PA drive. On resonance with constant delivered power, stored energy U = Q·P_diss/ω is pinned. This two-loop design is what actually "holds stored energy constant despite thermal detuning."

### 2b. Temperature monitoring

**Sensor choice is bimodal by location:**

- **Inside / on the cavity walls (in the RF field):** use **fiber-optic sensors, not thermocouples/RTDs.** Metal leads act as antennas in the cavity — they arc, self-heat (>10 °C error reported), perturb the field, and degrade Q. Fluorescence (GaAs/phosphor-tip) fiber probes give ±0.1–0.5 °C at a few points; FBG arrays give ±0.5–1 °C at many multiplexed points along one fiber (strain-relieved packaging required). Vendors: Osensa, FISO, Rugged Monitoring, Opsens.
  - Fluorescence probe + single-channel interrogator: **~$1,500–3,000** for 1–4 channels.
  - FBG interrogator + 8–16 grating fiber: **~$3,000–6,000** (justified only if you want dense wall mapping).
- **Off the RF field (coax body, chamber walls, balance arm, PA heatsink, dump load):** **4-wire Class-A or 1/10-DIN PT100 RTDs.** RTDs beat thermocouples here decisively — 1/10-DIN ≈ ±0.03 °C at 0 °C vs Type-K ±2.2 °C, plus long-term stability (no inhomogeneity drift). 0.01 °C *resolution* is readily available.
  - 1/10-DIN PT100 probes: **$40–120 ea.**
  - Multi-channel RTD logger: Omega OM-CP-RTDTempX (4/8/12/16-ch, 0.001 °C resolution, 4 Hz, NIST cert) **~$1,000–2,000**; or MicroEdge SITE-LOG LRTD (5-ch) **~$300–500**.

**Placement (minimum viable sensor map, ~10–12 channels):**
| # | Location | Sensor | Purpose |
|---|---|---|---|
| 1–2 | Cavity wall, two ends of the taper (small/large) | fiber fluorescence | primary detune-driver temp; reconstruct CTE frequency shift |
| 3–4 | Cavity wall, **symmetric pair straddling the balance axis** | fiber | differential heating = the classic false-positive; must read ~equal |
| 5 | Coax / feed near cavity port | PT100 | cable heating (feed-through artifact source) |
| 6–7 | Chamber wall, near-thruster vs far-thruster | PT100 | wall-reradiation asymmetry onto the balance |
| 8 | Balance arm / pivot | PT100 | thermal expansion of the balance itself |
| 9 | Dump load body | PT100 | verify heat lands where intended |
| 10 | PA heatsink (if PA on balance) | PT100 | electronics COM-shift source |
| 11–12 | Ambient reference ×2 | PT100 | common-mode / drift subtraction |

Log all channels time-synced with the thrust and RF-power streams so temperature is a **regressable covariate**, not just a health check.

### 2c. Thermal isolation + symmetrization

- **Mount PA + amplifier electronics OFF the balance** (battery-backed "black box" only, or PA fully off-arm feeding through a rotary/low-stiffness coax). Dresden traced a large share of the artifact to on-balance electronics heating + feed-through; moving mass/heat off the moving frame removed it.
- **Symmetric thermal straps / heat spreader:** bond the cavity to the balance through a *symmetric*, high-conductivity path (e.g., paired copper braid straps of equal length on both sides of the axis) so bulk expansion pushes the COM along the axis, producing zero torque, rather than sideways.
- **Radiation shield / low-emissivity wrap** (polished-Al or MLI) around the cavity to slow and symmetrize radiative coupling to nearby chamber walls; keeps sensors 6–7 balanced. ~$50–150.
- **Mount below the suspension point** (Dresden's inverted counterbalanced double pendulum) so thermal-expansion COM shifts are geometrically nulled at the pivot. This is a balance-design constraint your subsystem must respect, not a bought part.

### 2d. Dump-load thermal placement (the constant-power trick)

Route the circulator's isolated port to a **50 Ω dump load whose heat is thermally tied to the same spreader/location as the cavity's own dissipation** (or at minimum, off the balance and symmetric about the axis). Goal: whether the cavity is on- or off-resonance, **the total RF power dissipated in the balance-frame region is identical and lands in the same place.** When off-resonance, power the cavity rejects goes to the dump; when on-resonance it's absorbed in the copper — arrange the geometry so the balance can't tell the difference thermally.
- 50 Ω N/SMA termination, 30–50 W: **$30–100.**

---

## 3. The single null-test-critical optimization

**Modulate on-resonance ↔ off-resonance at CONSTANT total dissipated RF power, with the PLL/dither lock holding the on-resonance stored energy fixed — so copper heating is identical in both modulation phases and the thermal COM-shift artifact becomes common-mode (DC), while only stored-energy-dependent thrust appears at the 0.02 Hz modulation frequency where the lock-in looks.**

Why this is make-or-break: the naïve scheme modulates RF **on/off** at 0.02 Hz. But on/off *also modulates the heat* at 0.02 Hz — so the thermal-expansion artifact sits **exactly at the lock-in reference frequency and is NOT rejected.** Lock-in rejects everything except the reference band; it cannot save you from a thermal signal synchronous with the modulation. Two things must be true simultaneously:

1. **Constant-power modulation, not on/off.** Switch the *cavity* between on-resonance (stored energy high) and off-resonance (stored energy ~0) while a balancing dump load keeps **total delivered/dissipated power constant** every phase. Copper heating no longer has a 0.02 Hz component → thermal artifact moves to DC/common-mode → lock-in rejects it. A genuine thrust that scales with stored energy still toggles at 0.02 Hz → survives.
2. **Time-constant separation as the backstop.** Make the cavity's thermal time constant τ_th **much longer than the 50 s modulation period** (large copper thermal mass, deliberately slow radiative coupling). Then even residual heating imbalance between phases is a slow ramp whose first-harmonic content at 0.02 Hz is heavily rolled off (a single thermal pole at τ_th ≫ 50 s attenuates the 0.02 Hz component by ~ωτ_th). Critically, **avoid τ_th ≈ 50 s** — that is the worst case, where the thermal response peaks at the modulation frequency. Push τ_th to many minutes.

Combined, these convert the thermal effect from *synchronous artifact* (fatal) to *common-mode + heavily-attenuated* (rejectable). Then the temperature sensor map (§2b) provides the independent check: regress the demodulated thrust against the measured wall/differential temperatures — a real thrust shows **zero correlation** with the reconstructed CTE detune; an artifact shows the correlation and is vetoed. This — PLL lock + constant-power modulation + τ separation + temperature-covariate regression — is the entire reason this subsystem exists.

---

## 4. Open risks

- **Dump-load thermal matching is approximate.** Cavity copper and a resistive termination have different thermal masses and radiation patterns; "identical heat, same place" is a design target, never perfect. Residual differential heating is the leading remaining artifact — quantify it with sensors 3–4 and 9 and bound it.
- **Lock-in oscillator + detector thermal coefficients.** Precision-force work shows the lock-in's own reference oscillator (~0.05 ppm/°C) and detector gain drift become limiting once the big effects are gone. Temperature-stabilize or periodically recalibrate the electronics rack.
- **Dither self-heating modulation.** The frequency dither slightly modulates stored energy (hence heating) at the dither frequency; keep dither amplitude ≪ linewidth and dither frequency well separated from both 0.02 Hz and the balance mechanical resonance.
- **Fiber-probe strain/temperature cross-talk (FBG).** If FBGs are used on the moving cavity, mechanical strain during thermal expansion corrupts the temperature reading — use fluorescence probes or strain-relieved FBG packaging.
- **Q drift with temperature** changes the stored-energy-vs-power relation even when on-resonance and at constant power; monitor Q (linewidth from the reflected dip) continuously as a third slow channel, not a one-time calibration.
- **PA phase-noise / settling** on the SynthHD/ADF4351 during fast dump-load switching could momentarily unlock; verify the servo re-acquires within one modulation phase.
- **PT100 fragility under vibration/pumping** — 1/10-DIN elements are delicate; strain-relief the leads.

---

## 5. Sources (URLs)

- High-accuracy EMDrive thrust measurements & false-positive elimination (Tajmar/TU-Dresden, CEAS Space J. 2022): https://link.springer.com/article/10.1007/s12567-021-00385-1
- EmDrive overview + thermal COM-shift artifact consensus: https://en.m.wikipedia.org/wiki/EmDrive
- PDH locking, undergraduate VCO/RF treatment (inc. dither equivalence): https://arxiv.org/pdf/1108.0960
- PDH-style lock tracking a thermally drifting high-Q microwave/dielectric resonator: https://arxiv.org/pdf/2511.11561
- Multi-tone microwave frequency locking to a noisy cavity via real-time feedback: https://arxiv.org/html/2304.06296v2
- PDH review (Nickerson): https://papers.nickersonm.com/2008-12-20%20-%20PDH%20Locking%20Review.pdf
- Dither-locking as simpler low-freq PDH (Caltech Ph77 PDH lab): http://pmaweb.caltech.edu/~ph77/labs/optics/pdh.pdf
- ADF4351 datasheet / product (Analog Devices): https://www.analog.com/en/products/adf4351.html
- ADF4351 signal-source module (retail): https://www.amazon.com/35M-4-4GHz-Frequency-Synthesizer-Development-Generator/dp/B078NRD8V6
- Mini-Circuits directional couplers (ZUDC10-183+): https://www.minicircuits.com/WebStore/dashboard.html?model=ZUDC10-183+
- Pasternack SMA circulators (1–26.5 GHz): https://www.pasternack.com/sma-circulators-category.aspx
- PT100 RTD vs thermocouple accuracy/stability: https://www.tcdirect.co.uk/pt100-sensor/rtd-vs-thermocouple.aspx
- Omega DP9602 precision RTD thermometer (0.01/0.001 °C): https://www.omega.co.uk/pptst/DP9602.html
- MicroEdge multi-channel RTD logger: https://www.microedgeinstruments.com/lrtd.php
- Fiber-optic vs thermocouple temperature sensing in microwave/RF fields: https://www.fjinno.net/microwave-temperature-sensors-fiber-optic-vs-thermocouple/
- Fiber-optical thermometer (fluorescence/FBG background): https://en.wikipedia.org/wiki/Fiber-optical_thermometer
- Lock-in detection principles (drift/DC-offset immunity): https://www.zhinst.com/en/resources/principles-of-lock-in-detection/
- SR830-based precision force metrology (thermal oscillator-drift limits): https://arxiv.org/pdf/2403.10998
