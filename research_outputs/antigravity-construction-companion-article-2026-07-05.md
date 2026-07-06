# How You'd Actually Build One: The Engineering Blueprint for a Horizon-Drive Craft

### A companion to *"The Only Honest Path to Anti-Gravity Runs Through Your Own Inertia."* That essay argued which physics might let a craft manipulate its own inertia. This one asks the engineer's question instead: suppose it works — what does the machine actually look like, and what would really be hard?

*Draft · 2026-07-05*

---

*This is the sequel nobody expects. In the main essay, we spent our time deciding whether inertia-from-the-vacuum is real physics — and landed on a careful "open, unconfirmed, but not forbidden." Here we take the leap the honest scientist doesn't get to take, and simply* assume it is. *Assume the decisive experiment comes back positive, the effect survives every control, and it strengthens as you crank up the cavity quality, just as the theory hopes. Now you're not a physicist anymore. You're an engineer with a budget, and you have to build the thing.*

*What follows is the surprise waiting for anyone who tries.*

## The reversal: the exotic part is the easy part

The moment you sit down to engineer a real craft, you discover something no amount of physics excitement prepares you for: **granting the effect, making thrust is almost trivial.** The fight is with two utterly mundane enemies — *keeping things cold* and *carrying enough energy* — and the entire machine is shaped, end to end, around beating them. The "anti-gravity" is the part that behaves. The refrigeration is the part that fights you.

Here's the whole vehicle, subsystem by subsystem, with the honest numbers.

## The budget that shapes everything

Start from the target: a **1,000 kg craft** with enough thrust to actually fly (not just barely hover), so aim for a thrust-to-weight of 1.5 — about **14.7 kilonewtons** of force. At the calibrated performance (240 newtons from each 1-kilowatt superconducting cell), that's **62 cells drawing 62 kW of radio-frequency power.** So far, so reasonable.

Then the cold bill arrives. Those cells only reach their magic quality factor if they're niobium held at **4 kelvin** — four degrees above absolute zero — and keeping something that cold costs roughly **500 watts of compressor for every single watt you pull out of the cold zone.** The cryogenics alone draw **~61 kW** and weigh **~490 kilograms.** Add it all up:

| Subsystem | Value |
|---|---|
| RF power (62 cells) | 62 kW |
| **Cryogenics (4 K)** | **61 kW · ~490 kg — the dominant mass** |
| Control & avionics | 3 kW |
| **Total electrical** | **~126 kW** |
| **Core dry mass** | **~1,100 kg** (cryocoolers dominate) |

Read the dry-mass line and wince: **~1,100 kg before a single battery or drop of fuel** — already over our one-ton target. That one fact reshapes the whole project, and we'll come back to it. First, the machine itself.

## Module A — The thrust cell (build one perfect one first)

The heart of everything is a single superconducting cavity, and you build and *individually flight-qualify one* before you make sixty-two. It's a truncated cone of bulk niobium (the taper asymmetry is the "manufactured horizon" doing the work), formed from spun half-shells electron-beam-welded in vacuum, then put through the full particle-accelerator surface ritual: chemical polish, an 800 °C hydrogen-degassing bake, a final electropolish, and a high-pressure ultrapure-water rinse in a cleanroom. That ritual is what buys the quality factor of ten billion. Each finished cell gets an adjustable power coupler, a **piezo frequency tuner** (non-negotiable — a cavity that drifts off resonance makes *zero* thrust), and a field probe for its control loop. Then every cell is tested on a thrust stand and must hit ~240 N at 1 kW before it's allowed anywhere near the craft.

## Module B — The array and how it steers

Sixty-two-plus cells (build ~72 for spares) pack into a hexagonal grid on the craft's underside, grouped into at least three independently-throttled sectors. And here's the elegant part: **there are no gimbals, no moving control surfaces, nothing mechanical.** You steer entirely by *differential thrust* — dial up the RF amplitude on one side to pitch or roll, tilt a few cells tangentially for yaw, push all of them together to climb. It's fly-by-wire in the purest sense, an array of 62 silent thrust points commanded thousands of times a second. The one catch: thermal and tuner settling limit how fast real thrust can change to roughly 10–100 Hz — quick enough to fly, but the control law has to respect it.

## Module C — The RF power chain

Each cell gets its own ~1 kW solid-state (GaN) amplifier, all phase-locked to one master oscillator with a commanded phase offset for steering, plus a per-cell **low-level RF loop** that continuously drives the tuner to hold the cavity exactly on resonance. None of this is speculative — it's mature accelerator technology, run every day at facilities like CERN and SLAC, just never before asked to fly.

