# Engineering Roadmap — Quantised-Inertia / Horizon-Drive Test-and-Development Platform

> Captured 2026-07-04. Detailed build roadmap for a device to test, characterize, and (only if the physics survives) scale the inertia-manipulation / horizon-drive effect. Engineering numbers verified `/tmp/eng.py`. Companion to `antigravity-decisive-test-design-spec-2026-07-04.md` (the noise-budget) and the Medium draft.

---

## 0. Honest premise — what you are actually building

You cannot build a "working anti-gravity device" today, because **the effect is unconfirmed** — every clean, well-isolated test to date (Tajmar/Dresden) has returned null. Therefore the only rational thing to *build first* is the **instrument that settles it**: a nano-newton-resolution, artifact-immune thrust apparatus wrapped around a tunable high-Q resonator. That instrument is a real, buildable, valuable piece of engineering regardless of the outcome — if it sees nothing, that's a publishable null that tightens the bound; if it sees a signal that survives every control *and scales with Q*, you have the most important physics result in a century and a defined path to a thruster.

So this roadmap is a **staged development program with kill-gates**, not a blueprint for a flying car. The single most important number, from the calibrated model $F \approx \eta P Q/c$ (η ≈ 0.007), is this:

| Phase | Cavity | Power | Q | **Predicted thrust** | vs 0.33 µN photon floor |
|---|---|---:|---:|---:|---|
| 2 | copper | 100 W | 10⁴ | **24 µN** | 70× — measurable if real |
| 2+ | high-Q copper | 100 W | 10⁵ | **240 µN** | 700× |
| 3 | superconducting Nb | 100 W | 10¹⁰ | **~24 N** | ~10⁸× — *impossible to miss* |

That last row is the entire gamble in one line: **if** the effect is real **and** its thrust truly scales with Q, a superconducting cavity would produce tens of newtons — trivially measurable. The fact that nobody has ever seen this at high Q is either because the effect is false, or because nobody has built the clean high-Q rig. **This program builds that rig.**

---

## 1. System architecture

```
                    ┌───────────────────────  UHV CHAMBER (≤1e-8 Pa)  ───────────────────────┐
                    │                                                                          │
   RF SOURCE ──►  optical/twisted   ┌──────────── TORSION BALANCE ────────────┐                │
   (locked to     power feed        │   [counterweight]───fiber───[EMITTER]    │  ◄── interfero-│
    cavity f)     (no lead loop)     │                                RF cavity │      meter     │
        ▲                            │            calibration coil ►            │      readout   │
        │  VNA (Q,f)                 └──────────────────────────────────────────┘                │
        │                              inside: MU-METAL shield + thermal SHROUD                   │
   CONTROL/DAQ ◄── temps, field, power, position, Q/f ──────────────────────────────────────────┘
        │
   PROTOCOL ENGINE: orientation-flip · dummy-load · Q-detune · power-mod lock-in · blind analysis
```

Six subsystems: **(A) resonator/emitter**, **(B) thrust balance/metrology**, **(C) vacuum**, **(D) thermal**, **(E) EMI/magnetics**, **(F) control/DAQ/protocol**. Each is specified below with the artifact it exists to defeat.

---

## 2. Subsystem specifications

### A — Resonator / emitter (the device under test)
- **Geometry:** truncated-cone (frustum) RF cavity — the EmDrive/McCulloch geometry, where the end-plate diameter asymmetry is the "manufactured horizon." Big-end Ø ~0.28 m, small-end Ø ~0.16 m, length ~0.23 m (tunable). *Rationale: McCulloch's thrust prediction depends on the (1 − w_small/w_big) taper term.*
- **Phase-2 material:** OFHC copper, electro-polished interior (surface finish drives Q). Target loaded Q ≈ 1×10⁴–10⁵.
- **Phase-3 material:** bulk niobium (RRR≥300), chemically polished + high-pressure rinsed (SRF recipe). Target Q₀ ≈ 10¹⁰ at 2–4 K.
- **RF drive:** 2.45 GHz (ISM band — cheap, licence-free) solid-state GaN amplifier, 10–200 W, or a phase-lockable magnetron. Solid-state preferred for phase/frequency control.
- **Frequency lock (critical):** the cavity resonance drifts with temperature; off-resonance = no stored energy = no thrust. Use a PLL or VNA-tracked feedback driving a **piezo end-plate tuner** to hold the drive on the loaded resonance. Continuously log f₀ and loaded Q via a VNA (S11/S21).
- **Coupling:** adjustable antenna/loop coupler to set Q_ext for critical coupling.
- **Instrumentation:** forward/reflected power (dual directional coupler), 3–4 RTDs on the cavity body.

