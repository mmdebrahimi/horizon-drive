# The Cavity Chamber: Where the Anti-Gravity Actually Happens

### A deep dive into the single most important part of a horizon-drive craft — the one component that is simultaneously the most speculative physics and the most mature engineering on the whole vehicle.

*Draft · 2026-07-06 · a technical companion to ["How You'd Actually Build One"](antigravity-construction-companion-article-2026-07-05.md) and the essay ["The Only Honest Path to Anti-Gravity Runs Through Your Own Inertia."](antigravity-medium-article-draft-2026-07-04.md)*

---

*Everything else on the craft — the cryoplant, the generator, the flight computer — is there to serve one small metal cone. If the effect is real, that cone is where a craft reaches out and changes its own inertia. So it's worth slowing down and looking at it closely: what it's supposed to do, why it has to be superconducting, and the three quiet ways it fights the engineer who builds it. It turns out to be the strangest component on the vehicle — the part whose physics is least certain, built out of the part whose engineering is most certain.*

## What the cavity is actually for

Strip away the fuselage and the cryogenics and you're left with the only thing that matters: **a resonant cavity shaped like a truncated cone** — a frustum, wide at one end, narrow at the other. In the honest-but-suspend-disbelief scenario this whole project lives in, *that shape is the physics.* Not the styling. The shape.

