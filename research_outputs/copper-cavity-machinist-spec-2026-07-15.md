# MACHINIST SPECIFICATION — Copper Resonant Cavity (Horizon-Drive Thrust-Cell, Test Article)

**Drawing no.** HD-CU-CAV-001 · **Rev.** A · **Date** 2026-07-15
**Part name:** Copper RF resonant cavity — truncated-cone (frustum) test article, room-temperature
**Quantity:** 1 (prototype) · **Companion docs:** `antigravity-copper-cell-fabrication-2026-07-06.md` (process narrative), `copper_cavity_machinist_check.py` (dimension verification)

> **What this part is (one line for the shop):** a hollow, mirror-polished copper cone that must ring as a microwave resonator near **1.84 GHz**. It is made as **three machined parts** — a cavity **BODY**, an **END CAP**, and a **TUNER PLUNGER** — plus purchased non-magnetic hardware.

---

## GENERAL NOTES — read before cutting metal

1. **Material (all machined parts): OFHC copper, C10100** (oxygen-free, "OFE"). C10200 acceptable. **Do NOT** substitute ETP/C11000 if avoidable, and **no brass/bronze** for the cavity walls.
2. **The internal surface finish is the single most important requirement.** The RF current flows in the top ~1.5 µm of the inner surface, so **all internal (bore + cap inner face) surfaces must be mirror-polished to Ra ≤ 0.4 µm.** Roughness here directly destroys performance. Tool marks, scratches, or matte finish inside = reject.
3. **Frequency is trimmed later — do NOT chase it.** Machine to the dimensions and tolerances given; the exact resonant frequency is set afterward by the tuner and measured on a network analyzer. The ±0.1 mm bore tolerance only shifts frequency ~1.5 MHz, which the tuner absorbs ~20× over (verified in `copper_cavity_machinist_check.py`).
4. **EVERYTHING must be non-magnetic.** Copper parts, and **all fasteners silver-plated brass or brass — NO magnetic stainless, NO steel.** A hand magnet must not attract any part or screw. (This matters for downstream physics tests.)
5. **Cleanliness:** after final polish, degrease the bore (isopropyl alcohol), keep it particulate-free, and **handle internal surfaces with nitrile gloves only** — skin oils degrade RF surfaces.
6. **Dimensions in millimetres.** Unspecified tolerance: ±0.2 mm. Unspecified surface finish: Ra 1.6 µm. Break sharp external edges 0.3 mm; **do NOT chamfer internal cavity edges** unless noted.

---

## CROSS-SECTION (schematic, not to scale)

```
                 END CAP (Part 2)  Ø200 x 14
      drive port ●        ● pickup port   (r = 70 mm, 180° apart)
      ┌───────────────────────────────────┐
      │        inner face: MIRROR         │  ← mates to BODY mouth flange
      └───┬───────────────────────────┬───┘   (8x M5 on 185 PCD, soft-Cu gasket)
          │                           │
   mouth  │   Ø160.0 ±0.1  (open)     │   ← BODY (Part 1) flange face, flat & mirror
   plane ═╪═══════════════════════════╪═══
          │ \                       / │
          │   \   tapered bore     /   │        linear taper, half-angle 16.3°
          │     \   MIRROR       /     │        from the cavity axis
          │       \            /       │
          │         \        /         │  120.0 ±0.2  internal axial length
   base   │           Ø90.0 ±0.1       │
   plane ═╪═════════════╤═════════════╪═
          │   6-8 mm    │  solid base  │
          └─────────────┼──────────────┘
                   TUNER PLUNGER (Part 3)  M20x1.0, on axis, travel ±5 mm
```

---

## PART 1 — CAVITY BODY (HD-CU-CAV-001-01)

A copper "cup": closed at the small end, open at the large (mouth) end, with an integral mounting flange at the mouth.

**Stock:** OFHC copper round bar, Ø210 × 145 mm (allows cleanup + the flange).

| Feature | Dimension | Tol. | Finish / note |
|---|---|---|---|
| **Internal bore — mouth (large) diameter** | Ø **160.0** | ±0.1 | **mirror, Ra ≤ 0.4 µm** — the RF surface |
| **Internal bore — base (small) diameter** | Ø **90.0** | ±0.1 | **mirror, Ra ≤ 0.4 µm** |
| **Internal axial length** (mouth face → inner base) | **120.0** | ±0.2 | measured on axis |
| Bore profile | **linear taper**, Ø160→Ø90 over 120 axial | — | half-angle **16.3°** from axis; single straight taper, no steps |
| Base wall thickness (below inner base) | 6–8 | ref | structural + tuner boss |
| Body external OD (below flange) | Ø174 | ±0.5 | electrically irrelevant; cosmetic Ra 1.6 |
| **Mouth flange** OD | Ø **200** | ±0.5 | integral with body |
| Mouth flange thickness | 14 | ±0.2 | — |
| **Mouth flange sealing face** (mates cap) | flat | flatness ≤ **0.02** | Ra ≤ 0.8 µm; perpendicular to axis |
| Flange bolt holes | **8× M5 clearance (Ø5.5)**, on **185 PCD**, equally spaced (45°) | ±0.1 PCD | c'bore Ø10 × 5 for socket head |
| **Tuner boss** (in the base, on axis) | tapped **M20 × 1.0**, through the base into the cavity | concentric ±0.1 | fine thread; deburr the inner opening, no chamfer inside |

