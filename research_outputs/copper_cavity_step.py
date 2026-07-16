"""Parametric CAD model -> STEP export for the copper resonant cavity HD-CU-CAV-001.

Builds the three machined parts (BODY, END CAP, TUNER PLUNGER) straight from the
dimensions frozen in `copper-cavity-machinist-spec-2026-07-15.md`, exports one
STEP file per part for online CNC quoting, and self-verifies the solids
(bounding box + positive volume) so a bad build fails loudly.

Threads are NOT modelled (STEP carries no thread callout) -- tapped/threaded
features are modelled at their tap-drill / nominal diameter and the thread spec
lives in the drawing + machinist spec. This model is for QUOTING geometry, the
spec sheet governs manufacture.

Run with the cadquery venv on D::
    /d/cad-venv/Scripts/python.exe research_outputs/copper_cavity_step.py
"""
from __future__ import annotations
import os
import cadquery as cq

OUT = os.path.dirname(os.path.abspath(__file__))

# ---- frozen dimensions (mm) from HD-CU-CAV-001 ------------------------------
BODY_OD      = 174.0     # body external OD below flange
FLANGE_OD    = 200.0
FLANGE_THK   = 14.0
BORE_MOUTH_D = 160.0     # internal bore, mouth (large) diameter
BORE_BASE_D  = 90.0      # internal bore, base (small) diameter
BORE_LEN     = 120.0     # internal axial length, mouth face -> inner base
BASE_WALL    = 7.0       # base wall thickness below inner base (6-8 -> nominal 7)
TUNER_TAPD   = 19.0      # M20x1.0 tap-drill (nominal), through the base on axis
BOLT_PCD     = 185.0     # flange/cap bolt circle
BOLT_R       = BOLT_PCD / 2.0
N_BOLTS      = 8
M5_TAPD      = 4.2       # M5 tap drill for the TAPPED body flange holes
M5_TAPDEPTH  = 8.0
CAP_THK      = 14.0
CAP_CLEAR_D  = 5.5       # cap clearance holes
CAP_CBORE_D  = 10.0
CAP_CBORE_DP = 5.0
PORT_R       = 70.0      # drive/pickup port radius on the cap
DRIVE_PORT_D = 16.0      # N-type
PICKUP_PORT_D= 6.5       # SMA
BODY_H       = BORE_LEN + BASE_WALL          # 127 total body height
FLANGE_Z0    = BODY_H - FLANGE_THK           # flange starts here

# ---- Part 1: CAVITY BODY (HD-CU-CAV-001-01) ---------------------------------
body = cq.Workplane("XY").circle(BODY_OD / 2).extrude(BODY_H)
flange = cq.Workplane("XY").workplane(offset=FLANGE_Z0).circle(FLANGE_OD / 2).extrude(FLANGE_THK)
body = body.union(flange)

# internal linear-taper cavity: r=45 @ z=BASE_WALL up to r=80 @ z=BODY_H
inner = (cq.Workplane("XY").workplane(offset=BASE_WALL)
         .circle(BORE_BASE_D / 2)
         .workplane(offset=BORE_LEN)
         .circle(BORE_MOUTH_D / 2)
         .loft(combine=False))
body = body.cut(inner)

# axial tuner bore through the base (opens into the cavity)
body = body.cut(cq.Workplane("XY").circle(TUNER_TAPD / 2).extrude(BODY_H))

# 8x M5 TAPPED (blind, tap-drill dia) in the flange, from the mouth face down
body = (body.faces(">Z").workplane()
        .polarArray(BOLT_R, 0, 360, N_BOLTS)
        .hole(M5_TAPD, depth=M5_TAPDEPTH))

# ---- Part 2: END CAP (HD-CU-CAV-001-02) -------------------------------------
cap = cq.Workplane("XY").circle(FLANGE_OD / 2).extrude(CAP_THK)
cap = (cap.faces(">Z").workplane()
       .polarArray(BOLT_R, 0, 360, N_BOLTS)
       .cboreHole(CAP_CLEAR_D, CAP_CBORE_D, CAP_CBORE_DP))
cap = cap.faces(">Z").workplane().pushPoints([(PORT_R, 0)]).hole(DRIVE_PORT_D)
cap = cap.faces(">Z").workplane().pushPoints([(-PORT_R, 0)]).hole(PICKUP_PORT_D)

# ---- Part 3: TUNER PLUNGER (HD-CU-CAV-001-03) -------------------------------
plunger = (cq.Workplane("XY").circle(24 / 2).extrude(8)          # adjustment head
           .faces(">Z").workplane().circle(20 / 2).extrude(30)    # M20x1.0 shank (nominal)
           .faces(">Z").workplane().circle(19.9 / 2).extrude(12)) # plain guide + inner face

# ---- export + verify --------------------------------------------------------
PARTS = [
    ("HD-CU-CAV-001-01_body.step",    body,    (FLANGE_OD, FLANGE_OD, BODY_H)),
    ("HD-CU-CAV-001-02_endcap.step",  cap,     (FLANGE_OD, FLANGE_OD, CAP_THK)),
    ("HD-CU-CAV-001-03_plunger.step", plunger, (24.0, 24.0, 50.0)),
]

print("=" * 62)
print("HD-CU-CAV-001  copper cavity  ->  STEP export + solid check")
print("=" * 62)
all_ok = True
for fname, part, (ex, ey, ez) in PARTS:
    path = os.path.join(OUT, fname)
    cq.exporters.export(part, path)
    solid = part.val()
    bb = solid.BoundingBox()
    vol = solid.Volume()
    dx, dy, dz = bb.xlen, bb.ylen, bb.zlen
    ok = (abs(dx - ex) < 0.6 and abs(dy - ey) < 0.6 and abs(dz - ez) < 0.6 and vol > 0)
    all_ok &= ok
    print(f"[{'PASS' if ok else 'FAIL'}] {fname}")
    print(f"       bbox = {dx:.1f} x {dy:.1f} x {dz:.1f} mm (expect {ex:.0f} x {ey:.0f} x {ez:.0f})")
    print(f"       volume = {vol/1000:.1f} cm^3, exported -> {fname}")

print("=" * 62)
print("ALL PARTS OK" if all_ok else "BUILD FAILED")
raise SystemExit(0 if all_ok else 1)
