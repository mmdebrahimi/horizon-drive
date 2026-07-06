# Detailed Engineering Instructions — A Working Horizon-Drive Craft (effect ASSUMED proven)

> Captured 2026-07-04. Suspend-disbelief engineering build. **Premise: Phase-3 of the test program has succeeded — the inertia/horizon-drive thrust is real and scales as F ≈ η·P·Q/c up to superconducting Q.** These are the build instructions for a *working* 1-ton-class thruster/craft. Budget verified `/tmp/craft.py`. Companion to the test-rig roadmap (`antigravity-device-engineering-roadmap-2026-07-04.md`).
> Honest header: granting the physics, the thrust is the *easy* part. The build is dominated by two constraints the physics doesn't remove — **cryogenic mass/power** (you need Q≈10¹⁰ → superconducting Nb → 4 K) and **energy storage** (endurance). The instructions below are engineered around those two walls.

---

## 0. Design targets & the budget that shapes everything

**Target:** a 1,000 kg craft, thrust-to-weight 1.5 (useful flight, not just hover) → **F_total ≈ 14.7 kN**.

**Per-cell thrust** (F = η·P·Q/c, η=0.0072, Q=10¹⁰): **240 N per 1 kW cell.** So:
- Hover: ~41 cells / ~41 kW. Design (TWR 1.5): **62 cells / 62 kW RF.**

**The verified budget (this is the real engineering, not the physics):**

| Subsystem | Value | Note |
|---|---|---|
| RF power | **62 kW** | 62 × 1 kW cells |
| **Cryogenics** | **61 kW** | keeping Nb at 4 K: COP ≈ 0.002 → **~493 W input per W lifted**; ~124 W heat leak |
| Control/avionics | 3 kW | |
| **Total electrical** | **~126 kW** | |
| Core **dry mass** | **~1,100 kg** | cells 186 + cryostat 120 + **cryocoolers 489** + RF amps 93 + structure 180 + avionics 40 |

**The two walls, quantified:**
1. **Cryogenics dominates dry mass** (~490 kg of cryocoolers alone). This is *the* design driver — everything below is arranged to minimize the 4 K heat load.
2. **Energy storage sets endurance.** At 126 kW: Li-ion gives **~10 min per ~85 kg**, but **~60 min needs ~505 kg** of battery — which, with the ~1,100 kg dry mass, *does not close* for a 1-ton vehicle. **Honest consequence: a genuinely flyable craft is either (a) larger (2–3 t class), (b) short-endurance/tethered, or (c) fuelled** (a turbo-generator gives 60 min for ~63 kg of fuel — the only endurance path that closes at 1 ton).

**So the device you actually build is:** a superconducting thruster array + its cryoplant + a *fuelled* generator (not batteries) + flight control + a lightweight frame — engineered relentlessly to cut the 4 K heat leak. Build it module-by-module below.

---

## 1. Module A — The thrust cell (the core unit)

Build and qualify **one perfect cell first**; the craft is an array of identical cells.

**A.1 Cavity fabrication (SRF practice):**
- Material: bulk niobium, RRR ≥ 300, ~3–4 mm wall. Geometry: truncated cone (frustum), big-end Ø ≈ 0.16 m, small-end Ø ≈ 0.09 m, length ≈ 0.12 m (per-cell scaled down from the test frustum; the taper asymmetry is the thrust-producing "horizon").
- Forming: deep-drawn or spun half-shells + electron-beam welding under vacuum (SRF-grade welds — no inclusions).
- Surface processing (this sets Q): (1) bulk **buffered chemical polish (BCP)** or **electropolish (EP)** removing ~150 µm; (2) **high-temperature vacuum bake** (600–800 °C) to degas hydrogen; (3) light EP; (4) **high-pressure ultrapure-water rinse** in a cleanroom; (5) clean assembly. Target **Q₀ ≈ 10¹⁰ at 2–4 K.**

**A.2 RF coupler + tuner:**
- Input power coupler: adjustable antenna set near critical coupling for ~1 kW throughput; ceramic RF window rated for the power; thermally intercepted at cryo stages to cut heat leak.
- **Frequency tuner (mandatory):** a piezo/stepper tuner deforming the cavity ~kHz range to hold resonance against thermal/Lorentz detuning. A cavity off-resonance produces **zero thrust** — the tuner is not optional.
- Field probe (pickup antenna) → the per-cell control loop.

**A.3 Per-cell spec (qualify each before array install):**
- f₀ = 1.3 or 2.45 GHz (pick one array-wide), loaded Q measured on a VNA, ≥ 10¹⁰ at operating T.
- Verified thrust on the qualification balance ≈ 240 N at 1 kW (± tolerance) — *each cell is thrust-tested individually* before it flies.
- Quench threshold characterized (max stored energy before the superconductor goes normal).

---

## 2. Module B — The thruster array & vectoring

