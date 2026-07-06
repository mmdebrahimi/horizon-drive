"""Closed-loop scenario tests: the MVP verification signals.

Fast settings (dt=0.02) keep the suite quick while still exercising the full
controller -> allocation -> array -> dynamics loop.
"""
import numpy as np
from device_sim import default_params
from device_sim.array import ThrusterArray
from device_sim.allocation import allocate
from device_sim.cell import cell_thrust
from device_sim.sim import run


# --- unit-ish checks on the building blocks ---

def test_uniform_thrust_is_near_vertical():
    """Centered geometry + alternating yaw cant => uniform amplitude gives ~pure Fz.

    A residual horizontal force exists (odd cell count => the alternating tangential
    cants don't cancel bitwise) but is negligible relative to the vertical thrust,
    and the closed-loop controller nulls it (see test_hover_holds).
    """
    arr = ThrusterArray(default_params())
    w = arr.wrench(np.full(arr.n, 0.5))
    horiz = np.hypot(w[0], w[1])
    authority = arr.n * arr.per_cell_max() * arr.params.array_radius_m
    assert horiz < 0.005 * w[2]                          # < 0.5% of vertical thrust
    assert np.linalg.norm(w[3:6]) < 0.001 * authority    # < 0.1% of total torque authority
    assert w[2] > 0                                      # up


def test_allocation_delivers_hover_wrench():
    arr = ThrusterArray(default_params())
    W = default_params().craft_mass_kg * 9.80665
    demand = np.array([0, 0, W, 0, 0, 0.0])
    delivered = arr.wrench(allocate(arr, demand))
    assert abs(delivered[2] - W) < 0.02 * W              # vertical within 2%
    assert np.linalg.norm(delivered[3:6]) < 1.0          # negligible torque


def test_quench_reallocates_vertical_thrust():
    arr = ThrusterArray(default_params())
    W = default_params().craft_mass_kg * 9.80665
    demand = np.array([0, 0, W, 0, 0, 0.0])
    for i in range(5):
        arr.cells[i].healthy = False                     # kill 5 cells
    delivered = arr.wrench(allocate(arr, demand))
    assert abs(delivered[2] - W) < 0.05 * W              # neighbours still meet demand


# --- full closed-loop scenarios (the MVP bar) ---

def test_hover_holds():
    r = run(target_pos=np.array([0, 0, 0.]), start_pos=np.array([0, 0, -2.]),
            duration=60, dt=0.02)
    assert not r.diverged
    assert r.max_pos_err < 0.1        # < 10 cm hold
    assert r.max_tilt_deg < 2.0


def test_single_cell_quench_stays_bounded():
    r = run(target_pos=np.array([0, 0, 0.]), start_pos=np.array([0, 0, -2.]),
            duration=60, dt=0.02, quench_at=20.0, quench_cells=1)
    assert not r.diverged
    assert r.max_pos_err < 0.1


def test_five_cell_quench_stays_bounded():
    r = run(target_pos=np.array([0, 0, 0.]), start_pos=np.array([0, 0, -2.]),
            duration=60, dt=0.02, quench_at=20.0, quench_cells=5)
    assert not r.diverged
    assert r.max_pos_err < 0.15       # slightly looser: 5 dead cells


def test_step_translation():
    r = run(target_pos=np.array([3, 0, 0.]), start_pos=np.array([0, 0, 0.]),
            duration=60, dt=0.02)
    assert not r.diverged
    assert r.max_pos_err < 0.1
    assert r.max_tilt_deg < 10.0
