# RF Power Chain — Component-Level Optimization Memo

**Subsystem:** RF power chain for the horizon-drive Phase-1 decisive experiment
**Cavity under test:** room-temp copper truncated-cone, TM010 ≈ 1.836 GHz, Q₀ ≈ 27,000, drive 10–15 W
**Predicted Phase-1 signal:** ≈ 12 µN
**Optimization priority (this task):** MEASUREMENT QUALITY first; cost noted but secondary
**Date:** 2026-07-20

---

## Overview

The RF chain's job is not "make 15 W at 1.84 GHz." It is to deliver a **known, traceable, constant DISSIPATED power** into the cavity while the drive stays parked on a thermally drifting resonance — and to do so in a way that does **not** create the very thermal/EM false-positives that killed EmDrive/Eagleworks. Two chain-level requirements dominate every component choice:

1. **F ∝ Q discriminator** requires that we can *vary Q at fixed dissipated power*. Dissipated power is not the amplifier's forward power; it is `P_diss = P_fwd − P_refl − P_trans`. The chain must therefore measure forward and reflected power to good absolute accuracy and let us servo the source so `P_diss` is held constant as Q is deliberately changed (coupling change, lossy insert, wall treatment). Thrust must then track Q linearly at constant `P_diss`; if it tracks *forward power* or *temperature* instead, it is an artifact.

2. **Null-test invariance of deposited heat.** Off-resonance the cavity reflects nearly all forward power; on-resonance it absorbs it. If that swing in "where the heat goes" lands on the thrust balance, thermal drift perfectly mimics an on/off-resonance thrust. The chain must route reflected power to a **fixed, off-balance thermal sink** so the balance sees the same heat load regardless of resonance state. (Expanded in "The single null-test-critical optimization.")

Chain topology (source → load):

```
[OCXO 10 MHz]──ref──►[Valon 5015 synth]──►[LPF/BPF]──►[GaN/GaAs PA 10–15 W]──►[isolator]──►
   ▲ EFC/servo                                                                   │
   │                                                          [dual-directional coupler]
   │                                                             │fwd        │refl
   │                                                        [pwr sensor]  [pwr sensor]
   │                                                                              │
[PID / inverse-PDH servo]◄──[mixer / lock-in]◄──[Schottky det]◄──[circulator port-2 reflect]
                                                                              │port-3
                                                                     [FIXED thermal dump load]
                                                                     (off-balance, heat-sinked)
```

---

## Optimized component list (vendor / model / price)