The mechanism we're betting on is Mike McCulloch's **quantised inertia** (QI). Its claim, in one breath: inertia isn't a given — it emerges from the way an accelerating object interacts with the vacuum (Unruh radiation), and that interaction can be *shaped* by putting horizons around it. A tapered cavity does exactly that. In McCulloch's own words from the 2016 EmDrive paper, *"more Unruh waves are allowed at the wide end, leading to a greater inertial mass for the photons there... the cavity must move towards its narrow end"* ([McCulloch 2016, arXiv:1604.03449](https://arxiv.org/abs/1604.03449)). Photons bouncing inside the cone are, in this picture, slightly heavier at the big end than the small end, and to conserve momentum the whole cavity drifts toward the narrow side. That drift is your thrust.

This is why the cavity is the beating heart of the craft and not just a part in it: **the asymmetry of the cone is the engine.** Make it a cylinder and, by the same theory, the effect vanishes. And there's a beautiful, cheap falsification baked right in — QI predicts that *"if the axial length is equal to the diameter of the small end of the cavity, the thrust should be reversed"* ([same paper](https://arxiv.org/abs/1604.03449)). A theory that tells you exactly which geometry flips the sign of the force is a theory you can kill on a bench. That single test — build the reversed geometry, watch which way it pushes — is worth more than any amount of arguing.

So the cavity is where the one genuinely open question of this entire enterprise lives: **does shaping the vacuum with a horizon actually produce a force?** Everything downstream assumes yes. This document is about what you'd build *if* the answer is yes — and about the one number, buried in the cavity, that decides whether the craft is a garage project or a national one.

## Why it has to be superconducting: Q is the whole lever

Here is the number that shapes the entire vehicle. The thrust from one cell follows a simple law:

> **F = η · P · Q / c**

— where *P* is the RF power you pump in, *c* is the speed of light, *η* is the (unknown, hoped-for) efficiency of the effect calibrated against the Eagleworks measurements (~0.0072 in our budget), and **Q is the quality factor of the cavity.** Q is the number of times the electromagnetic wave bounces coherently inside the cavity before its energy leaks away. A Q of 10¹⁰ means the field builds up ten billion-fold: a 1-kilowatt feed sustains a stored, circulating field equivalent to something astronomically larger, and *that* stored field is what the effect acts on.

Run the arithmetic and the leverage is staggering: at Q = 10¹⁰, one 1-kilowatt cell produces **240 newtons** — roughly the thrust of a small jet engine, from a cone you can hold in two hands, fed by a kilowatt. Take the *same* cavity and let Q fall to 10⁶ (a good room-temperature copper cavity), and the thrust falls by four orders of magnitude to a fraction of a newton. Nothing flies.

Now the honesty, because this is where the single biggest bet in the whole design sits — and it is not "can we build a Q = 10¹⁰ cavity" (we can). It's whether that thrust law is real. Two things have to hold, and neither is established: **(1)** the η above is pinned to a *disputed* measurement — NASA Eagleworks' ~1.2 mN/kW at Q ≈ 5×10⁴, which later high-precision experiments (Dresden / Tajmar) could **not** reproduce, finding no thrust above the photon-recoil floor; and **(2)** getting from that low-Q bench number to 240 N at Q = 10¹⁰ assumes the thrust keeps scaling *linearly with Q across six orders of magnitude* — something no one has ever demonstrated. It gets worse: the companion essay's thermodynamic vise shows that *if* the effect did scale that far, the drive would beat the photon-rocket limit and become a free-energy machine at walking speed — which is exactly why the only physically-survivable reading is a genuine **inertia modifier**, not a reactionless thruster. So treat the 240 N/kW as an *assumed actuator*, and everything below as the answer to a narrower question: given such a cell, what would the cavity have to be?

**That factor of ten thousand is the entire reason this craft is a cryogenic machine.** You cannot get Q = 10¹⁰ out of copper at room temperature; the walls dissipate too much. You can only get it from a **superconductor**, where the RF surface resistance collapses by orders of magnitude and the field can ring ten billion times before it dies. The "anti-gravity" craft is, at its core, an accelerator-physics machine — a flying array of superconducting radio-frequency (SRF) cavities, the same technology that drives the beams at CERN, Fermilab, and Jefferson Lab. The exotic part borrows its whole body from the most mundane, mature corner of big physics.

## The temperature trap: why "4 K" is quietly load-bearing

Here's where the engineering gets sharp, and where the popular version of the story quietly cheats. It's easy to write "niobium held at 4 kelvin" and move on. But 4 K versus 2 K is not a rounding detail — it's the difference between the craft working and not.

The loss in an SRF cavity is dominated by the **BCS surface resistance**, and that resistance falls *exponentially* as you cool. For a 1.3 GHz niobium cavity, the numbers are brutal and specific: the BCS surface resistance drops from about **800 nΩ at 4.2 K to roughly 15 nΩ at 2 K** — a fifty-fold collapse ([SRF literature; see e.g. the nitrogen-infusion work, arXiv:1701.06077](https://arxiv.org/pdf/1701.06077)). Since Q is inversely proportional to that resistance, the same physical cavity that manages perhaps Q ~ 10⁸–10⁹ at 4.2 K leaps to **well above 10¹⁰ at 2 K.** This is exactly why every large accelerator on Earth pays the enormous expense of running its niobium cavities near 1.9–2 K in *superfluid* helium rather than the far cheaper 4.2 K.

So the honest statement is this: **pure niobium does not give you Q = 10¹⁰ at 4 K. It gives it to you at 2 K.** And 2 K is a worse place to be than 4 K for a flying machine — superfluid helium, lower temperature, an even steeper cryogenic penalty, more compressor mass. The "4 K" in the build spec is doing more work than it looks like.

There are only two honest ways out, and both of them keep *cold* as the wall the whole craft is built around.

## The material fork: niobium at 2 K, or Nb₃Sn at 4 K

**Road one — pure niobium, at 2 K.** You get the full Q = 10¹⁰⁺ and the highest gradients (more on that below), but you commit to a superfluid-helium cryoplant. On a one-ton flying craft, that's the heaviest, most demanding version of the cold problem.

**Road two — niobium-tin (Nb₃Sn), at 4 K.** This is the genuinely interesting escape hatch, and it's why the build spec can honestly say "4 K" at all. Nb₃Sn has a superconducting transition temperature and a superheating field roughly *twice* niobium's, which means it holds a high Q at a much warmer temperature. The measured results are real, not hypothetical:

- Cornell's single-cell Nb₃Sn cavities reached, at 4.2 K, an average **Q₀ of 8 × 10⁹ at the quench field** ([Fermilab review, FNAL-PUB-17-133](https://lss.fnal.gov/archive/2017/pub/fermilab-pub-17-133-td.pdf)).
- Fermilab-coated CEBAF cavities hit **Q₀ = 10¹⁰ at 4.4 K** at a 10 MV/m gradient.
- The payoff is enormous where it hurts most: moving from 2 K niobium to 4.4 K Nb₃Sn while holding Q₀ in the 10¹⁰–10¹¹ range can **cut cryogenic energy consumption by roughly an order of magnitude** ([same review](https://lss.fnal.gov/archive/2017/pub/fermilab-pub-17-133-td.pdf)) — which, on a vehicle where cryogenics *is* the dominant mass and power, is close to decisive.

But Nb₃Sn extracts a price, and it's paid in gradient. The best Nb₃Sn R&D cavities quench around **14–24 MV/m**, roughly *half* the field that bulk niobium can hold. So the material fork is real and unavoidable: **niobium buys you field strength but demands 2 K; Nb₃Sn buys you 4 K but surrenders half your gradient.** Either way — and this is the point that matters for the whole thesis of the project — *the cold is the wall.* You cannot design your way out of it at the cavity; you can only choose which face of it to fight.

## The gradient ceiling: how hard you can push one cell

Gradient — the accelerating field the cavity can sustain — sets the ceiling on how much energy you can store in a single cell before it fails, and therefore how much thrust headroom each cell has before you're forced to add more of them.

For bulk niobium the ceiling is now well characterized and close to fundamental. The best 1.3 GHz cavities reach **45–50 MV/m**, with a hard-won record of **49 MV/m in continuous-wave operation** achieved through a two-step 75 °C/120 °C vacuum bake ([Grassellino et al., arXiv:1806.09824](https://arxiv.org/pdf/1806.09824)). The limit is physical, not procedural: at those fields the peak magnetic field at the cavity wall reaches ~200–210 mT, right up against niobium's **superheating field**, beyond which magnetic vortices penetrate the surface, dump energy as heat, and collapse the Q — the cavity *quenches*. Bulk niobium is, in the field's own phrasing, "approaching its fundamental limitations."

For our craft this ceiling is comfortably high: 240 N per cell needs only ~1 kW of continuous feed, far below the stored-energy limit even of an Nb₃Sn cell running at its more modest ~14 MV/m. So gradient isn't what caps the *nominal* design — but it's what caps the *upgrade path.* If you ever want much more thrust per cell (to shrink cell count and mass), you run into the superheating field, and the only doors past it are exotic thin-film multilayers (MgB₂, NbTiN) or traveling-wave geometries — active research, not shelf technology. The cavity, in other words, has a known and unforgiving speed limit.

## The three demons: keeping a cavity working is harder than making one

Building a Q = 10¹⁰ cavity is a solved art. *Keeping* one at Q = 10¹⁰ while it's bolted to a vibrating, flying machine is where the real fight is. Three specific enemies:

**1. Detuning — the silent thrust-killer.** A resonant cavity only works *on* resonance. Drift the frequency by even a few hertz and the field collapses — and with it, per the thrust law, the force goes to *zero.* Two things constantly try to detune it: **Lorentz detuning** (the RF field's own radiation pressure physically deforms the cavity walls) and **microphonics** (every vibration on the craft — pumps, the generator, aerodynamic buffeting — shakes the cavity geometry). This is why every cell carries a mandatory **piezoelectric tuner** driven by a fast low-level RF (LLRF) control loop, squeezing the cavity thousands of times a second to hold it exactly on resonance. On this craft the danger is acute and specific: the turbo-generator's vibration can microphonically detune the cells, which is why the cryostat has to be mechanically isolated from the engine. A tuner that fails is a thruster that silently stops making thrust — arguably the single most dangerous failure mode on the vehicle, precisely because it's invisible until the craft drops.

**2. Quench — the fast, violent failure.** If a cell exceeds its gradient limit, or a defect on the surface heats up, the superconductor goes normal in a fraction of a millisecond. The ten-billion-fold stored field dumps its energy into the wall as heat, boiling helium and producing a sharp thrust transient. Quench protection is therefore safety-critical: the control system watches every cell's reflected RF power and temperature, and on the first sign it must trip that cell and reallocate its load to neighbors **within milliseconds**, without letting the local heat cascade to adjacent cells. This is exactly the failure our flight-control simulation stress-tests — and survives 100% of the time across a Monte-Carlo campaign losing up to eight cells at once.

**3. Field emission and multipactor — the cleanliness demons.** The reason SRF cavity fabrication reads like a surgical ritual — buffered chemical polish, an 800 °C hydrogen-degassing bake, a final electropolish, a high-pressure ultrapure-water rinse in a cleanroom, clean assembly — is that a single micron-scale particle or surface contaminant on the RF surface becomes a field-emission site that bleeds away the field and caps the gradient. **Multipactor** — a resonant avalanche of electrons ping-ponging off the walls in phase with the RF — is a related menace that can lock a cavity out of its operating band entirely. Neither is exotic; both are why you cannot build one of these in a normal machine shop. The Q you can *achieve* is set by the physics; the Q you actually *get* is set by how clean your last rinse was.

## The strange verdict: most speculative, most mature

Step back and the cavity chamber is the most paradoxical object on the whole craft.

It is the **most speculative** component: everything about whether this vehicle can *ever* fly comes down to one unmeasured number — the efficiency η of a horizon effect that mainstream physics does not accept exists, and that the Dresden/Tajmar null results on the EmDrive give us every reason to doubt. The cavity is where that bet is placed. If η is really zero, the most beautiful cone ever machined produces exactly nothing.

And yet it is also, hardware-for-hardware, the **most mature** component. A superconducting RF cavity holding Q = 10¹⁰ is not a thing we hope to build — it's a thing accelerator labs build routinely and have for decades. The niobium, the 2 K or 4 K choice, the 50 MV/m ceiling, the tuners and LLRF loops and quench protection — all of it is catalogued, measured, sourced, and understood. The moment the physics ever came through, the cavity would be the *easiest* exotic part of the machine to actually make, because it isn't exotic at all.

That's the honest shape of it. The cavity chamber asks the one question the whole enterprise can't yet answer — *does shaping the vacuum push?* — and answers, entirely on its own, every question about *how you'd build the thing that asks it.* The physics is a coin still in the air. The engineering, remarkably, has already landed.

---

## Sources

- M.E. McCulloch, *Testing quantised inertia on the EmDrive* — asymmetric-Unruh mechanism in a tapered cavity + the falsifiable thrust-reversal prediction. [arXiv:1604.03449](https://arxiv.org/abs/1604.03449)
- A. Grassellino et al., *Unprecedented quality factors at accelerating gradients up to 45 MV/m in niobium … via low-temperature nitrogen infusion* — BCS surface resistance and high-Q treatments at 1.3 GHz, 2 K. [arXiv:1701.06077](https://arxiv.org/pdf/1701.06077)
- *Accelerating fields up to 49 MV/m in TESLA-shape SRF niobium cavities via 75 °C vacuum bake* — bulk-Nb gradient ceiling and the ~200 mT superheating limit. [arXiv:1806.09824](https://arxiv.org/pdf/1806.09824)
- S. Posen & D.L. Hall, *Nb₃Sn superconducting radiofrequency cavities* (Fermilab review) — Nb₃Sn Q₀ ≈ 10¹⁰ at 4.2–4.4 K, quench-field results, and the ~order-of-magnitude cryogenic-energy saving. [FNAL-PUB-17-133](https://lss.fnal.gov/archive/2017/pub/fermilab-pub-17-133-td.pdf)

*A note on honesty, carried through from the companion pieces: the physics premise here (that a shaped cavity produces thrust by modifying inertia) is open and unconfirmed — this deep dive assumes it, and everything about the cavity's fabrication, temperature, gradient, and failure modes is real, sourced accelerator engineering. What isn't real yet is the thrust law itself: whether the effect exists at all, and whether it scales linearly with Q up to 10¹⁰ (η's value rides on both). Everything else — the niobium, the 2 K vs 4 K choice, the gradients, the tuners — already exists.*