### B — Thrust balance / metrology (measures the force)
- **Type:** **torsion balance** — the field standard for µN–nN thrust (Tajmar, NASA Eagleworks, Cavendish heritage). Emitter on one arm, mass-and-thermal-matched counterweight on the other.
- **Suspension:** tungsten torsion fiber, Ø 25 µm × 0.5 m (torsion constant κ ≈ **1.2×10⁻⁸ N·m/rad**, verified) — or a cross-flexure pivot for robustness. Arm length ~0.2 m.
- **Readout:** fiber (Michelson) **laser interferometer** or a multi-pass optical lever, ≤1 nm resolution. *Verified: at 1 nm / 0.2 m arm the readout-limited force resolution is ~10⁻¹⁶ N — i.e. the readout is nowhere near the limit; the floor is set by Brownian/seismic/drift noise at the ~1–30 nN level, matching Tajmar-class rigs.*
- **In-situ calibration:** an electrostatic comb or a calibrated coil-magnet actuator applies **known µN/nN forces** before/after every run — you never trust an uncalibrated balance.
- **Damping:** eddy-current (magnet-plate) damper to control the ~0.01 Hz pendulum mode; or active feedback (electrostatic) to run in force-rebalance mode.
- **Isolation:** the whole balance on a passive/active **vibration-isolation stack** (pneumatic or active piezo), on a massive granite/inertial block, ideally in a low-traffic basement (seismic is a real noise term at these levels).

### C — Vacuum system (kills outgassing + radiometric artifacts)
- **Chamber:** 304/316 stainless, ConFlat (CF) flanges, ~Ø0.5 m bell jar or cube, viewports for the interferometer.
- **Pumping train:** roughing (scroll) → **turbomolecular** pump → **ion pump + NEG** for the UHV base. Target **≤1×10⁻⁸ Pa**.
- **Bakeout:** heater jackets, 150–250 °C for 24–48 h to reach UHV. *Rationale: at 10⁻³ Pa outgassing gives ~0.6 µN of thrust — it must drop below the ~nN floor, which needs ≤10⁻⁸ Pa (verified).*
- **Feedthroughs:** UHV-rated RF (N-type on CF), electrical (for RTDs/cal-coil), and an optical window for power (see E).

### D — Thermal management (kills the #1 false-positive)
- **The trap:** the emitter dissipates power → asymmetric thermal expansion shifts its center of mass → the balance reads a *fake displacement*. **Verified: a 1 K asymmetric warm-up of a 0.1 m aluminium emitter shifts the CoM by ~2,300 nm — versus a real signal of ~1 nm. This is exactly the artifact that produced every historical false "thrust."**
- **Controls (all mandatory):**
  1. **Radiative thermal shroud** around the balance, actively temperature-controlled; hold ΔT < 0.05 K across the emitter (brings the artifact to ~115 nm — still large, so ↓).
  2. **Symmetric emitter design + symmetric heat routing** so any residual expansion is common-mode (no net CoM shift).
  3. **Thermal straps** carry waste heat to a controlled sink *off the balance's moment arm* (flexible, low-force copper braid or heat pipe crossing at the fiber axis).
  4. **Full thermal telemetry** (RTDs) → build and *subtract* a measured thermal-CoM-shift transfer function.
  5. The **dummy-load control** (subsystem F) is the ultimate thermal discriminator: same watts, no cavity.

### E — EMI / magnetics (kills the DOMINANT artifact)
- **The trap:** current in the power leads crossing Earth's field is a Lorentz force. **Verified: 10 A over 0.1 m in 50 µT = 50 µN — ~150× the photon floor, the single biggest artifact.**
- **Controls:**
  1. **Break the lead loop:** deliver drive power **optically** (laser-to-photovoltaic on the balance) or via **counter-wound/twisted bifilar leads with liquid-metal (GaInSn) pivots** so no net current-loop area sits in the field.
  2. **Mu-metal magnetic shield** enclosing the balance; **Helmholtz coils** to null the residual ambient field to <1 µT at the emitter.
  3. **Faraday cage + RF absorber** on chamber interior to stop stray-field forces and reflected-power torques.
  4. **Current-reversal null test:** reverse RF phase/drive polarity — a real thrust is invariant; a Lorentz artifact flips sign. Definitive discriminator.