| # | Function | Vendor / Model | Rough price | Why chosen (measurement-quality rationale) |
|---|----------|----------------|-------------|--------------------------------------------|
| 1 | Signal source (phase-lockable synth) | **Valon 5015**, 10 MHz–15 GHz | **$1,795 new** | Multi-loop PLL → low phase noise + low spurs; calibrated output +13→−30 dBm in 0.1 dB steps; accepts external 10 MHz ref; has a **±3 V external EFC input** that we hijack as the analog servo actuator for the inverse-PDH lock. |
| 1b | Low-cost source alternative | **SV1AFN ADF4351 module** + Arduino/`siggen4351` fw | ~$60–120 | Covers 1.84 GHz (3.68 GHz VCO ÷2), locks to ext 10 MHz. Higher phase noise / spurs than Valon — acceptable for first-light, **not** for the final quality run. |
| 2 | Frequency reference | Surplus **OCXO 10 MHz** (Symmetricom/HP 10811-class) | ~$40–150 used (eBay) | Close-in phase-noise + drift of the whole chain is set here. Distributes as the lab 10 MHz standard and also feeds the power-sensor timebase. Valon accepts 5–100 MHz ext ref. |
| 3 | Harmonic/spurious filter (post-synth, low level) | **Mini-Circuits VLF-2000+** LPF (or SLP-1900) | ~$40 | Cleans synth harmonics before amplification so the PA is not asked to amplify a 2nd harmonic. Note VLF-1800+ cutoff (passband edge 1800 MHz) is **marginal at 1.836 GHz** — step up to VLF-2000+ so 1.836 GHz sits inside the passband. |
| 4 | Power amplifier (~10–15 W) | **Mini-Circuits ZHL-10W-2G+**, connectorized SMA, 800–2000 MHz, 10 W, 50 Ω | ~$1,800–2,100 new | Turnkey connectorized linear PA covering 1.836 GHz; internal bias/match; robust. **Caveat: this class is GaAs, not GaN.** GaN alternatives (RFHIC / Fairview / Qorvo eval modules at 1.8 GHz) exist but cost more and add integration; GaN's advantage (efficiency/ruggedness) is not measurement-critical here since we run well backed-off. |
| 4b | GaN alternative | Qorvo/Wolfspeed 1.8 GHz GaN eval board or **RFHIC RRP184xx** module | ~$400–1,500 | Consider only if thermal/DC efficiency of the PA bench becomes a lab-heat problem. |
| 5 | Harmonic filter (post-PA, high level) | **Mini-Circuits VLF-2000+ (10 W)** or a **cavity/interdigital BPF @1.84 GHz** | ~$40 (LPF) / ~$150–400 (BPF) | Suppresses PA-generated 2nd/3rd harmonic before the coupler/cavity so harmonic power cannot masquerade as absorbed fundamental in the `P_diss` accounting. A narrow BPF is better (rejects both harmonics and any broadband PA noise) but adds insertion loss to calibrate out. Must be rated for full forward power. |
| 6 | Isolator (protect PA) | **DiTom D3I1719** (or UIY/JQL) coaxial isolator, 1.7–1.9 GHz, N-type, ≥20 W | ~$150–300 | Protects the PA from cavity reflection and keeps PA load-pull from changing forward power as Q/detuning changes — **critical for holding forward power constant**. Integral or external matched load absorbs reflection. |
| 7 | Circulator + dump (reflection routing) | **DiTom D3C1719** 3-port circulator, 1.7–1.9 GHz, N, ≥20 W | ~$150–350 | Port-1 in, port-2 to cavity, port-3 to the fixed thermal dump. This is the component that makes the null-test-critical routing possible (see below). Can be the same device as #6 if a circulator is used with an external load. |
| 8 | Matched dump load (fixed thermal sink) | **Bird 8329-300 / Termaline 50 W** dry termination, N-type, on a large finned heatsink **bolted to the optical table, off the balance** | ~$50–150 used | The reflected-power heat sink. Thermally massive + thermally isolated from the cavity/balance. Oversized (≥50 W for a 15 W chain) so its temperature barely moves. |
| 9 | Directional coupler (fwd/refl metrology) | **Mini-Circuits ZGBDC30-372HP+**, dual/bi-directional, 380–3700 MHz, 30 dB | ~$300–400 | Simultaneous forward + reflected sampling with good directivity. 30 dB coupling drops 15 W (+41.8 dBm) to ~+11.8 dBm — inside the power sensors' range. Directivity sets how cleanly reflected is separated from forward — **directivity error propagates directly into `P_diss` uncertainty**, so directivity (not just coupling flatness) is the spec to hold. |
| 10 | Forward power sensor | **LadyBug LB5908A** true-RMS, 1 MHz–8 GHz, NIST-traceable | ~$1,600–2,000 | True-RMS diode sensor, NoZero/NoCal, explicit NIST traceability. Absolute accuracy here is what makes `P_diss` and therefore F∝Q defensible. |
| 11 | Reflected power sensor | **LadyBug LB5908A** (second unit) or **Mini-Circuits PWR-6LRMS-RC** | ~$700–2,000 | Second matched sensor on the reflected coupled port. Ideally **identical model to #10** so systematic calibration offsets cancel in `P_fwd − P_refl`. |
| 12 | PLL / inverse-PDH servo | **Red Pitaya STEMlab 125-14** (digital lock-in + PID, PyRPL) + a low-freq **phase modulator** or synth FM, + **zero-bias Schottky detector** (e.g. Herotek DZR124AA) | ~$300–500 (RP) + ~$100 (Schottky) | Phase-modulate the drive, detect the cavity reflection, demodulate to a dispersion-shaped error signal that zero-crosses at resonance, PID → Valon EFC. Discriminator slope ∝ Q, so lock tightens as Q rises. Red Pitaya gives digital lock-in + servo in one box. |
| 13 | Cabling / adapters | Phase-stable coax (e.g. Mini-Circuits/Junkosha), N and SMA | ~$150 | Phase-stable runs on the reflection path so the demod phase (and thus the error-signal zero) doesn't drift with room temperature. |