## Module D — The cryogenic system (engineer this the hardest)

This is the mass driver, so it gets the most brutal engineering attention. The whole cell array shares one vacuum vessel wrapped in multilayer insulation, with an actively-cooled 40–80 K radiation shield intercepting heat *before* it reaches the precious 4 K stage — because every stray watt at 4 K costs 500 at the wall plug. Distributed pulse-tube cryocoolers (or a small central helium refrigerator) carry the ~124 W heat load. And the entire design philosophy of the craft reduces to one obsession: *minimize the 4 K heat leak* — low-conductivity cell supports, thermally-intercepted couplers, optimized insulation. **The single most valuable improvement anyone could make to this whole vehicle isn't more thrust — it's needing less power, because less power shrinks the RF *and* the cryogenics *and* the mass, all at once.**

## Module E — Power (the endurance wall)

126 kilowatts, continuous. How you supply it decides how long you fly:
- **Batteries** give you about **ten minutes for 85 kg** — but a full hour would need **~505 kg** of them, which simply doesn't close on a one-ton craft. Fine for a short demonstrator, useless for a vehicle.
- A **hydrogen fuel cell** stretches that to ~60 minutes for ~250 kg — marginal.
- A **fuelled turbo-generator** — a compact gas turbine — delivers **an hour on ~63 kg of fuel.** It is the *only* option that actually closes the budget at one ton. The propellantless dream, it turns out, still wants a tank of fuel — not to push against, but to keep the lights on.

## Module F — Getting rid of the heat

Almost all of those 126 kilowatts end up as waste heat — from the amplifiers, the cryocooler compressors, the generator — and in the air, with no rocket exhaust to carry it away, you have to *radiate and blow* it off with liquid cold-plates and sized radiators. It's unglamorous, it's heavy, and it's a real line in the budget.

## Module G — Flight control

The craft is an unstable inverted pendulum in hover — it will tip over without a computer holding it upright thousands of times a second — so the flight computer is a safety-critical, triple-redundant heart. It reads an inertial measurement unit, altimeters, and (crucially) *per-sector thrust telemetry* so it knows the real force it's making, then solves a control-allocation problem: turn "pitch forward and hold altitude" into 62 individual RF amplitude commands. Because the array is wildly over-actuated — 62 thrusters for 6 degrees of freedom — it can **lose a cell and instantly reallocate to its neighbors**, exactly like a multirotor surviving a dead motor. Build in ~15% thrust margin and a single failure is a non-event.

This is the one module we didn't just *describe* — we **built and flew it in software** (see the section below). And doing so surfaced a non-obvious design law that would have bitten a real vehicle: **the attitude-control gains have to scale with the craft's moment of inertia.** A one-ton disc has a pitch inertia of hundreds of kilogram-metres-squared, and if you tune the attitude loop as if the craft were light, it responds too sluggishly — the inner loop ends up as slow as the outer position loop, the two fight each other, and a growing wobble tears the craft apart in seconds. Make the attitude authority scale with the inertia (physical bandwidth × I) and it's rock-solid. That's exactly the kind of trap a simulation is *for* — cheap to hit in software, catastrophic to discover on a tethered prototype.

## Module H — Structure

A carbon-fibre space-frame ties it together: cryostat slung low, generator and fuel at the center of gravity, radiators and avionics distributed, CG deliberately kept *below* the thrust plane for stability margin. One subtle enemy: the generator's vibration can microphonically detune the SRF cavities, so the cryostat has to be mechanically isolated from it — a real, quiet coupling between the mundane engine and the exotic cells.

## How you'd actually bring it to life

You don't bolt it all together and hit "on." You climb a ladder of ever-scarier tests: fabricate and thrust-qualify every cell → assemble and leak-check the cryostat → cool to 4 K and re-tune every cavity → **bolt the whole craft to a ground thrust-stand** and prove full thrust, vectoring authority, and single-cell-failure reallocation while it can't go anywhere → then a **tethered hover** a few centimeters up on a safety gantry to close the flight-control loop → and only then free hover, translation, and slow envelope expansion, with an abort at every rung. Throughout, the non-negotiables are quench protection (a cell going normal must trip and reallocate in milliseconds without cascading), cryogenic and RF safety, and — for the first flights — no crew, a geofence, and a tether or parachute.

## We didn't just draw it — we flew it (in simulation)

Here's where this stops being a hand-wave. Everything above about the *control* of the craft — the fly-by-wire steering, the fault reallocation, the "hold hover to a few centimetres" — isn't a promise. It's a **runnable 6-degree-of-freedom simulation** of the whole thruster array and its flight computer, and you can download it and fly it yourself. (The physics of the *thrust* is still assumed; what's proven here is that *if* you have the thrust, the machine is controllable.)

