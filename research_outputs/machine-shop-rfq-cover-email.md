# Machine-shop RFQ — cover email (copper resonant cavity HD-CU-CAV-001)

Paste-ready request for a CNC/precision machine shop. Fill the bracketed
`[...]` fields, attach the **3 STEP files + the machinist spec sheet**, and send.
Keep the STEP and the spec together — the STEP is geometry only; the spec sheet
governs manufacture (tolerances, surface finish, threads, material).

---

**Subject:** RFQ — prototype set of 3 machined OFHC copper parts (mirror-bore RF cavity)

Hello,

I'd like a quote to machine a **single prototype set of three copper parts** — a cavity body, an end cap, and a small threaded tuner plunger. They form a microwave resonant cavity for a personal physics/engineering research project.

**Quantity:** 1 of each part (one complete set).

**Material:** OFHC copper, **C10100** (C10200 acceptable). I can supply stock or you can — please advise which you prefer and how it affects the price.

**Attached:**
- `HD-CU-CAV-001-01_body.step`, `HD-CU-CAV-001-02_endcap.step`, `HD-CU-CAV-001-03_plunger.step` — STEP geometry for quoting.
- `HD-CU-CAV-001` machinist specification sheet (PDF/MD) — the controlling document for tolerances, surface finish, threads, and material. **Please quote to the spec sheet, not the STEP alone** (STEP files carry no thread or finish callouts).

**The three requirements that drive this job** (please tell me whether you can meet them):

1. **Mirror-polished internal bore.** The internal tapered bore (Ø160 → Ø90 over 120 mm) and the cap's inner face must reach **Ra ≤ 0.4 µm** (mirror finish). This is the single pass/fail requirement — RF performance depends on it. What process would you use to achieve it on a tapered blind-ish bore (diamond turning / lapping / electropolishing)?
2. **Threads as specified** — an **M20 × 1.0 fine** axial thread in the base, and **8× M5 tapped** holes in the mouth flange (blind, ≥ 8 mm deep). The end cap has matching Ø5.5 clearance holes with counterbores.
3. **Non-magnetic throughout** — copper parts only; no steel inserts. (I supply the non-magnetic fasteners separately.)

**What I'd like in the quote:**
- Confirmation you can hold **Ra ≤ 0.4 µm** on the internal bore, and by what process.
- **Budgetary price** for the one prototype set.
- **Lead time.**
- Whether you supply the OFHC copper stock or I should.
- Any dimensions or tolerances on the drawing you'd flag as difficult or would like to relax.

This is a one-off prototype, so I'm flexible on non-critical cosmetic surfaces (the spec marks those). Happy to hop on a call to walk through the part.

Thank you,

[Your name]
[Email] · [Phone]

---

*Tips for choosing a shop:* prioritize a shop that says **"yes, and here's how"** to the Ra ≤ 0.4 µm bore — that finish, not the outside geometry, is the whole job. Shops that do RF/waveguide, optical, or vacuum work are the right fit; a general job shop may sub the polish out. Online quoters (Xometry, Protolabs, PCBWay, SendCutSend) will price the geometry from the STEP instantly but confirm the **mirror-bore finish** is achievable before committing — it's often outside a standard CNC finish and may need a specialist polish/electropolish pass.
