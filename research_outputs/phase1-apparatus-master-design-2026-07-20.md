# Phase-1 Apparatus — Integrated Master Design & Optimization

**Date:** 2026-07-20 · **Scope:** the complete room-temperature decisive-experiment apparatus for the horizon-drive copper cavity
**Built from:** 7 subsystem deep-dives (each its own memo) + the cavity design review + the taper-vs-pillbox fork resolution
**Grounding:** `apparatus_artifact_budget.py` (exit 0) + the per-subsystem memos below

> This is the synthesis: how the seven subsystems combine into ONE coherent, null-capable measurement, what the design converges on, and the honest cost/reality of building it.

---

## The core thesis — this is not "measure a force," it's "make every artifact betray itself"

The predicted Phase-1 signal is **~12 µN**. The decisive finding of this whole optimization pass (`apparatus_artifact_budget.py`): **four of the six candidate artifacts individually RIVAL OR EXCEED that 12 µN signal.** No single measurement can be trusted. The apparatus is therefore designed as a **stack of orthogonal discriminators** — each artifact is separated from a real thrust by a *different* symmetry or parameter it cannot fake. A signal counts as real **only if it survives ALL of them at once.** That stack is exactly what EmDrive/Eagleworks lacked and what Tajmar's SpaceDrive group used to null those claims.

## The discriminator stack (the crown jewel — how each artifact is killed)

| Artifact | Size vs 12 µN signal | The discriminator that separates it | Owning subsystem |
|---|---|---|---|
| **Radiometric / convective** (residual gas) | **~23–44 µN @ 10⁻³ torr** (exceeds signal!) → 0.02–0.04 µN @ 10⁻⁶ (≈270×+ margin) | **Pressure sweep at fixed RF power** — real thrust is pressure-independent; artifact dies as you pump down | Vacuum |
| **Thermal / center-of-mass drift** (RF heating detunes cavity) | dominant, slow | **Constant-dissipated-power on↔off modulation** (heat identical both phases → common-mode → lock-in rejects) **+ 180° rotation + dummy-heater null + temp regression** | Thermal + Force metrology |
| **Feed-current × Earth-field** (I L×B) | **~15 µN @ 1 A loop** (exceeds signal!) | **Coax zero-loop routing** + **current-polarity reversal** (real thrust invariant, artifact flips) | EM / DAQ |
| **Stored-energy drift** (detuning) | large | **PLL frequency-lock** holds stored energy constant | Thermal + RF |
| **Optical-lever beam drift** | can rival signal | enclose/stabilize beam path; migrate to interferometer if it limits | Force metrology |
| **Experimenter bias** | — | **Blind + PRNG-randomized on/off scheduling** | EM / DAQ |

**Two master symmetries thread through everything:**
- **180° cavity rotation** — a real thrust is fixed in the *cavity* frame, so it **flips sign**; thermal-CoM-drift and gravity-leveling artifacts don't. (Force metrology + EM both converged on this independently.)
- **F ∝ Q at fixed dissipated power** — the headline discriminator: real thrust scales with Q, every systematic is flat in Q. This is why the **material/temperature ladder IS the experiment's measurement axis** (see Q-ladder below).

## The single most important cross-subsystem finding (a design pivot)

Independently, the **RF** and **thermal** agents converged on a subtle, *fatal* flaw in the obvious approach and its fix:
> **Naïve on/off RF modulation is fatal** — it modulates *heat* at the same ~0.02 Hz the lock-in listens at, placing the thermal artifact **exactly at the reference frequency where it is NOT rejected.**
> **Fix:** modulate **on-resonance ↔ off-resonance at constant TOTAL dissipated power** — the reflected/differential power is dumped into a *fixed, off-balance, thermally-massive load*, so the copper heats identically in both phases. The thermal artifact becomes common-mode/DC (rejected); the stored-energy-dependent thrust stays at 0.02 Hz (detected).

This one decision reshapes the RF chain (isolator + circulator → fixed dump), the thermal design (symmetric heating), and the modulation scheme simultaneously. It is the linchpin of the whole apparatus.

## The 7 subsystems — optimized picks (each has a full memo)

| # | Subsystem | Optimized pick (headline) | The one null-critical move | ~Cost (used→new) |
|---|---|---|---|---|
| 1 | **RF power chain** | Valon 5015 synth → Mini-Circuits ZHL-10W-2G+ PA → DiTom isolator+circulator → dual-directional coupler → 2× NIST-traceable RMS sensors; inverse-Pound/PDH lock via Red Pitaya | Route ALL reflected power to a **fixed off-balance thermal dump** | $4–9k |
| 2 | **Vacuum** | Pfeiffer HiCube 80 / Agilent TwisTorr 74 (oil-free) + dry scroll; 450–600 mm electropolished chamber; PKR full-range gauge; bellows-decoupled pump | Reach + **log ≤10⁻⁶ torr** and run the **pressure sweep** | $6–19k |
| 3 | **Force metrology** | 0.90 mm W fibre × 300 mm (κ≈3.5×10⁻² N·m/rad; 12 µN→**7.8 µm**), CFRP arm, optical-lever start (→interferometer), Minus-K isolation, removable eddy damper | **In-vacuum 180° rotation** + counterbalanced (hot mass at ~zero moment arm) | $1–5k DIY (+isolation) |
| 4 | **Calibration** | Comb electrostatic actuator (Trek 601C HV, gap-independent) **+** 1064 nm photon-pressure cross-check (traceable thermopile); in-situ tones at distinct freqs | **Two absolute refs agree <2%** in overlap or reporting is blocked | **$15–55k** ⚠ |
| 5 | **Thermal + PLL** | dither/reflected-min lock (not full PDH), fiber-optic temp sensors *inside* RF field, PA off-balance, symmetric straps | **Constant-dissipated-power modulation** (see pivot above) | $4–10k |
| 6 | **EM + DAQ** | Nested mu-metal, coax/twisted leads + π-filters, star ground, LabJack/Pi DAQ, Python software lock-in | **Coax zero-loop + polarity×rotation 2×2** | $0.6–1.8k |
| 7 | **Cryo / SRF path** | Cryocooler @ 4.2 K (Cryomech PT415) + **Nb₃Sn** (Q~10¹⁰ at 4.2 K = Nb-at-2K, ~10× less cryo); cryo-Cu middle rung | The **Q-ladder** = the F∝Q discriminator axis | $40–250k (Phase 3) |

