# Horizon Drive — An Honest Anti-Gravity Investigation + Engineering Digital Twin

A rigorous, suspend-disbelief exploration of whether any known or frontier physics could let a craft
manipulate its own inertia (and thereby its weight) — followed, once the physics is *assumed* proven, by a
full engineering design and a **runnable simulation** of the resulting vehicle.

Every number in this repository was derived and checked against the measured constants of physics
(CODATA), and every empirical claim was grounded to a primary source through an audit pipeline. The point
throughout is honesty: where a mechanism is dead, the math says so; where it survives, the "no" is named
precisely (experimental precision vs. fundamental impossibility).

> **What this is:** an honest physics survey + an engineering "what if it worked" build study + a working
> control-simulation. **What this is not:** a claim that anti-gravity is real. The physics is open and
> unconfirmed; the engineering is fan-fiction with honest numbers. Read the memos for the distinction.

---

## The bottom line (from the research)

Every anti-gravity corner is walled off by orders-of-magnitude or symmetry — modified Maxwell (forbidden by
gauge/Lorentz symmetry), light→gravity (43 orders too weak + wrong sign), Higgs-lightening (touches only 1%
of mass, costs ~10³⁷ J/mm³), warp/negative-energy (Ford–Pfenning: ~10¹¹× the universe's mass), spin–torsion
(Planck-suppressed), Woodward (Tajmar null) — **except inertia-from-the-vacuum** (Haisch–Rueda–Puthoff /
McCulloch quantised inertia), whose "no" is *experimental precision*, not fundamental physics. And even that
one meets a two-sided vise: a reactionless thruster beating the photon-rocket limit would violate the first
law of thermodynamics (Higgins 2015), while pushing on the vacuum needs a rest frame the vacuum lacks
(Carroll). The only version that survives is a genuine **inertia modifier** — which sidesteps the vise.

## Repository map

| Path | What |
|---|---|
| `research_outputs/antigravity-medium-article-draft-2026-07-04.md` | The essay (physics, ~25 min) — is any of this real? |
| `research_outputs/antigravity-construction-companion-article-2026-07-05.md` | The build companion (~13 min) — if it worked, what would you build? |
| `research_outputs/antigravity-cavity-chamber-deep-dive-2026-07-06.md` | Cavity-chamber deep-dive (~11 min) — the craft's most important part: QI mechanism, why Q is the lever, the 2 K-Nb vs 4 K-Nb₃Sn fork, the 50 MV/m ceiling, and the failure demons |
| `research_outputs/antigravity-first-principles-derivation-deep-dive-2026-07-04.md` | First-principles derivations (Maxwell forced, the walls, the surviving door) |
| `research_outputs/antigravity-full-landscape-assessment.md` | The full ~35-candidate landscape matrix |
| `research_outputs/casimir-*`, `lentz-*`, `woodward-*`, `polarizable-*`, `qi-haisch-*`, `quantised-inertia-*`, `higgins-*`, `space-horizon-*` | Per-candidate audit memos (primary-source-grounded) |
| `research_outputs/antigravity-working-device-build-instructions-2026-07-04.md` | The working-craft build (modules A–H), assuming the effect is real |
| `research_outputs/antigravity-device-engineering-roadmap-2026-07-04.md` | The decisive-experiment test-rig roadmap |
| `research_outputs/antigravity-decisive-experiment-design-2026-07-06.md` | **The definitive falsification experiment** — full design: Q-scaling discriminator, null-test matrix, go/no-go decision tree, 3-phase escalation |
| `research_outputs/decisive_test_budget.py` | Runnable signal/systematics/noise budget for the decisive experiment (proves it's systematics-limited, not sensitivity-limited) |
| `research_outputs/decisive_test_sim.py` | Measurement digital-twin: torsion balance + systematics + lock-in; proves the analysis pipeline detects a true-QI world and rejects a systematics-only one (zero false positives) |
| `research_outputs/antigravity-phase1-buildspec-2026-07-06.md` | **Turnkey Phase-1 build spec** — the cheap room-temp-copper decisive test: BOM, assembly, the 8 applicable null tests, calibration, go/no-go, safety/cost tier |
| `research_outputs/phase1_balance_sizing.py` | Sizes the Phase-1 torsion balance (0.90 mm W fibre) and proves it resolves the 12 µN signal with ~7,900× margin |
| `research_outputs/antigravity-device-drawing-guide-LLM-spec-2026-07-05.md` | An LLM prompt spec to generate a step-by-step visual build guide |
| `plans/Anti_Gravity_Device_Hardware_WBS.md` | Hardware work-breakdown structure |
| `device_sim/` | **The digital twin** — a runnable 6-DOF simulation of the thruster craft |

## The digital twin (`device_sim/`)

A simulation of the 62-cell superconducting thruster array + fly-by-wire flight control (physics assumed
proven: `F = η·P·Q/c`, 240 N per 1 kW cell). It reproduces the verified mass/power budget and flies a full
closed loop — with per-cell thrust-slew dynamics, noisy sensors, a Kalman/complementary state estimator,
and control allocation that reallocates around failed cells.

```bash
pip install -r requirements.txt                    # numpy, scipy, pytest
python -m pytest -q device_sim                     # 15 tests, all green
python -c "from device_sim.montecarlo import campaign; print(campaign().summary())"
```

*Last verified 2026-07-06: 15/15 tests pass; the Monte-Carlo campaign reports 100.0% survival (40/40), 0 diverged, worst-case 0.278 m, up to 8 cells quenched.*

**Headline results:**
- Reproduces the verified budget exactly: 240 N/cell, 62 cells, ~126 kW, ~490 kg cryocoolers, ~1,108 kg dry.
- Holds hover, step/diagonal translation, and ±5-cell quench to **< 1–2 cm** with < 2° tilt.
- Under realistic sensor noise (3 cm / 0.5°) + a Kalman estimator, holds hover to **~3.7 cm**.
- **Monte-Carlo fault campaign: 100% survival over 40 randomized runs** (random targets, up to 8
  simultaneous cell failures at random times), zero divergences, worst-case position error 0.278 m.

A key engineering finding surfaced by the twin: **attitude-control authority must scale with the vehicle's
moment of inertia** or the cascaded loop goes unstable — the kind of thing a digital twin exists to catch
before hardware.

## Honesty rails

- Physics claims are grounded to primary sources (arXiv, NASA, peer-reviewed); the audit memos separate
  supported (verbatim-quoted) from unsupported (needs-verification) rows.
- The engineering "what if it worked" study is explicitly conditional on the effect being real.
- The single load-bearing caveat: the surviving mechanism must be an *inertia modifier*, not a reactionless
  thruster — the latter is forbidden by thermodynamics + momentum conservation.

*Built as a research + engineering exercise. Suspend disbelief for the physics premise; the arithmetic is
honest either way.*

## License

Code (`device_sim/`) is released under the **MIT License** (see `LICENSE`) — clone it, run it, break it,
build on it. The research essays under `research_outputs/` are shared for reading and discussion; please
credit the author and link back if you quote or reuse them.