- **Layout:** 62+ cells (include spares/margin → build ~72) in a hexagonal close-packed grid on the craft's underside, thrust axis nominally down. Group into ≥3 independently-controllable sectors for attitude.
- **Vectoring by differential thrust:** you steer by modulating **per-cell (or per-sector) RF amplitude/phase**, not by gimbals. More thrust on one side → pitch/roll; net lateral component → translation. This is fly-by-wire thrust-vectoring with no moving aero surfaces.
  - Roll/pitch: differential sector amplitude.
  - Yaw: if cells are canted slightly tangentially, differential yields a torque couple; else add dedicated canted yaw cells.
  - Vertical: common-mode amplitude.
- **Response bandwidth:** RF amplitude can be modulated in microseconds, but **thermal/tuner settling** limits real thrust-slew to ~10–100 Hz — fast enough for flight control, but the control law must respect it.
- **Manifolding:** each cell = its own cryo intercepts, RF feed, control channel. Modular "line-replaceable" cell cartridges for maintenance.

---

## 3. Module C — RF power chain

- **Per-cell solid-state amplifier** (GaN), ~1–1.2 kW, phase- and frequency-controllable. 62 units + spares. (~1.5 kg/kW → ~93 kg.)
- **Master oscillator + phase-locked distribution:** one reference; each cell's amp locked to it with a commanded phase offset (for vectoring) and a per-cell tracking loop to the cavity resonance (LLRF — low-level RF control, standard in accelerators).
- **LLRF controller per cell:** reads the field probe, drives amplitude/phase + tuner to hold on-resonance at commanded amplitude. This is mature accelerator technology.
- Directional couplers on every feed for forward/reflected monitoring (reflected power spike = detuning or quench precursor).

---

## 4. Module D — Cryogenic system (the mass driver — engineer hardest here)

- **Cryostat:** the cell array shares a common vacuum vessel + multilayer-insulation (MLI) + an actively-cooled thermal shield (~40–80 K) intercepting radiation before the 4 K stage. Minimizing 4 K heat leak is the whole game (every watt at 4 K costs ~500 W of compressor).
- **Coolers:** distributed **pulse-tube or Gifford-McMahon cryocoolers** (each ~1–2 W at 4 K), or a small **central helium refrigerator** if the array is large. Budget ≈ 124 W at 4 K → ~61 kW compressor input → **~490 kg** — the dominant dry mass.
- **Heat-leak reduction program (do all of these):** low-conductivity composite cell supports; RF coupler thermal intercepts at 40 K and 4 K; vapor-cooled or HTS current leads; MLI optimization; minimize RF wall dissipation by keeping Q high and coupling critical.
- **Cooldown procedure:** pump cryostat to high vacuum → stage-cool shield to ~50 K → cool cells to 4 K slowly (thermal-stress limited, watch weld regions) → verify Q per cell → arm RF only after all cells superconducting and tuned.
- **Design escape hatch (note honestly):** if a proven higher-Q or higher-η reduces the RF power, the cryo load and mass drop proportionally — the single highest-leverage improvement to make the craft lighter is *less required power*, which shrinks *both* the RF and cryo masses.

---

## 5. Module E — Electrical power source (the endurance wall)

- **Hover/flight load ≈ 126 kW.** Source choice is the endurance decision:
  - **Batteries (Li-ion, 250 Wh/kg):** ~10 min for ~85 kg; **60 min = ~505 kg** → does *not* close at 1 t. Use only for a short-hop / demonstrator.
  - **Hydrogen fuel cell (~500 Wh/kg system):** ~60 min for ~250 kg — marginal.
  - **Fuelled turbo-generator (~2 kWh/kg incl. fuel):** **60 min for ~63 kg of fuel** — the endurance path that *closes* at 1 ton. Recommended for a real vehicle: a compact gas-turbine or diesel genset supplying the ~126 kW bus.
- **Power bus:** HVDC distribution to the 62 RF amps + cryocooler compressors; hefty conductors, contactors, and a battery buffer for transients + safe shutdown.

---

## 6. Module F — Thermal rejection

- ~126 kW electrical in → nearly all becomes **waste heat** (RF amp losses + cryocooler compressor heat + generator heat). This must be rejected or the craft cooks.
- Liquid-cooled cold plates on the RF amps + cryocooler warm ends → radiators/heat exchangers. In atmosphere, forced-air/liquid radiators; the airflow from any propellers is absent here, so dedicated fans/ducts.
- Waste-heat mass + drag is a real budget line — size radiators for the full 126 kW.

---

## 7. Module G — Flight control

