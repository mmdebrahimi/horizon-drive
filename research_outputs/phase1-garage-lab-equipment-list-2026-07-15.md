# Phase-1 Garage/Basement Lab — Equipment List

**For:** the room-temperature copper-cavity decisive test (Horizon-Drive Phase 1)
**Compiled:** 2026-07-15 · companion to `antigravity-phase1-buildspec-2026-07-06.md` + `copper-cavity-machinist-spec-2026-07-15.md`

> **Read first — two safety systems that can hurt you:**
> - **RF (10–15 W @ ~1.84 GHz):** microwave-band, tissue-heating. **Never energize an open/unshielded cavity. Never look into or probe a live cavity.** Keep everything inside a closed, interlocked enclosure.
> - **High vacuum:** implosion energy in a bell jar is real. Use a rated chamber, a guard/shield, and standard vacuum practice.
> - **Non-negotiable rule from the physics:** *every* part near the RF and the balance must be **non-magnetic** (copper, brass, aluminium — **no steel**), or the later null tests are meaningless.

---

## What you already have (✔)
- ✔ Vacuum pump — *see the honest note in §2; a roughing pump alone won't reach the vacuum a clean measurement needs.*
- ✔ Variac — useful for the amplifier PSU / general power.
- ✔ Basic electrical + test gear (DMM, soldering, bench PSU, oscilloscope presumed).

---

## The smart way to buy: TWO stages

**Do NOT buy the whole rig at once.** The cavity has to pass a resonance/Q test *before* the thrust rig is worth building. So:

- **Stage 0 — "Does the cavity even work?"** (cheapest, do first): machined cavity + a VNA + RF cables. Measure the resonance near 1.84 GHz and the unloaded Q₀. **Gate: Q₀ ≥ 20,000.** If it fails, you fix polishing/sealing before spending another dollar.
- **Stage 1 — "Does it push?"**: add the RF power chain, the vacuum thrust chamber, the torsion balance + optical readout, shielding, and the DAQ/modulation.

---

## §0 — The cavity itself
| Item | Notes | Tier |
|---|---|---|
| Copper cavity (body + cap + tuner) | Per the machinist spec `HD-CU-CAV-001`. OFHC copper, mirror bore. | $$ (machine-shop) |
| Non-magnetic fasteners + copper gasket | Brass/silver-plated brass M5; soft-copper mouth gasket. | $ |

## §1 — RF metrology (Stage 0) — **the first real cost decision**
| Item | Notes | Tier |
|---|---|---|
| **VNA covering 1–3 GHz** | **The critical measurement tool.** Measures the resonance + Q. | see below |
| RF cables + SMA/N adapters, torque wrench | Low-loss, short. | $ |

