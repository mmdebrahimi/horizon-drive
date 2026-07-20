# Subsystem Optimization Memo — EM Shielding + DAQ / Software Lock-In

**Project:** Horizon-drive Phase-1 decisive experiment (DETECT-OR-NULL ~12 µN anomalous thrust; room-temp Cu cavity, ~10–15 W RF @ 1.836 GHz, torsion balance)
**Subsystem owner scope:** magnetic shielding · feed-lead / feedthrough treatment · grounding · modulation microcontroller · software lock-in · blinding
**Date:** 2026-07-20
**Enemy:** FALSE POSITIVES — chiefly the feed-current × ambient-B force (F = I L×B) that mimics thrust, plus experimenter bias.

---

## 1. Overview

The dominant published false positive for exactly this class of experiment is **not** subtle physics — it is the **drive current in the feed leads interacting with Earth's / ambient magnetic field**. Tajmar's SpaceDrive group at TU Dresden traced the entire apparent EmDrive "thrust" to this mechanism (partially shielded cables × Earth's field) plus thermal drift, and their high-accuracy campaign refuted the claims by ≥3 orders of magnitude. That is the prior we design against.

This subsystem attacks the artifact on **four independent axes** so no single failure produces a false detection:

1. **Reduce ambient B at the balance** → mu-metal enclosure (shrinks the B in F = I L×B).
2. **Reduce the current loop area / net force** → twisted + shielded feed leads (differential-mode field cancellation) + feedthrough π-filters.
3. **Remove ground-loop currents** → single-point / star ground so stray currents don't flow through the balance structure.
4. **Discriminate signal from artifact by symmetry** → software lock-in at the modulation frequency + **polarity/orientation reversal tests** + blinded scheduling.

The core measurement chain is deliberately cheap and reproducible: laser → mirror on balance → **PSD/quadrant photodiode** → **24-bit DAQ** → microcontroller square-waves RF on/off at ~0.02 Hz → **Python/NumPy software lock-in** demodulates displacement at the modulation frequency. No hardware lock-in needed.

---

## 2. Optimized Component List (parts / rough prices, USD)

### 2a. Magnetic shielding
| Item | Spec / use | Vendor | ~Price |
|---|---|---|---|
| MuMETAL® sheet 12"×8", 0.062" analog gauges | Enclosure walls around balance (ASTM A753 Alloy 4) | Magnetic Shield Corp via DigiKey (MU004-8 / MU006-8 / MU008-8) | $49–$61 / sheet |
| MuMETAL® foil, 0.004–0.008" adhesive-backed | Wrap feed-lead runs, patch seams, line gaps | Magnetic Shield Corp / Aircraft Spruce (by the inch) | ~$40–120 / roll segment |
| Flat-rate shipping (Magnetic Shield Corp via DigiKey) | — | — | $45 flat |
| **Fabrication note** | Foil sold **stress-annealed for forming**; give a **final magnetic anneal after cutting/bending** or you lose most permeability | — | — |
| Enclosure budget (multi-sheet 2-layer nested box) | Two nested mu-metal layers > one thick layer for shielding factor | — | **~$300–600** |

Design note: mu-metal shields **low-frequency / DC magnetic fields** (Earth's field). It does *not* shield the RF; it shields the ambient B that the feed current couples into. Nested double-layer beats single because shielding factors roughly multiply. Leave the RF cavity's own field path unobstructed — you're shielding the *balance and leads*, not the cavity output.

### 2b. Feed leads + feedthrough filtering
| Item | Spec / use | ~Price |
|---|---|---|
| Shielded twisted pair (STP) for RF-supply DC/bias + sense lines | Twist cancels differential-mode I L×B loop; shield handles E-field/HF | $1–3 / ft |
| Coax (RG-402 / semi-rigid or good RG-58) for the 1.836 GHz drive | Coax return current is coaxial → **near-zero net external loop area** (biggest single artifact win for the RF conductor itself) | $2–8 / ft |
| Feedthrough / π-filter capacitors at bulkhead (e.g. Tusonix / API-style) | Mount at metal wall, bare-metal contact, shunt conducted EMI to chassis | $5–20 each |
| Common-mode choke on supply pair | Attenuate common-mode current | $3–10 |

Rule: **the RF drive current must return coaxially** (coax, not two spaced wires). A spaced pair carrying the drive current is the exact I L×B loop that faked EmDrive thrust. Where a pair is unavoidable (DC/bias/sense), twist it tightly and keep the loop area minimal.

### 2c. Grounding / isolation
- **Single-point (star) ground** at the vacuum/bulkhead flange — one defined reference node; insulate balance structure so no stray current path runs through the moving element. Real UHV/cryostat and ProtoDUNE builds use exactly this (single-point feedthrough grounding, frames insulated from each other).
- Ground cable **shields at the source end** at low frequency; transition to both-ends grounding **only** above ~100 kHz / when cable > λ/20, using short (<5 cm) straps to avoid new loop antennas. For DC/audio-band sense wiring, single-end.
- Bulkhead contact must be **bare metal** (strip paint/anodize under the filter/clamp).
- **Optically isolate** the DAQ/logging PC from the balance electronics where possible (USB isolator ~$40, or run the photodiode preamp battery-powered) to break the mains ground loop.

### 2d. Displacement readout
| Option | Spec | Vendor | ~Price |
|---|---|---|---|
| **Thorlabs PDP90A** lateral-effect PSD module | 9×9 mm active, 320–1100 nm, 15 kHz BW, ±4 V out, integrated transimpedance — turnkey | Thorlabs | **~$493** |
| Quadrant / bi-cell photodiode | Highest sensitivity **at null**; best if you servo the beam to center (recommended for max thrust resolution) | Thorlabs / First Sensor | $150–400 + preamp |
| Bare Hamamatsu 1D PSD chip (e.g. S8158) + DIY transimpedance | Cheapest; you build electronics | Hamamatsu | ~$2.50 chip + parts |
| Laser diode + collimator (readout beam) | Reflect off balance mirror | Thorlabs | ~$50–150 |

Recommendation: **quadrant photodiode in a beam-centering (nulling) configuration** for best small-signal resolution; PDP90A if you want turnkey absolute position with linear range. Keep optical power adequate — PSD resolution degrades linearly with falling light; shield stray/background light (it averages irreducibly into a lateral PSD).

### 2e. DAQ + modulation microcontroller
| Item | Spec / use | ~Price |
|---|---|---|
| **LabJack U6-Pro** USB DAQ | 24-bit sigma-delta (~22 effective / 20 noise-free bits at slow speed), programmable gain ×1/×10/×100 for small photodiode signals, ±10 V, differential inputs — plug-and-play, low drift | ~$599 |
| Budget alt: Raspberry Pi + **ADS1262/1263** 32-bit ADC board | 0.16 µVpp noise, 1 nV/°C drift — lab-grade at ~$100 total | ~$100 |
| Modulation controller: **Arduino Uno / Nano** (or Pi GPIO) | Square-waves RF **on/off at ~0.02 Hz** (25 s on / 25 s off) via relay/PIN-diode/RF switch; emits the phase-reference timestamp/TTL that the software lock-in uses | ~$10–30 |
| RF on/off switch controlled by MCU | GaAs RF switch or drive the source's TTL blanking input; **do not** hot-switch by mechanically moving leads (creates artifacts) | $20–80 |

Timing rule: use an **interval timer**, not `sleep()`, for the modulation and logging cadence — jitter degrades the lock-in. Log **timestamp, RF-state (0/1), photodiode/PSD position, and any B-field monitor** every sample. Add a **3-axis magnetometer** (e.g. a cheap fluxgate or an QMC/HMC-class board, ~$15–200) logging ambient B as a covariate — lets you correlate any residual signal against field, the smoking gun for an artifact.

**Rough subsystem total:** ~$1,200–1,800 (mu-metal ~$400, PSD/optics ~$500, LabJack U6-Pro ~$600, MCU + RF switch + filters + magnetometer ~$150–250). Budget variant with Pi+ADS1263 and DIY PSD: **~$600–800**.

---

## 3. The Single Null-Test-Critical Optimization

> **Make the drive-current path magnetically symmetric AND reversible, then let the software lock-in + polarity-reversal exploit the symmetry difference between a real thrust and an EM artifact.**

Concretely, the one optimization that most separates true thrust from the dominant false positive:

**Route the RF drive current coaxially (zero net external loop) and add a mechanical/electrical means to REVERSE current polarity and to ROTATE the cavity 180° in the balance frame — without changing anything else.** Then:

- A **real thrust** is fixed in the **cavity frame**: it keeps the same sign under current-polarity reversal and **flips sign when you rotate the cavity 180°** (this is Tajmar's rotate-to-null discriminator).
- An **I L×B artifact** is fixed in the **lab frame / current direction**: it **flips sign when you reverse current polarity** and tracks the ambient-B orientation, largely **indifferent to cavity rotation** except as the lead geometry changes.

The lock-in gives you a **signed, phase-resolved amplitude** at 0.02 Hz for each configuration. Cross the two reversals (current polarity × cavity orientation) into a 2×2 table; only a signal that behaves as "fixed in cavity frame, invariant to current polarity, flips under 180° rotation" survives as a candidate thrust. Everything else is EM/thermal artifact. This is cheap (coax + a rotation stage + a polarity switch) and is the exact methodology that let SpaceDrive kill the EmDrive claim. **Buy the coax and the rotation capability before anything else.**

---

## 4. Software Lock-In + Blinding Approach

### 4a. Software lock-in (phase-sensitive detection)
Modulate RF on/off at **f_mod ≈ 0.02 Hz**; the anomalous thrust (if real) appears as a square-wave-correlated displacement at f_mod, riding on top of slow thermal/seismic drift. Software lock-in pulls it out:

1. **Acquire** position `x[n]` and RF-state at fixed Δt (interval-timed) — block-wise via NumPy for efficiency (`nidaqmx` / LabJack stream or timed reads).
2. **Build references** at f_mod from the MCU's phase clock: `ref_I = sign(sin(2π f_mod t))` (in-phase, matches the square drive) and `ref_Q = sign(cos(2π f_mod t))` (quadrature).
3. **Mix**: `mI = x * ref_I`, `mQ = x * ref_Q`.
4. **Low-pass** far below f_mod (e.g. Butterworth, cutoff ~f_mod/10 ≈ 0.002 Hz, SciPy `butter`+`filtfilt`) → slow `X`, `Y`.
5. **Amplitude/phase**: `R = hypot(X, Y)`, `θ = arctan2(Y, X)`. A genuine on/off thrust sits at the **expected phase**; noise/artifacts land at random or wrong phase.

```python
import numpy as np
from scipy.signal import butter, filtfilt

def software_lockin(t, x, f_mod, lp_cut=None):
    # square-wave references locked to the modulation clock
    ref_i = np.sign(np.sin(2*np.pi*f_mod*t))
    ref_q = np.sign(np.cos(2*np.pi*f_mod*t))
    mi, mq = x*ref_i, x*ref_q
    fs = 1.0/np.median(np.diff(t))
    lp_cut = lp_cut or f_mod/10.0
    b, a = butter(4, lp_cut/(fs/2))
    X, Y = filtfilt(b, a, mi), filtfilt(b, a, mq)
    R = np.hypot(X, Y)          # demodulated amplitude
    theta = np.arctan2(Y, X)    # phase vs. drive
    return X, Y, R, theta
```

Notes: a **square-wave reference recovers only the fundamental Fourier component** — fine here (we want the f_mod component), but keep it in mind for calibration scaling. Report the **signed in-phase X** (calibrated to force via the balance's known torsion constant / EM calibration) as the thrust estimate; the quadrature Y and off-phase power are your artifact/noise diagnostics. Log ambient B alongside and regress X on B — nonzero coupling ⇒ artifact.

### 4b. Blinding / randomized scheduling (bias defense)
Experimenter bias is the second enemy; blind analysis is the traceable cure (Klein & Roodman 2005; nEDM/PSI; J-PARC hidden-offset method).

- **Randomized on/off schedule**: instead of a fixed 25 s/25 s pattern, have the MCU draw the on/off block sequence from a **seeded PRNG** (still ~0.02 Hz average) so the analyst can't unconsciously time-align to expectations. Store the seed sealed.
- **Hidden-offset blinding**: apply an **unknown additive offset** (and/or unknown sign flip) to the demodulated thrust estimate `X` during analysis. Fix all cuts, filters, calibration, and artifact-rejection thresholds **before** unblinding. Encrypt the offset (password-sealed), reveal only after the pipeline is frozen — mirrors the J-PARC secret-frequency-offset and nEDM re-blinding practice.
- **Label-blind runs**: record which configuration (RF-on vs sham, polarity +/−, orientation 0°/180°) under coded labels; the person running the lock-in sees only codes until analysis is locked. Prevents cut-tuning until a "desired" result appears.
- **Pre-register** the decision rule (e.g. "detection = in-phase X at expected phase, ≥5σ, that survives all four symmetry reversals and shows no B-correlation") before touching data.

---

## 5. Open Risks

1. **Mu-metal saturation / handling** — mechanical shock, bending after anneal, or nearby strong magnets ruin permeability. Anneal after fabrication; keep magnets away; re-degauss periodically.
2. **Mu-metal doesn't help at all if the artifact is thermal or from the lead loop geometry** — shielding reduces B but the residual loop-area × residual-B force can still fake thrust. The coax + reversal tests, not the shield, are the real defense.
3. **Square-wave harmonics + slow drift aliasing** — at 0.02 Hz, thermal transients from RF heating share the band; the on/off thermal expansion of the cavity/mount can be *in-phase* with the drive and directly mimic thrust. Mitigate with sham-load runs (resistive dummy load dissipating equal power, no cavity resonance) and thermal monitoring.
4. **PSD/laser pointing drift** — laser wavelength/thermal pointing drift shows up as position drift; stabilize laser, keep it outside the RF-heated zone, and let the lock-in reject out-of-band drift.
5. **Ground-loop reintroduced by the DAQ PC** — USB/mains ground can re-couple current through the balance; verify with the isolator in/out.
6. **Timing jitter** in cheap MCU/DAQ degrades lock-in phase resolution — use hardware/interval timing, log actual timestamps not assumed cadence.
7. **Under-powered readout light** — PSD resolution degrades linearly with falling optical power; budget enough laser power and block stray light.
8. **Blinding leakage** — real-time plots that reveal the answer defeat blinding; the live display must show only blinded/coded quantities.

---

## 6. Sources (URLs)

- Magnetic Shield Corp — MuMETAL® foil/sheet specs: https://www.magnetic-shield.com/mumetal-perfection-annealed-foil/ · https://www.magnetic-shield.com/mumetal/
- DigiKey MuMETAL® sheet listing (pricing, $45 flat ship): https://www.digikey.com/en/products/detail/magnetic-shield-corporation/MU012-8/13160831
- Aircraft Spruce mu-metal foil (by the inch): https://www.aircraftspruce.com/catalog/elpages/edmomumetal.php
- Magnetic Shields Ltd (UK) — foil, stress-anneal-then-final-anneal note: https://mumetalfoil.co.uk/
- Tajmar / SpaceDrive — high-accuracy EmDrive test + Earth-field/cable false-positive elimination + 180° rotate-to-null: https://link.springer.com/article/10.1007/s12567-021-00385-1 · https://www.researchgate.net/publication/328134095_The_SpaceDrive_Project-Thrust_Balance_Development_and_New_Measurements_of_the_Mach-Effect_and_EMDrive_Thrusters
- Thorlabs PDP90A lateral-effect PSD module (~$493): https://www.thorlabs.com/position-sensing-detectors
- Hamamatsu PSD selection guide / bare chips: https://www.hamamatsu.com/us/en/product/optical-sensors/distance-position-sensor/psd.html
- LabJack U6-Pro (24-bit, effective-bits candor, timing/jitter): https://labjack.com/products/labjack-u6-pro · https://labjack.com/pages/frequently-asked-questions
- Low-cost Raspberry Pi + ADS1262/1263 32-bit DAQ (~$100, low drift): https://pmc.ncbi.nlm.nih.gov/articles/PMC9215268/
- Microcontroller ADC noise caveats (ESP32/Pico/Arduino): http://www.doctormonk.com/2024/01/comparingadcs.html
- Software-defined lock-in demodulator, low-frequency, NumPy/SciPy: https://arxiv.org/html/2412.00093v1
- Digital lock-in principle (mix + low-pass, I/Q): https://ethz.ch/content/dam/ethz/special-interest/phys/quantum-electronics/tiqi-dam/documents/semester_theses/semesterthesis-christoph_fischer.pdf
- Open-source Python real-time lock-in (GitHub topic): https://github.com/topics/lock-in-amplifier
- Twisted-pair / feedthrough-filter / single-point-ground EMI practice: https://octopart.com/pulse/p/feedthrough-and-common-mode-chokes-suppress-high-frequency-emi · https://picwire.com/Resources/Technical/Technical-Articles/Grounding-Wires-Cables
- ProtoDUNE single-point feedthrough grounding (star-ground reference): https://arxiv.org/pdf/1706.07081
- Blind analysis — Klein & Roodman review: https://www.slac.stanford.edu/pubs/slacpubs/12000/slac-pub-12051.pdf
- Data blinding, nEDM/PSI (re-blinding algorithm): https://arxiv.org/pdf/1912.09244
- Hidden-offset blinding (J-PARC precision measurement): https://arxiv.org/pdf/2501.02736
