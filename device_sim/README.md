# device_sim — Horizon-Drive Craft Digital Twin

A runnable simulation of the quantised-inertia / horizon-drive thruster craft from
the anti-gravity research thread. **Suspend-disbelief engineering:** the propulsion
physics is *assumed proven* (`F = η·P·Q/c`, η=0.0072, Q=10¹⁰ → 240 N per 1 kW cell);
this package models the vehicle you'd build around it and validates that the
control approach works — before any hardware exists.

It is WP6-SW of the hardware WBS (`plans/Anti_Gravity_Device_Hardware_WBS.md`) — the
only zero-hardware-dependency work package, and the cheapest way to de-risk the
ground-test phase.

## What it models
- **`constants.py`** — frozen design params (provenance: the build-instructions memo).
- **`cell.py`** — one thrust cell (`F = η·P·Q/c`) with a quench (failure) hook.
- **`array.py`** — 62-cell centered hex-disc array with alternating yaw cant; maps
  per-cell amplitudes → a 6-DOF wrench about the CG.
- **`budget.py`** — reproduces the verified power/mass budget.
- **`allocation.py`** — bounded least-squares (scipy `lsq_linear`, 0≤a≤1) mapping a
  wrench demand → per-cell amplitudes; drops quenched cells so neighbours compensate.
- **`dynamics.py`** — 6-DOF Newton-Euler rigid body (quaternion attitude).
- **`controller.py`** — cascaded position→attitude controller. **Attitude gains scale
  with the moment of inertia** (physical bandwidth × I) so the inner loop stays fast
  relative to position on a heavy vehicle — the key to stability.
- **`sim.py`** — closed loop + scenarios (hover, translate, quench injection).

## Verified results
| Quantity (reproduced by `budget.py`) | Value |
|---|---|
| Thrust per 1 kW cell (Q=10¹⁰) | 240 N |
| Cells for TWR 1.5 (1 t) | 62 |
| Total electrical power | ~126 kW |
| Cryocooler mass | ~490 kg |
| Core dry mass | ~1,108 kg |

Closed-loop (60 s, dt=0.02): **hover, ±5-cell quench, and step/diagonal translation
all hold position to < 1–2 cm** with < 2° tilt — including instant reallocation
after a cell failure.

## Run
```bash
python -m pytest -q device_sim          # unit + scenario tests
python -c "import numpy as np; from device_sim.sim import run; \
r=run(target_pos=np.array([3,0,0.]), quench_at=20, quench_cells=5, dt=0.02); \
print('diverged', r.diverged, 'pos_err', round(r.max_pos_err,4), 'm')"
```

## Scope / honesty
A **decision-support digital twin**, not certified flight software. Simplifications:
thrust-slew (the real 10–100 Hz tuner/thermal limit) is idealized; cavity thermal
dynamics and sensor noise are not modelled. The point is to show the *control
architecture* (fly-by-wire differential-thrust vectoring with fault reallocation) is
sound — which it is. Whether the underlying effect is real at all is the subject of
the companion research memos, not this package.
