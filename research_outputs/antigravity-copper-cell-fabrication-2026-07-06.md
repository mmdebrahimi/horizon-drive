# Building the Inertia-Modifying Element: Step-by-Step Fabrication of a Copper Thrust Cell

**Compiled 2026-07-06 · Soraya (conversational-executor) · the hands-on fabrication front end of `antigravity-phase1-buildspec-2026-07-06.md`**

> **Read this box before anything else — it decides whether this is honest or not.**
>
> 1. **This is the *testable* element, not a working thruster.** A room-temperature copper cavity has Q ≈ 27,000 (verified in `copper_cavity_fab_calc.py`), so the predicted force at 10 W is **~12 micronewtons** — a signal you *measure on a balance*, not a push you feel. The 240 N/kW "thruster" needs Q = 10¹⁰, which is only reachable in **niobium at 4 K** (a national-lab SRF capability — **not** covered here, and not a garage build).
> 2. **The physics is still an assumption.** Building this cell does not make inertia-modification real. It builds the object the decisive experiment tests. A clean null is the likely — and still valuable — outcome.
> 3. **Two hard boundaries I will not cross for you:** (a) **money** — every purchase below is yours to make; I spec, you buy. (b) **the niobium/HF/cryogenic tier** — chemical polishing uses hydrofluoric acid (lethal), plus an 800 °C vacuum furnace and cryogens; that is specialist work for an equipped lab with trained staff, and this guide deliberately stops at copper.
>
> With that honest: here is how you actually make one.

---

## What you are building

A **single copper resonant thrust cell** — a truncated-cone (frustum) microwave cavity, big-end Ø160 mm / small-end Ø90 mm / length 120 mm, resonating in the **TM010 mode near 1.84 GHz**, with a tunable plunger, an RF coupling port, and a field-pickup probe. This is Module A of the craft at the *buildable* tier. Build **one perfect one** before you ever think about an array.

**Verified design numbers** (`python copper_cavity_fab_calc.py`):

| Quantity | Value |
|---|---|
| TM010 resonant frequency | **1.836 GHz** |
| Expected room-temp copper Q₀ | **~27,000** |
| Skin depth at 1.84 GHz | 1.52 µm (→ surface finish is critical) |
| Surface resistance Rₛ | 11 mΩ |
| Wall heat to remove at 10 W drive | 10 W |
| Predicted thrust (assumed effect, 10 W) | ~12 µN |

---

## Bill of materials (you purchase — I do not)

**Cavity body**
- OFHC (oxygen-free high-conductivity) copper, **C10100 or C10200** — one billet ≥ Ø180 mm × 150 mm for the body, plus plate for the two end caps. (OFHC matters: it takes a mirror polish and has the conductivity the Q depends on.)
- Optional: bright-acid-copper or silver electroplating service for the final internal surface (buys you ~10–15 % Q).

**Tuning & ports**
- Copper tuning plunger (threaded, Ø ~20 mm) + a fine-pitch brass lead-screw + locknut.
- 2× N-type or SMA panel connectors (one drive, one pickup) with copper coupling loops/antennas you'll size during tuning.
- PTFE or alumina feedthrough insulators for the ports.

**Fasteners & sealing**
- Silver-plated brass bolts (non-magnetic) for the end caps.
- RF gasket: a copper or silver-plated spring C-gasket, **or** plan to solder/e-beam the caps if you want a permanent joint. (Bolted-with-RF-gasket is the serviceable choice for a first article.)

**Metrology / drive** (shared with the Phase-1 rig)
- Vector Network Analyzer (VNA) covering 1–3 GHz — **the single most important instrument**; it measures resonance and Q.
- Signal generator + **10–15 W GaN amplifier** at 1.84 GHz, directional coupler, matched load, circulator.
- RF detector / power meter.

---

## Tools & facility

- **CNC lathe + mill** (or a skilled manual machinist) — the frustum bore and the flat sealing faces need real accuracy.
- Fine boring bar, form tools; a **diamond-turning or fine-polishing** capability for the internal cone surface (skin depth is 1.5 µm — surface roughness directly costs Q).
- Metrology: bore gauge, CMM or good calipers + depth mic; surface-roughness gauge if available.
- Ultrasonic cleaner, lint-free wipes, isopropyl alcohol, nitrile gloves (keep skin oils off the RF surface).
- A modest vacuum setup only *later*, for the thrust test (not for making the cell).

*No cleanroom, no furnace, no acids. That's the whole point of staying at the copper tier.*

---

## Step-by-step fabrication

### Step 1 — Model it and pin the frequency
Draw the frustum in CAD to the nominal Ø160/Ø90/120 mm. **The resonant frequency is set by the geometry**, and the TM010 estimate (1.84 GHz) is approximate for a cone — so *design in tuning range*: the plunger must be able to pull the frequency ±2–3 % to hit your amplifier's exact band. If you have an EM solver (CST, HFSS, or the open-source **openEMS**), simulate the real frustum to get the true mode frequency and field map before cutting metal; if not, machine slightly **oversize in frequency** (a hair small in diameter) and tune down with the plunger.

