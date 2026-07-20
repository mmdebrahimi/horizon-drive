# Test Parameters & Build Strategy — "How good must we build to beat the environment?"

**Date:** 2026-07-20 · **Answers:** at what Q/size the signal beats environmental artifacts; staged vs straight-to-niobium; the optimized parameters; the build table.
**Grounding:** `snr_vs_quality.py` (exit 0) + `apparatus_artifact_budget.py` + the 7 subsystem memos.

---

## The one fact that decides everything

**The signal grows with Q. The environmental artifacts do NOT.**
- Signal: `F = η·P·Q/c` — scales with quality factor Q (and power P).
- Artifacts (thermal drift, EM feed-force, radiometric): scale with **dissipated power** or are **fixed** — they are **flat in Q**.

Two consequences, both important:
1. **Power is not a lever.** More RF power lifts the signal *and* the thermal/EM artifacts together — SNR barely moves. **Size is only a weak lever** (Q≈∝1/√f, so a bigger/lower-frequency cavity gains a little). **Temperature is THE lever** — cooling drops the surface resistance, which is what raises Q by orders of magnitude.
2. **The unfakeable signature is F ∝ Q itself.** Every artifact is flat in Q; only a real thrust tracks it. So the decisive measurement is **not a single clean reading — it's the SLOPE of F versus Q.**

## What quality actually beats the environment (computed)

Assuming the full mitigation stack leaves a **residual artifact floor of ~0.3 µN (well-built) to ~3 µN (imperfect)** — this bracket *is* the core uncertainty, and it's exactly your worry:

| Rung | Q | Signal (10 W) | SNR (good mitig.) | SNR (poor mitig.) | Verdict |
|---|---|---|---|---|---|
| **Room-temp copper** | 2.7×10⁴ | 6.5 µN | 22 | **2.2** | **Marginal — works only if mitigation is good** |
| **Cryo copper (~4 K)** | 1×10⁵ | 24 µN | 80 | **8** | **Confident even if mitigation is poor ✅** |
| **Niobium / Nb₃Sn (SC)** | 1×10¹⁰ | 2.4 **N** | ~10⁶ | ~10⁶ | Unambiguous — but overkill for *detection* |

- **SNR ≥ 10** (confident) needs **Q ≈ 1×10⁴ – 1.3×10⁵** → reachable at **cryo-copper, no superconductor required.**
- **SNR ≥ 100** (mitigation-irrelevant) needs Q ≈ 10⁵ – 10⁶ → the superconductor rung.

**So the honest answer to "what size/quality":** it's **not size and not power — it's Q ≈ 10⁵, i.e. cryogenic copper.** That's the real minimum to *robustly* beat the environment. Room-temp copper (Q~27k) is genuinely marginal — **your worry is correct.**

## Should we skip straight to the niobium / full-scale build?

**No — and not for cost reasons alone. It's scientifically weaker.** Three honest points:

1. **A single high-SNR niobium point does NOT prove the effect.** However clean, one reading showing thrust could still be some *Q-correlated* systematic you didn't anticipate. **The convincing result is F tracking Q across the ladder** (copper→cryo-copper→niobium) while the artifacts (measured live via the pillbox null + dummy-heater) stay flat. A single point can't show a slope. **The staged Q-sweep is the stronger experiment, not just the cheaper one.**
2. **Niobium is overkill for detection and inherits new environmental problems.** Q~10¹⁰ gives SNR ~10⁶ — a million times more margin than you need to *detect*. And going cryogenic to get there adds its **own** artifacts: **cryocooler vibration** coupling into the balance, cryogenic-balance complexity, thermal-acoustic forces. You'd trade "marginal signal margin" for "new environmental noise + a big bill." That Q~10¹⁰ margin is what the **propulsion-grade craft** needs — not the detection test.
3. **"Full scale" (multi-cell craft) is a propulsion demonstrator, not a detector.** N cells give N× thrust but N× power/heat too — SNR doesn't improve. You build the craft *after* detection, never to achieve it.

**The real sweet spot your question points at:** not room-temp copper (too marginal), not full niobium (overkill + new artifacts + huge cost) — but **cryogenic copper, Q~10⁵.** It beats the environment confidently (SNR 8–80) *without* a superconductor, and it comes with two bonuses: the **cryostat also cryopumps to ultra-high vacuum for free** (folding the separate turbo/chamber cost in), and it puts you on the ladder to swap in Nb₃Sn later for confirmation **on the same cryostat.**

## Optimized test parameters (the recommended rig)