**Notes for Part 1:**
- The tapered bore is the resonator — cut it as one clean straight taper (taper attachment or CNC). No chatter, no steps.
- Leave the **final 0.15–0.20 mm of the bore for the polishing pass** — rough-bore, then diamond/fine-polish (or send the bore for electropolish) to Ra ≤ 0.4 µm.
- The mouth flange face and the cap inner face together close the cavity; both must be flat and clean for a good RF seal.

---

## PART 2 — END CAP (HD-CU-CAV-001-02)

A copper disc that closes the mouth and carries the two RF ports.

**Stock:** OFHC copper plate/round, Ø210 × 20 mm.

| Feature | Dimension | Tol. | Finish / note |
|---|---|---|---|
| Cap OD | Ø **200** | ±0.5 | match body flange |
| Cap thickness | **14** | ±0.2 | — |
| **Inner face** (faces into cavity) | flat | flatness ≤ **0.02** | **mirror, Ra ≤ 0.4 µm** — it IS the cavity end wall |
| Bolt holes | **8× M5 clearance (Ø5.5)** on **185 PCD**, 45° spaced | ±0.1 PCD | must align with Part 1 |
| **Drive port** | through-hole at **r = 70 mm, 0°** | ±0.2 | size to chosen connector (N-type: Ø16 + 4× M3 flange holes) |
| **Pickup port** | through-hole at **r = 70 mm, 180°** | ±0.2 | size to chosen connector (SMA: Ø6.5) |

**Notes for Part 2:** the two port holes let coupling loops enter the cavity; their exact size/position is nominal (coupling is optimized during RF commissioning). Keep the inner face pristine — no burrs around the port holes.

---

## PART 3 — TUNER PLUNGER (HD-CU-CAV-001-03)

A threaded copper rod that screws into the base boss to trim the resonant frequency.

**Stock:** OFHC copper rod, Ø25 × 70 mm.

| Feature | Dimension | Tol. | Finish / note |
|---|---|---|---|
| Threaded shank | **M20 × 1.0**, length 30 | class 6g | mates Part 1 tuner boss |
| Plain guide diameter | Ø19.9 | ±0.05 | ahead of thread, ~10 long |
| **Inner end face** (protrudes into cavity) | flat, ⟂ axis | — | **mirror, Ra ≤ 0.4 µm** |
| Adjustment head | Ø24 × 8, hex or knurled | — | for hand/tool adjustment |
| Overall length | ~55 | ref | so face travels **±5 mm** about flush-with-base |

Supplied with **1× M20 × 1.0 brass lock-nut** (non-magnetic).

---

## BILL OF MATERIALS

**Machined (this drawing set):**
| Item | Part | Material | Qty |
|---|---|---|---|
| 1 | Cavity body HD-CU-CAV-001-01 | OFHC Cu C10100 | 1 |
| 2 | End cap HD-CU-CAV-001-02 | OFHC Cu C10100 | 1 |
| 3 | Tuner plunger HD-CU-CAV-001-03 | OFHC Cu C10100 | 1 |

**Purchased / assembly hardware (NON-MAGNETIC — buyer supplies):**
| Item | Description | Qty |
|---|---|---|
| 4 | M5 × 20 socket-head cap screw, **silver-plated brass or brass** (non-magnetic) + washer | 8 |
| 5 | **Soft annealed copper gasket ring** for the mouth seal (ID ~162 / OD ~176 × ~1.5 thk), OR a canted-coil RF spring gasket | 1 |
| 6 | M20 × 1.0 brass lock-nut | 1 |
| 7 | N-type bulkhead panel connector + small copper coupling loop (drive) | 1 |
| 8 | SMA bulkhead panel connector + small copper coupling loop (pickup) | 1 |

*(Items 7–8 and the coupling loops are fitted and tuned during RF commissioning, not by the machine shop.)*

---

## INSPECTION / ACCEPTANCE

**Machine-shop acceptance (dimensional + finish):**
- [ ] Bore mouth Ø160.0 ±0.1, base Ø90.0 ±0.1, internal length 120.0 ±0.2 — verified (bore gauge / CMM).
- [ ] **Bore + cap inner face Ra ≤ 0.4 µm (mirror)** — verified (roughness gauge or witness sample). *This is the pass/fail item.*
- [ ] Flange & cap-inner flatness ≤ 0.02 mm; faces perpendicular to axis.
- [ ] 8× M5 holes align between body and cap (trial fit).
- [ ] Tuner plunger runs smoothly in the base boss, ±5 mm travel, locks without wobble.
- [ ] **Non-magnetic check:** a hand magnet attracts NO part or fastener.
- [ ] Bore clean, oil-free, particulate-free; delivered with internal surfaces protected.

**RF acceptance (performed by the experimentalist after assembly — listed here for context, NOT a machine-shop task):**
- [ ] Assembled cavity on a vector network analyzer; TM010 resonance located near **1.8 GHz**.
- [ ] **Unloaded Q₀ ≥ 20,000** (design target ~27,000). *Below ~20,000 → investigate surface finish / joint seal / cleanliness before use.*

---

*Honesty note for the record: this is the **room-temperature copper test article** — the object used to measure whether the effect exists, not a flight component. Its expected Q (~27,000) is far below the Q≈10¹⁰ the propulsion claim needs (that requires niobium at 4 K, a separate specialist build). Machining this part correctly is a real, buildable step; interpreting what it measures is the experiment. Dimensions verified in `copper_cavity_machinist_check.py` (exit 0). Physics grounding: `antigravity-cavity-chamber-deep-dive-2026-07-06.md`.*