- **Sensors:** IMU (3-axis gyro+accel), barometric + radar altimeter, GPS/INS, and — critically — **load cells / thrust-per-sector telemetry** so the controller knows actual thrust, not commanded.
- **Control law:** a standard multirotor-style controller *maps* attitude/position commands → per-sector thrust demands → per-cell RF amplitude/phase, respecting the ~10–100 Hz thrust-slew limit. Cascaded PID or LQR/MPC; the array is over-actuated (62 cells → 6 DOF) so use control allocation with cell-health weighting.
- **Redundancy:** lose a cell → reallocate to neighbors (over-provision ~15% thrust margin so any single-cell or single-sector fault is survivable — like a multirotor losing a motor).
- **Stability:** thrust responds faster than a rotor but the craft is still an unstable inverted-pendulum in hover → the flight computer is load-bearing for safety; triple-redundant.

---

## 8. Module H — Structure & integration

- **Frame:** CFRP space-frame carrying the cryostat (below), generator + tanks (CG-centered), avionics, radiators; ~180 kg budget.
- **Mass discipline:** the budget is *tight* (dry ~1,100 kg vs 1,000 kg target) — every subsystem is mass-policed; expect the first real vehicle to be **2–3 t class** with meaningful payload, shrinking toward 1 t only as cryo/power efficiency improves.
- **CG & vibration:** keep CG below the thrust plane for pendulum stability margin; isolate the cryostat from generator vibration (microphonics detune SRF cavities — a real coupling between the generator and the cells).

---

## 9. Assembly & commissioning sequence (step-by-step)

1. **Fabricate + SRF-process + individually thrust-qualify** every cell (Module A). Reject any below spec.
2. Build the cryostat; install cells with low-conductivity supports + thermal intercepts; leak-check to UHV.
3. Integrate RF chain; bench-test each amp + LLRF loop warm.
4. **Cooldown** to 4 K; verify Q and tune every cell; measure per-cell + array thrust on a ground thrust-stand (craft bolted down).
5. Integrate power (generator + bus), thermal rejection, avionics, flight computer.
6. **Ground thrust-stand test:** full-array thrust vs command; vectoring authority; quench/fault injection; verify control allocation + redundancy.
7. **Tethered hover:** craft on a safety tether/gantry, lift a few cm, close the flight-control loop, tune gains, test single-cell-fault reallocation.
8. **Free hover → translation → envelope expansion**, incrementally, with abort/tether recovery at each step.

---

## 10. Safety & failure modes (non-negotiable)

- **Quench:** a cell going normal dumps its stored EM energy as heat + a thrust transient → detect (reflected-power/temperature) in ms, trip that cell, reallocate. Design quench-energy handling so it can't cascade.
- **Cryogenic:** helium inventory → O₂-displacement/asphyxiation monitoring; over-pressure relief; cold-burn PPE; quench-induced boil-off venting.
- **RF:** 60+ kW of microwave power — fully enclosed, interlocked, leakage-surveyed; no exposure.
- **Power/thermal:** HVDC arc-flash protection; 126 kW of waste heat → thermal-runaway interlocks.
- **Flight:** unstable in hover → triple-redundant flight computer + IMU; ballistic-parachute or tether for the demonstrator; geofenced, uncrewed first.

---

## 11. The honest engineering verdict (even granting the physics)

Assume the effect is completely real and scales as advertised. **The thrust is then the easy part.** What actually gates a working craft:

1. **Cryogenics.** Needing Q≈10¹⁰ forces 4 K superconductors, whose cooling costs ~500 W per watt lifted — ~490 kg and 61 kW on a 1-ton craft. This single fact means a true 1-ton vehicle is *marginal*; a first real craft is 2–3 t class.
2. **Energy storage.** 126 kW × useful endurance only closes with a **fuelled generator**, not batteries. A battery version is a minutes-long demonstrator.
3. **The highest-leverage improvement is not more thrust — it's more thrust *per watt*** (a better η or usable higher Q at higher temperature). Every watt saved shrinks RF *and* cryo mass. If a proven effect turns out stronger than the calibrated Eagleworks η, all these budgets ease dramatically and the craft gets light.

So the buildable device — even in the best case where the physics is handed to you — is a **superconducting thruster array + cryoplant + fuelled generator + fly-by-wire thrust-vectoring**, most credibly first realized as a **tethered / short-endurance multi-ton demonstrator**, shrinking toward a practical 1-ton "flying car" only as cavity efficiency and cryogenic mass improve. The elegant part (silent, propellant-less thrust) is real in this scenario; the unglamorous parts (cryo mass, kilowatts, waste heat) are what the engineering fight is actually about.

---

## Appendix — verified budget (script `/tmp/craft.py`, exit 0)
| Quantity | Value |
|---|---|
| Thrust per 1 kW cell (Q=10¹⁰) | 240 N |
| Cells for TWR 1.5 (1 t) | 62 (hover: 41) |
| RF power | 62 kW |
| Cryo COP at 4 K | ~0.002 (493 W in per W lifted) |
| Cryo compressor power | ~61 kW |
| Total electrical | ~126 kW |
| Core dry mass | ~1,100 kg (cryocoolers ~490 kg dominate) |
| Battery for 60 min | ~505 kg (doesn't close) |
| Fuelled generator for 60 min | ~63 kg fuel (closes) |