| Parameter | Value | Why |
|---|---|---|
| **Core lever** | **Vary Q, measure the F∝Q slope** | The only unfakeable signature; artifacts are flat in Q |
| **Q-sweep range** | ~3×10⁴ (Cu 300 K) → ~10⁵ (Cu 4 K) → later 10¹⁰ (Nb₃Sn) | Spans ≥1.5 orders now, ≥5 with the SC upgrade |
| **Target detection rung** | **Cryo-copper, Q ≈ 10⁵** | Confident SNR 8–80 without a superconductor |
| **RF power** | ~10 W dissipated, **held constant across Q** | Power isn't a lever; constant power keeps artifacts fixed |
| **Frequency / mode** | 1.836 GHz, TM010, frustum | Per the fixed cavity design |
| **Vacuum** | ≤10⁻⁷ torr (cryopumped for free at 4 K) | Radiometric artifact →negligible |
| **Modulation** | on-res ↔ off-res at **constant total dissipated power**, ~0.02 Hz, blind-randomized | Thermal artifact → common-mode (see master design) |
| **Null control** | symmetric **pillbox** run identically each session | Must read zero; catches any residual systematic |
| **Discriminator stack (all required)** | Q-slope · 180° rotation · current-polarity · pressure-independence · two-cal-agree <2% · dummy-heater null | A signal counts only if it survives ALL |
| **Detection bar** | F ∝ Q slope significant AND pillbox null flat AND survives all reversals | Not a single-point SNR |

## Build table — each element / action (recommended cryo-capable Q-sweep rig)

| # | Element / Action | Spec / target | Role | Est. cost (used→new) |
|---|---|---|---|---|
| 1 | **Closed-cycle cryostat** (pulse-tube, ~1.5 W @ 4 K) + **vibration isolation** (remote/soft cold link) | 4 K, low-vibration mount | Raises Q (the lever) **+ free UHV via cryopumping**; vibration is the new artifact to fight | $40–80k |
| 2 | **Copper cavity — high-RRR OFHC** (frustum) + **matching pillbox null** | RRR>100; Q~2.7×10⁴ (300 K) → ~10⁵ (4 K); Ra≤0.4 µm bore | The resonator; RRR grade so cooling actually buys Q | $3–5k (machining) |
| 3 | **RF power chain** | Valon 5015 synth → 10 W PA → isolator+circulator → **fixed off-balance dump** → dual coupler → 2× traceable RMS sensors | Clean drive; constant dissipated power; reflected heat to a fixed sink | $4–9k |
| 4 | **PLL frequency lock + thermal** | dither/refl-min lock (Red Pitaya) + fiber-optic temp sensors + symmetric straps | Holds stored energy constant vs detuning; kills the #1 artifact | $4–10k |
| 5 | **Force balance (cryo-compatible)** | torsion balance, W fibre, CFRP arm, optical-lever→interferometer, **in-vacuum 180° rotation stage** | Reads the ~10–24 µN force; rotation = master discriminator | $5–15k (cryo raises this) |
| 6 | **Vibration isolation** | Minus-K negative-stiffness stage + cryocooler decoupling | Cryocooler vibration is the cryo path's new environmental enemy | $3–8k |
| 7 | **Calibration** | comb electrostatic actuator + photon-pressure cross-check (traceable thermopile) | Two absolute force refs agree <2% → licenses the newtons | $15–40k |
| 8 | **EM shielding + DAQ** | mu-metal, **coax zero-loop** leads, star ground, software lock-in, blind scheduling | Kills feed-current×B; phase-sensitive detection; anti-bias | $1–2k |
| A | **Action: machine cavity + pillbox** | send STEP + spec to shop | — | (in #2) |
| B | **Action: assemble + commission cold** | cool down, find TM010, measure Q at 300 K and 4 K | Confirms the Q-sweep range is real | time |
| C | **Action: validate with the lifter** | Biefeld–Brown lifter — must read zero in vacuum | Proves the whole force chain against a known answer (~$5) | ~$5 |
| D | **Action: run the Q-scaling campaign** | F vs Q at fixed power; pillbox null each session; all reversals | The actual experiment — measure the slope | time |
| — | **TOTAL (detection rig, cryo-copper)** | | | **~$75–170k** |
| — | **Upgrade: Nb₃Sn coating** (same cryostat) | JLab/Fermilab/Cornell collaboration; Q→10¹⁰ | Unambiguous confirmation **only if** the Q-sweep shows the effect | +$40–100k (partnership-gated) |

## Bottom-line recommendation

- **Don't fight to the death on room-temp copper (marginal SNR 2–22), and don't leap to full niobium/full-scale (overkill, new cryo artifacts, huge bet, and scientifically *weaker* than a slope).**
- **Build the cryo-capable Q-sweep rig.** It reaches **cryo-copper Q~10⁵ (confident SNR 8–80)**, gets **free UHV** from cryopumping, and — crucially — lets you measure the **F ∝ Q slope**, the one signature no artifact can fake. Cost ~$75–170k, still lab-partnership-friendly.
- **Reserve niobium as the confirmation upgrade** on that same cryostat, pursued *only if* the copper-to-cryo-copper slope already shows the effect.
- **The single most honest caveat:** cooling buys signal margin but adds **cryocooler vibration** as a new environmental enemy (elements #1, #6 fight it). There is no free lunch — but Q, not power or size, is the only lever that raises signal *without* raising the environment, so the cryo path is still the right one.

*This still sits under the standing honesty rail: the most sensitive independent group (Tajmar) has null-tested this class to the nN floor; a positive result would be extraordinary. This memo optimizes the experiment to give a **credible** answer either way — the value is a clean null or (improbably) a slope that survives every discriminator. All numbers in `snr_vs_quality.py` (exit 0, wired into `verify_all.py`).*