## The Q-ladder = the experiment's measurement axis (with an honest correction)

> **Cu (300 K) 2.7×10⁴ → cryo-Cu (4 K) ~10⁵ → Nb₃Sn (4.2 K) ~10¹⁰**

**Correction surfaced by the cryo agent:** cryogenic copper caps near **~10⁵** (anomalous skin effect), **not ~10⁶** as loosely stated in the earlier design review — still a real, cheap middle F∝Q point, but a smaller lever than assumed. **Nb₃Sn at 4.2 K** (ordinary liquid helium / a cryocooler, not superfluid) is the right superconducting target for a Q-only test; its field-quench weakness is irrelevant at low field. SRF cavities: only RI (Germany) / Zanon (Italy) build full cavities; the realistic small-researcher path is a **coating/testing collaboration with JLab / Fermilab / Cornell** (single-cell processed Nb ≈ $40k). **The near-term bottleneck is lab partnerships, not cash.**

## The build/validation ladder (cheapest-first, known-answer-first)

1. **Biefeld–Brown lifter (~$5)** — known-answer calibration article: must lift in air, read **zero in vacuum**. Validates the whole vacuum + force chain before risking real money. *(See `biefeld-brown-replication-assessment`.)*
2. **Symmetric pillbox null-control** — same material/finish/drive as the cavity, must read **zero** (QI symmetric ⇒ 0). *(See `cavity-geometry-fork-resolution`.)*
3. **Copper frustum @ room temp** — the actual Phase-1 measurement (Q~27,000, F∝Q vs the pillbox null).
4. **Cryo-Cu → Nb₃Sn** — extend the Q-ladder (Phase 3, lab-partnership-gated).

## Honest cost reality (the number that matters)

The user's earlier ~$2k anchor was **just the machined cavity.** The **full Phase-1 room-temperature apparatus** is realistically:

| Bucket | Used/DIY | New |
|---|---|---|
| Cavity (frustum + pillbox) | ~$2k | ~$4k |
| RF chain | ~$4k | ~$9k |
| Vacuum | ~$6k | ~$19k |
| Force metrology + isolation | ~$3k | ~$8k |
| **Calibration** ⚠ | **~$15k** | **~$55k** |
| Thermal + PLL | ~$4k | ~$10k |
| EM + DAQ | ~$0.7k | ~$1.8k |
| **Phase-1 total** | **~$35k** | **~$100k+** |

**The surprise cost driver is CALIBRATION**, not the exotic cavity — traceable, redundant force metrology (two independent absolute references) is where the money is, precisely because that's what makes a 12 µN claim *credible*. Vacuum is second. Phase-3 cryo/SRF adds **$40–250k** and is gated on lab access more than money.

## What this changes about "how to build it"
- **You cannot credibly do this as a pure garage build for ~$2k.** The honest floor for a *publishable* null-or-detect is **~$35k used/DIY**, dominated by calibration + vacuum.
- **→ The real path forward is a lab partnership**, not a personal purchase — exactly what the earlier lab-outreach analysis pointed to (Tajmar/SpaceDrive already owns the ideal rig; a university with a torsion balance + vacuum + traceable force metrology collapses the cost to ~$0 and adds credibility).
- **The lifter + pillbox ladder** lets you validate cheaply and demonstrate competence *before* asking a lab for time on the expensive article.

## Honest rails (unchanged)
This apparatus is designed to **detect OR null** — it is built to *disprove* a signal as readily as confirm one. The prior context stands: the most sensitive independent group (Tajmar) has already null-tested this *class* of device to the nN floor; a positive result would be extraordinary. This design's value is that it could produce a **credible** null or (improbably) a **survives-every-discriminator** detection — not another artifact-driven false positive.

---

*Per-subsystem detail: `subsystem-{rf-power-chain,vacuum-system,force-metrology,calibration,thermal-management,em-shielding-daq}-optimization-2026-07-20.md` + `subsystem-cryogenic-srf-path-2026-07-20.md`. Cross-checks: `apparatus_artifact_budget.py` (exit 0, wired into `verify_all.py`). Cavity: `copper-cavity-design-review` + `cavity-geometry-fork-resolution`. Numbers are order-of-magnitude engineering estimates for planning, not final specs.*