### F — Control / DAQ / protocol (turns raw motion into a verdict)
- **DAQ:** Python or LabVIEW, synchronous logging of balance position, cavity f₀/Q, forward/reflected power, all temperatures, magnetic field, chamber pressure — all timestamped.
- **Lock-in detection:** **modulate the RF on/off (or power) at a chosen frequency f_mod ~ 0.05–0.2 Hz** (near but off the pendulum resonance) and detect the balance response *only* at f_mod. This rejects DC drift, thermal creep, and seismic tilt — the key to pulling ~nN out of the noise.
- **The four decisive controls (run every session):**
  1. **Orientation flip** — rotate the emitter 180° on the arm. Real thrust reverses direction; most artifacts don't.
  2. **Dummy ohmic load** — a resistor dissipating identical power with no resonant cavity. Isolates thermal/EMI from any real cavity effect.
  3. **Q-detune** — drive the same power *off* resonance (no stored energy). Real horizon-drive thrust should vanish; thermal/EMI persist.
  4. **Power staircase** — F vs P should be linear through the origin; a thermal artifact is often super-linear or lagged.
- **Blind analysis:** randomize/label runs so the analyst doesn't know which are live vs control until after reduction — kills confirmation bias (the field's historical failure mode).

---

## 3. Build phases, gates, and kill criteria

Each phase has an **entry gate**, **exit gate**, and an explicit **kill criterion**. Do not skip gates — that's precisely how the field produced two decades of artifacts.

### Phase 0 — Design, procurement, safety (paper + parts)
- Finalize mechanical/RF/thermal CAD; FEA the balance modes; RF-simulate the cavity (CST/HFSS/openEMS) for f₀, Q, field maps.
- BOM + safety plan (§7) + data-analysis plan **pre-registered** (blind protocol frozen before data).
- **Exit gate:** design review; predicted noise floor (from a Phase-0 error budget) < 33 nN; all four controls implementable.

### Phase 1 — Balance + metrology, NO RF (prove the instrument)
- Build the torsion balance, interferometer, vacuum, shroud, shielding. **No cavity yet.**
- Calibrate with known electrostatic/coil forces; characterize the noise floor and drift over 24–72 h; validate the lock-in pulls a *known* injected µN→nN test force out of the noise.
- **Exit gate:** demonstrated **≤ a few nN force resolution** with a stable, characterized baseline; injected-force recovery within 10%.
- **Kill criterion:** if the rig can't reach <100 nN after best effort, the science is inconclusive — fix metrology before proceeding (do NOT add RF to a blind instrument).

### Phase 2 — Copper cavity, full artifact protocol (the first real test)
- Mount the water-cooled copper frustum, RF at Q ≈ 10⁴–10⁵, UHV, all thermal/EMI controls live.
- Run the complete protocol: orientation-flip × dummy-load × Q-detune × power-staircase × lock-in × blind.
- **Predicted signal if real:** 24–240 µN — *far* above the <33 nN floor.
- **Exit gate (the crux question):** *Is there a thrust that (a) exceeds the floor, (b) reverses with orientation, (c) vanishes on Q-detune, (d) is absent on the dummy load, (e) is linear in P?* All five → proceed. Any fail → artifact.
- **Kill criterion:** null result (most likely outcome, matching Tajmar) → **publish the null + bound**; program's science goal is *achieved* even if the answer is "no." Optionally push Q higher before concluding.

### Phase 3 — Superconducting cavity, the Q-scaling test (decisive)
- *Only if Phase 2 shows a surviving signal.* Replace copper with niobium, add cryogenics (2–4 K, ~1–5 W wall load → **pulse-tube cryocooler** or LHe bath — real SRF engineering).
- Test the **load-bearing assumption**: does thrust scale ~linearly with Q up toward 10¹⁰? At Q=10¹⁰ the model predicts ~24 N — impossible to miss if true.
- **Exit gate:** thrust scales with Q as predicted (within a stated factor) → the effect is real and characterized. **This is the Nobel-class result.**
- **Kill criterion:** signal saturates or vanishes at high Q → the Phase-2 signal was a subtler artifact; publish + stop.

### Phase 4 — Self-contained bench thruster (engineering demo)
- *Only if Phase 3 confirms Q-scaling.* Build a free-standing unit: onboard RF + power + cooling, mounted on a simple scale, demonstrate **net measured force > its own weight-equivalent** on a small test mass; run untethered.
- **Exit gate:** repeatable, third-party-witnessed net thrust on an independent balance.