> **VNA honesty:** a **NanoVNA (v2/H4/"3 GHz" models, ~$50–150)** *can* find the 1.84 GHz resonance and give a rough Q — but its dynamic range/frequency resolution make measuring a **Q≈27,000** cavity marginal (you'll under-read Q). A **used benchtop VNA** (Keysight/HP 8753/Rohde, ~$1–5k used) measures it properly. **Best move: borrow/rent a benchtop VNA for the one-time cavity characterization** (a nearby university RF lab, makerspace, or ham-radio club often has one). Buy a NanoVNA for day-to-day tuning; borrow a real VNA for the acceptance number.

## §2 — Vacuum (Stage 1) — **the second real cost decision**
| Item | Notes | Tier |
|---|---|---|
| Vacuum chamber / bell jar w/ feedthroughs | Must fit the balance + cavity; needs RF + optical + power feedthroughs. | $$ |
| **Turbomolecular pump** (+ your roughing pump as backing) | **Likely the biggest single gap.** | $$$ |
| Vacuum gauge (Pirani + cold-cathode/ion) to read ≤10⁻⁶ torr | Your roughing pump + Pirani only reads ~10⁻³ torr. | $$ |
| Vibration-isolated pump mount + flexible bellows | Keep pump vibration off the balance. | $ |

> **Vacuum honesty:** a **roughing pump alone reaches ~10⁻³ torr** — at that pressure, **air convection + radiometric heat currents dominate and will fake a "thrust"** (this is exactly what discredited earlier EmDrive measurements). A **clean null needs high vacuum (<10⁻⁶ torr), which requires a turbo pump** on top of what you have. This is the item most likely to blow the budget. *Interim option:* you can do preliminary shakedown at 10⁻³ torr to debug the rig, but **the publishable measurement needs the turbo.** Used turbos (Pfeiffer/Edwards/Leybold) show up on the surplus market.

## §3 — RF power chain (Stage 1) — drives the cavity
| Item | Notes | Tier |
|---|---|---|
| Signal generator / VCO, ~1.8–1.9 GHz, phase-lockable | Sets the drive frequency. | $$ |
| **RF power amplifier, ~10–15 W @ 1.84 GHz** (GaN/LDMOS module) | The "engine." Module or kit. | $$–$$$ |
| Directional coupler (fwd/reflected monitoring) | Watch for detuning/quench precursors. | $ |
| Circulator/isolator + matched dump load (50 Ω, ~20 W) | **Critical for the null test:** routes reflected power to a *fixed* sink so on/off-resonance dumped power is equal. | $$ |
| RF power meter / detector head | Reads forward + reflected power. | $$ |

## §4 — Thrust measurement (Stage 1) — **mostly DIY, the good news**
| Item | Notes | Tier |
|---|---|---|
| Torsion balance | **Build it.** Tungsten fibre **Ø0.90 mm × 300 mm**, low-CTE beam (carbon-fibre/Zerodur), cavity + counterweight at ±15 cm. Sized in `phase1_balance_sizing.py`. | $ |
| **Optical readout** — laser + position-sensitive detector (optical lever), or a fibre displacement sensor | The 12 µN signal deflects the arm **~8 µm**; a simple laser optical-lever resolves that with **~1000× margin** (verified). You do **not** need a lab interferometer for a first result. | $–$$ |
| Fine rotation stage under the whole balance | For the 180°-rotation null test. | $ |
| Eddy-current damper (Cu vane + magnet, **removed during runs**) | Tames the ~12 s balance mode. | $ |

> **This is the part that's genuinely garage-friendly.** The predicted signal is ~8,000× above a careful home torsion balance's floor, so a DIY balance + laser optical-lever is *enough* — the hard engineering is vacuum + RF cleanliness, not the balance sensitivity.

## §5 — Calibration (Stage 1) — turns "a deflection" into "newtons"
| Item | Notes | Tier |
|---|---|---|
| Electrostatic actuator (plate + calibrated HV) | Applies known µN forces to calibrate the balance. | $ |
| Calibrated laser + mirror for a photon-pressure cross-check (F = 2P/c) | Second, first-principles force calibration; must agree with the electrostatic one to ≤2 %. | $ |

## §6 — Shielding, DAQ, modulation (Stage 1)
| Item | Notes | Tier |
|---|---|---|
| **Mu-metal shield** around the balance + twisted/shielded leads | Kills feed-current × Earth-field forces. | $$ |
| Vibration-isolated optical table / slab | The balance must sit still. | $–$$ |
| Microcontroller (Arduino/Pi) to square-wave the RF on/off at ~0.02 Hz + log the photodiode | **Software lock-in** does the rest — no hardware lock-in needed. | $ |
| Thermocouples/RTDs (×3–4: cavity, coax, chamber) | Track thermal drift (the #1 artifact). | $ |

---

## Priority / buy order (recommended)
1. **Get the cavity machined** (spec is ready).
2. **Beg/borrow/rent a benchtop VNA** → run the Stage-0 Q test. *Gate: Q₀ ≥ 20,000.* **Stop and fix before spending more if it fails.**
3. Sort **vacuum** (the turbo + gauge) — the long-lead, high-cost item; start sourcing early (surplus market).
4. Build the **torsion balance + optical readout** (cheap, in parallel with #3).
5. Buy the **RF power chain** (amp + circulator + dump load + coupler).
6. Add **shielding + DAQ**; integrate; commission.

## The two honest bottlenecks (where the money + difficulty are)
- **A VNA that can truly measure Q≈27,000** → *borrow one for the one-time acceptance; NanoVNA for daily tuning.*
- **High vacuum (turbo pump + ion gauge)** → *unavoidable for a clean, publishable null; roughing-pump-only pressures will fake a signal.*

Everything else — balance, optical readout, calibration, DAQ, modulation, RF chain — is modest-cost and largely buildable.

---
*Nothing here is a purchase I made — this is a spec/advisory list for you to source and budget. When you have the cavity machined + a VNA in hand, bring the Q measurement back and we'll interpret it and set up the thrust run.*