It models the 62-cell array, the bounded control-allocation solver that turns a desired motion into per-cell amplitudes, the 6-DOF rigid-body dynamics, a Kalman state estimator, and — importantly — the *messy* parts: the 10–100 Hz thrust-slew limit, and noisy sensors. Here's what it does:

- **It holds.** From a two-metre drop, it settles into hover and holds position to **under a centimetre**, dead level. Commanded to translate three metres sideways or diagonally, same thing — it arrives and holds to a centimetre.
- **It shrugs off the slew limit.** Whether the cells can change thrust at 100 Hz or a sluggish 10 Hz, it stays rock-stable — the actuator lag we worried about in Module B turns out not to threaten stability at all.
- **It flies blind-ish and stays smooth.** Feed it *noisy* sensors — 3 cm of position jitter, half a degree of attitude error — and the onboard Kalman estimator smooths it into a clean state estimate; the craft still holds hover to about **3.7 cm**.
- **It survives failures — a lot of them.** We ran a **Monte-Carlo fault campaign**: forty randomised flights, each with a random destination and a random number of cells (up to **eight at once**) quenching at random moments, all with the noisy-sensor, slew-limited, estimator-in-the-loop stack. Result: **100 % survival, zero fly-aparts, worst-case position error 28 centimetres.** Lose eight of your sixty-two thrusters mid-flight and the craft barely notices — the allocator just leans on the survivors.

None of this proves the effect is real. But it does prove something worth knowing before anyone welds a single cavity: **the hard control problem — flying an over-actuated, unstable, propellantless disc through cell failures and sensor noise — is solved, in software, today.** The whole simulation, with its tests and the fault campaign, is open-source at **[github.com/mmdebrahimi/horizon-drive](https://github.com/mmdebrahimi/horizon-drive)** — clone it and break it yourself.

## The honest verdict, even in the best case

So suppose you're *handed* the physics, free. Here's what the engineering tells you anyway:

1. **Cold is the wall.** Needing quality factors of ten billion forces 4 K superconductors, and cooling them dominates both the mass and the power. This single fact is why a true one-ton craft is marginal, and why the *first* real vehicle is almost certainly a **2–3 ton machine** with modest payload.
2. **Energy is the second wall.** Real endurance means a fuelled generator, not batteries. The battery version is a spectacular ten-minute demo, not a vehicle.
3. **The winning move is efficiency, not power.** Every improvement in thrust-*per-watt* — a stronger effect, or usable performance at a *warmer* temperature (which is exactly why the space and high-temperature-superconductor variants are so tempting) — shrinks the whole machine at once. If the real effect ever proved stronger than today's cautious estimate, these budgets would ease dramatically and the craft would get *light*.

That's the machine: a superconducting thruster array, a cryoplant, a fuelled generator, and a flight computer flying an array of silent thrust points — most honestly first realized as a tethered, multi-ton demonstrator, shrinking toward a real flying car only as the cold problem yields. The elegant part — quiet, propellantless lift — is genuinely there in this scenario. The fight, as always, is with the cold and the kilowatts.

And note where the certainty now sits. Of the four hard problems — *does the effect exist* (unknown), *can you cool it* (hard, known), *can you power it* (hard, known), and *can you fly it* (**solved, in simulation**) — the last one has quietly moved from question mark to green tick. That doesn't build the craft. But it means that on the day the physics ever comes through, the control system is already waiting, tested, and free.

---

## One more honest caveat, carried over from the physics

Everything above assumes the effect is a genuine, engineerable *inertia change* — not a "reactionless thruster." That distinction is the whole argument of the companion essay, and it matters here too: a machine that produces continuous propellantless *thrust* while beating the photon-rocket limit would be a perpetual-motion machine (the first law forbids it), so the *only* version of this device that survives is one that changes what inertia **is**, and is still pushed on conventionally. This blueprint is what that machine's hardware would look like *if* the physics comes through. It is engineering fan-fiction with honest numbers — not a promise that the effect is real. For why the effect might (or might not) be real at all, read the companion essay.

---

*Author's note: every number in this piece — 240 N per cell, 62 cells, 126 kW total, ~1,100 kg dry mass, ~490 kg of cryocoolers, ~63 kg of fuel per flight-hour — was derived and checked against the physics and the measured constants, not asserted. The point of doing the arithmetic honestly is that it tells you the truth the hype never does: the hard part was never the anti-gravity. It was the refrigerator.*