### Step 2 — Rough-machine the body
Turn the outer profile and **bore the internal cone** in the copper billet. Leave **0.3–0.5 mm** of stock on all internal surfaces for the finishing pass. Machine the two end-cap flats and the cap register/counterbores. Drill and tap the plunger boss and the two port bosses (drive + pickup), positioned per your field map (drive port near a high-H-field region, pickup near a sampling point).

### Step 3 — Finish the internal surface (this sets your Q)
Because skin depth is ~1.5 µm, **the inner surface finish is not cosmetic — it is the Q**. Finishing pass with a sharp diamond or fine-carbide tool for a mirror turn; then hand-polish with progressively finer diamond compound (down to ~1 µm) or have the bore **electropolished** by a plating shop. Target roughness Ra < 0.4 µm. Handle only with gloves afterward.

### Step 4 — (Optional) plate the interior
Send the body for **bright-acid-copper or silver electroplating** of the internal surface. Silver has slightly lower surface resistance than copper at RF and buys a modest Q gain. Skip if you want to keep it simple; the bare-polished-OFHC number (Q ≈ 27k) already clears the test requirement by a wide margin.

### Step 5 — Fit the ports and plunger
Install the drive and pickup connectors with their copper coupling loops (start with small loops — you'll size them during tuning). Fit the threaded copper plunger + lead-screw + locknut so it slides smoothly along the axis and locks without wobble. Everything that touches the RF volume must be copper or silver; no steel, no ferrous anything (magnetic parts wreck the later null tests).

### Step 6 — Clean and assemble
Ultrasonic-clean all parts in IPA, dry, and assemble **wearing gloves**. Seat the RF gasket, bolt the end caps to even torque in a star pattern. The joint must be RF-tight — a leaky seam radiates and kills Q.

### Step 7 — Measure resonance and Q on the VNA (the gate)
Connect the VNA across the drive/pickup ports in transmission (S21). Find the TM010 peak; **adjust the plunger** until it lands on your target frequency (1.84 GHz, or your amp's band). Read **loaded Q** from the −3 dB bandwidth (Q = f₀/Δf); back out **unloaded Q₀** from the coupling. **Acceptance: Q₀ ≥ 20,000** (you designed for ~27k; anything below ~20k means surface finish, a leaky joint, or a bad contact — diagnose before proceeding). Tune the coupling loops toward **critical coupling** (S11 dip to the noise floor at resonance).

### Step 8 — Power test and thermal check
Drive it with the 10–15 W amplifier at resonance through the directional coupler + circulator (reflected power to the matched load). Confirm the cavity holds resonance under power (watch for thermal drift pulling the frequency — retune the plunger as it warms and settles). Verify the **10 W of wall heat** is handled (the copper body is a big heat sink at these powers; add a small cold-plate if it drifts). Log forward/reflected power — a rising reflected spike means detuning.

### Step 9 — Flight-qualify the single cell (before any array)
The cell is "qualified" when it: hits target frequency on the VNA, holds **Q₀ ≥ 20,000**, couples critically, stays on resonance under 10 W CW for a sustained run, and has **no ferromagnetic parts**. Only a cell that passes all five goes onto the torsion balance for the actual thrust measurement (per the Phase-1 build spec §3–§5).

---

## What comes after one good cell

1. **Measure it for thrust** — mount the qualified cell on the torsion balance from `antigravity-phase1-buildspec-2026-07-06.md`, run the AC-modulation + lock-in + null-test suite. This is where you find out if the ~12 µN signal is real or (far more likely) absent.
2. **Only if a signal survives the null suite** → escalate. That means the **niobium SRF + cryogenic tier** to chase higher Q — and *that* is where you hand off to an equipped accelerator/SRF lab, because the fabrication (HF electropolish, 800 °C hydrogen bake, cleanroom assembly, 4 K cryostat) is genuinely hazardous specialist work, not a bench build. This guide stops at copper on purpose.
3. **An array** is only worth building once a single cell has shown a real, replicated effect. Don't make 62 of anything until one has earned it.

---

## Safety (copper tier)

- **RF:** 10–15 W at 1.84 GHz — keep the cavity closed and interlocked; never look into or probe an energized open cavity; RF at these powers is a tissue-heating hazard.
- **Machining:** standard lathe/mill PPE; copper swarf is sharp.
- **Electroplating (if used):** done by a plating shop — their hazard, their controls.
- **What's deliberately absent:** no hydrofluoric acid, no high-temperature furnace, no cryogens, no high-pressure water rinse. If you ever move to niobium, **stop and partner with a lab that runs SRF** — HF exposure can be fatal and is not a self-taught process.

---

*Appendix — reproduce the numbers:* `python research_outputs/copper_cavity_fab_calc.py` (TM010 frequency, skin depth, surface resistance, expected copper Q₀, wall heat; asserts the cavity resonates in the low-GHz band at a realistic room-temp Q). Test apparatus: `antigravity-phase1-buildspec-2026-07-06.md`. Why Q is the whole lever + why 4 K is needed for the real thing: `antigravity-cavity-chamber-deep-dive-2026-07-06.md`.*
