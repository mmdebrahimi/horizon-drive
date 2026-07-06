"""Thruster array: builds N cells + maps amplitudes -> a 6-DOF wrench."""
from __future__ import annotations
import numpy as np
from device_sim.constants import DesignParams
from device_sim.cell import Cell, cell_thrust


def _hex_disc_positions(n: int, radius: float) -> np.ndarray:
    """n points spread on a disc via a sunflower (phyllotaxis) pattern — even, deterministic."""
    idx = np.arange(n, dtype=float)
    golden = np.pi * (3.0 - np.sqrt(5.0))          # golden angle
    r = radius * np.sqrt((idx + 0.5) / n)
    theta = idx * golden
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    pts = np.column_stack([x, y, np.zeros(n)])
    pts[:, 0:2] -= pts[:, 0:2].mean(axis=0)        # center the centroid on the CG
    return pts


class ThrusterArray:
    """A disc of upward-thrusting cells; steered by per-cell amplitude."""

    def __init__(self, params: DesignParams, n_cells: int | None = None):
        self.params = params
        self.n = int(n_cells if n_cells is not None else params.cells_needed())
        fmax = cell_thrust(params.cell_power_W, params.Q, params.eta)
        pos = _hex_disc_positions(self.n, params.array_radius_m)
        cant = params.yaw_cant_rad
        self.cells: list[Cell] = []
        for i in range(self.n):
            p = pos[i]
            # nominal axis +z; add a small tangential cant so differential amplitude yaws.
            rho = np.hypot(p[0], p[1])
            if rho > 1e-9:
                tang = np.array([-p[1], p[0], 0.0]) / rho      # unit tangential
            else:
                tang = np.zeros(3)
            # ALTERNATE the cant sign so uniform thrust makes ZERO net yaw torque,
            # while differential amplitude still yields a yaw couple (controllable).
            sign = 1.0 if (i % 2 == 0) else -1.0
            axis = np.array([0.0, 0.0, 1.0]) + sign * cant * tang
            self.cells.append(Cell(position=p, axis=axis, max_thrust_N=fmax))

    # --- geometry / capability ---
    def per_cell_max(self) -> float:
        return self.cells[0].max_thrust_N

    def max_vertical_thrust(self) -> float:
        return sum(c.max_thrust_N * c.axis[2] for c in self.cells if c.healthy)

    def effectiveness(self) -> np.ndarray:
        """6xN matrix B mapping amplitudes -> wrench [Fx,Fy,Fz, Tx,Ty,Tz] about the CG (origin)."""
        B = np.zeros((6, self.n))
        for i, c in enumerate(self.cells):
            f = c.max_thrust_N * c.axis if c.healthy else np.zeros(3)
            tau = np.cross(c.position, f)
            B[0:3, i] = f
            B[3:6, i] = tau
        return B

    def wrench(self, amplitudes: np.ndarray) -> np.ndarray:
        """Net [force(3), torque(3)] for the commanded per-cell amplitudes."""
        a = np.clip(np.asarray(amplitudes, dtype=float), 0.0, 1.0)
        return self.effectiveness() @ a