### Phase 5 — Scale toward the 1-ton figures (pure engineering, IF 1–4 pass)
- SRF cavity arrays, tens of kW of RF, cryoplant, structural + power integration toward the ~40–80 kW / 1-ton hover-and-climb numbers. This is *engineering*, not physics — the physics was decided in Phase 3.

---

## 4. Metrology & calibration discipline (the make-or-break)
- **Every** measurement session brackets the data with in-situ force calibrations (coil/electrostatic).
- Independent **two-sensor** position readout (interferometer + capacitive) to catch readout faults.
- **Force-rebalance mode** (servo the balance to null) linearizes the response and extends dynamic range.
- Log EVERYTHING; the analysis is **blind** until reduction is frozen.
- Cross-check with a **completely independent** second balance design (e.g. an inverted pendulum) before any "confirmed" claim — Phase 3+.

---

## 5. Representative Bill of Materials (illustrative — NOT a purchase list)
| Subsystem | Key items |
|---|---|
| Resonator | Cu frustum (machined+EP) / Nb frustum (SRF-processed); 2.45 GHz GaN amp 200 W; dual directional coupler; piezo tuner; VNA |
| Balance | tungsten fiber or cross-flexure pivot; fiber interferometer; calibration coil/comb; eddy-current damper; vibration-isolation stack; granite block |
| Vacuum | SS CF chamber; scroll + turbo + ion + NEG pumps; bakeout jackets; UHV RF/electrical/optical feedthroughs; gauges |
| Thermal | temperature-controlled shroud; RTDs; copper thermal straps/heat pipe; chiller (Cu phase) |
| EMI | mu-metal shield; Helmholtz coils + supply; laser-PV optical power link OR GaInSn pivots; RF absorber |
| Cryo (Ph3) | pulse-tube cryocooler (1–2 W @ 4 K) or LHe dewar; cold-mass supports; thermometry |
| Control | DAQ (multi-channel, synchronous); lock-in (hardware or software); control PC |

*Cost/skill tiers (order-of-magnitude only, for planning): Phase 1–2 = a serious university-lab build (RF, UHV, precision-metrology skills; a torsion-balance + UHV + RF chain). Phase 3 adds SRF + cryogenics expertise (national-lab / specialist tier). This roadmap describes the engineering; it does not procure anything.*

---

## 6. Risk register (top risks)
| Risk | Likelihood | Mitigation |
|---|---|---|
| Thermal-CoM artifact mistaken for thrust | **High** (killed the field) | ΔT<0.05K shroud + symmetric design + dummy-load + Q-detune + subtract measured transfer fn |
| EMI/Lorentz artifact | **High** | optical power / counter-wound leads + mu-metal + Helmholtz + current-reversal test |
| Balance drift/seismic swamps nN signal | High | lock-in at f_mod + vibration isolation + long integration + force-rebalance |
| Cavity detunes off resonance (no signal) | Medium | PLL/VNA frequency lock + piezo tuner; log f₀,Q continuously |
| Confirmation bias in analysis | Medium | pre-registered blind protocol; independent second balance |
| Effect is simply not real | **Most likely** | that IS a valid, publishable result — the program is designed to deliver a rigorous yes/no |

---

## 7. Safety (non-optional)
- **RF:** 100+ W at 2.45 GHz — enclosed cavity + interlocked Faraday enclosure; RF leakage survey; no exposure.
- **High voltage / power:** amplifier + PV link electrical safety; interlocks.
- **Vacuum:** implosion risk on viewports — rated glass, guards; correct pump-down/vent procedures.
- **Cryogenics (Ph3):** asphyxiation (O₂ monitor), cold-burn PPE, over-pressure relief on cryostat, LHe handling training.
- **Magnetics:** mu-metal/Helmholtz fields — pacemaker/ferromagnetic-object protocols.

---

## 8. The one-paragraph honest summary
Build the **instrument**, not the dream. Phase 1 proves you can measure a few nano-newtons cleanly. Phase 2 asks the copper-cavity question with every artifact control the field previously skipped — and most likely returns a rigorous null (a genuine, publishable result). *Only if* a signal survives all five controls do you spend the real money on Phase 3's superconducting Q-scaling test — the single experiment that would either detonate physics as we know it or close the last open door. Every phase is gated, every gate has a kill criterion, and "the effect isn't real" is an honorable, valuable outcome. That is what building this device actually means.