**Indicative subtotal (quality build):** ~$7,000–9,000 new; ~$4,000–5,000 leaning on surplus PA/sensors/OCXO.

---

## The single null-test-critical optimization

**Route ALL reflected power to a fixed, off-balance, thermally-massive dump load via the circulator, so the heat deposited on the thrust balance is invariant to resonance state.**

Why this is *the* one that matters:

- The PA delivers essentially constant forward power `P_fwd`. What changes between on- and off-resonance is **where that power ends up**: on-resonance it is dissipated in the copper cavity walls (on the balance); off-resonance ~all of it reflects. If that reflected power were dumped anywhere thermally coupled to the balance, then switching on/off resonance would swing the balance's total heat load by up to the full ~15 W — producing a thermal-expansion / radiometric deflection **exactly correlated with the resonance state we are modulating**. That is the canonical EmDrive/Eagleworks false positive.
- The circulator (#7) sends the cavity reflection to port-3 → a dump load (#8) that is (a) **off the balance**, bolted to the table/heatsink, and (b) **oversized** so its own ΔT is negligible. Now the balance's thermal environment is the same whether we are on or off resonance except for the *genuine* wall dissipation — which is the thing we are deliberately holding constant for the F∝Q sweep.
- This dovetails with the discriminator: because forward power is held constant by the isolator (#6) preventing load-pull, and reflected power is measured (#9–#11) and sunk to a fixed place, the **net dissipated power `P_diss = P_fwd − P_refl`** is both *known* and *deposited in a controlled location*. To vary Q at fixed `P_diss`, we change coupling/loss and trim `P_fwd` on the Valon until the measured `P_fwd − P_refl` returns to setpoint. Thrust must then scale linearly with Q at fixed `P_diss`; the symmetric pillbox null-control, driven through the identical chain to the identical dump, must read zero.

Secondary but supporting: keep the dump load's thermal time constant *long* and its placement *symmetric* between the real-cavity and pillbox-null configurations, so any residual thermal coupling is common-mode and subtracts in the null comparison.

---

## Open risks / unknowns

1. **GaAs vs GaN PA:** the clean turnkey option (ZHL-10W-2G+) is GaAs. Need to confirm harmonic/IMD spectrum and that running ~3–6 dB backed off keeps 2nd-harmonic ≥ 40–50 dBc *before* the post-PA filter, else the harmonic filter (#5) must do more work and its insertion loss must be calibrated into `P_fwd`.
2. **Coupler directivity → `P_diss` error budget.** Need the ZGBDC30-372HP+ directivity *at 1.836 GHz* (datasheet, not band-typical). Finite directivity leaks forward into the reflected reading; near critical coupling (small `P_refl`) this dominates the `P_diss` uncertainty. May need a directivity calibration (sliding-load / offset-short) or a higher-directivity lab coupler.
3. **Absolute power traceability chain not yet closed.** Two LadyBug sensors give NIST-traceable *readings*, but the quantity we need is dissipated power *at the cavity port* — so coupler coupling factor, cable loss, and connector repeatability between the sensor plane and cavity plane must be characterized and held stable across the Q sweep. A VNA S-parameter de-embed of the coupler→cavity section is the honest way.
4. **Valon EFC as servo actuator:** need to verify EFC tuning slope (Hz/V), linearity, and bandwidth are adequate to track thermal drift of a Q≈27,000 resonance (linewidth ≈ 68 kHz). If EFC is too coarse/slow, drive the synth digitally over its control interface from the Red Pitaya instead.
5. **Phase-noise → effective Q / stored-energy jitter:** synth phase noise within the cavity linewidth modulates stored energy and thus any real thrust. Valon multi-loop + OCXO ref should suffice, but this needs a quantitative budget vs the 68 kHz linewidth.
6. **Reflected-path phase drift moving the lock point:** the demod phase sets where the error signal zero-crosses; thermal drift of the reflection-path cable can pull the lock slightly off true resonance, changing `P_diss`. Phase-stable coax + periodic re-zero of the discriminator mitigates; quantify residual.
7. **Circulator isolation vs power:** confirm the DiTom/UIY circulator's port-3 isolation and load VSWR hold at full 15 W so reflected power actually lands in the dump and not back at the cavity/PA.
8. **Common-mode guarantee for the null run:** the pillbox null must traverse a *bit-identical* chain (same PA drive, same dump). Any asymmetry (different cable, different dump placement) reintroduces a differential thermal signal. Mechanical/thermal symmetry of the two configs is an open build detail.

---

## Sources (URLs)

- Mini-Circuits ZHL-10W-2G+ (800–2000 MHz, 10 W connectorized PA): https://www.minicircuits.com/WebStore/dashboard.html?model=ZHL-10W-2G%2B
- Mini-Circuits GaAs/GaN PA eval-board bench setup (AN-60-149): https://blog.minicircuits.com/power-amplifier-testing/
- Valon 5015 synthesizer (specs, ext ref, EFC, $1,795): https://www.valonrf.com/5015-frequency-synthesizer-15ghz.html
- Valon 5015 launch details (price, external-reference note): https://zingpr.com/news/2018/9/8/valontechnology5015
- ADF4351 synthesizer datasheet / product info: https://www.analog.com/en/products/adf4351.html
- SV1AFN ADF4351 module + siggen4351 firmware: https://github.com/dfannin/siggen4351
- Mini-Circuits ZGBDC30-372HP+ bi-directional coupler (380–3700 MHz, 30 dB): https://www.minicircuits.com/WebStore/dashboard.html?model=ZGBDC30-372HP+
- Mini-Circuits ZDDC dual-directional coupler datasheet: https://www.minicircuits.com/pdfs/ZDDC20-K1844+.pdf
- Directional coupler operation/application (Mini-Circuits blog): https://blog.minicircuits.com/directional-couplers-their-operation-and-application/
- LadyBug LB5908A true-RMS NIST-traceable USB power sensor: https://www.ladybug-tech.com/product/the-lb5908a-1-mhz-to-8-ghz-true-rms-power-sensor/
- LadyBug NIST-traceability + true-RMS FAQ: https://www.ladybug-tech.com/faq/
- Mini-Circuits PWR-6LRMS-RC true-RMS USB/Ethernet sensor: https://www.minicircuits.com/pdfs/PWR-6LRMS-RC.pdf
- Mini-Circuits PWR-6GHS USB power sensor (CW, calibration/recal cost): https://www.minicircuits.com/pdfs/PWR-6GHS.pdf
- Coaxial isolators/circulators (DORADO, 800 MHz–40 GHz, N-type option): https://www.dorado-intl.com/wp-content/uploads/2017/10/Coaxial.pdf
- UIY coaxial circulators (10 MHz–50 GHz, N/SMA): https://www.uiyinc.com/Coaxial_Circulator/
- JQL coaxial RF circulators (100 MHz–40 GHz): https://www.jqlelectronics.com/product-category/rf-circulator/coaxial/
- Mini-Circuits VLF-1800+ LPF (cutoff 2.125 GHz, 10 W, harmonic rejection): https://www.minicircuits.com/WebStore/dashboard.html?model=VLF-1800
- Inverse Pound-Drever-Hall locking of a drive to a noisy microwave cavity (2023): https://arxiv.org/html/2304.06296
- PDH locking with Red Pitaya (digital lock-in/servo implementation): https://content.redpitaya.com/blog/pound-drever-hall-locking-opo-red-pitaya
- Pound reflection-locking of high-Q microwave (axion) cavities (FNAL workshop): https://indico.fnal.gov/event/13068/contributions/17087/
