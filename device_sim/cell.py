"""Single thrust cell: the F = eta*P*Q/c law + a quench hook."""
from __future__ import annotations
from dataclasses import dataclass, field
import numpy as np
from device_sim.constants import C


def cell_thrust(power_W: float, Q: float, eta: float) -> float:
    """Thrust magnitude of one cell at full amplitude: F = eta * P * Q / c (newtons)."""
    return eta * power_W * Q / C


@dataclass
class Cell:
    """One thruster cell.

    position: 3-vector of the cell on the craft body (m, body frame).
    axis:     unit thrust direction in the body frame (nominally +z 'up').
    healthy:  a quenched/failed cell produces zero thrust.
    """
    position: np.ndarray
    axis: np.ndarray
    max_thrust_N: float
    healthy: bool = True

    def __post_init__(self):
        self.position = np.asarray(self.position, dtype=float)
        self.axis = np.asarray(self.axis, dtype=float)
        n = np.linalg.norm(self.axis)
        if n == 0:
            raise ValueError("cell axis must be non-zero")
        self.axis = self.axis / n

    def thrust_vector(self, amplitude: float) -> np.ndarray:
        """Body-frame thrust 3-vector for a commanded amplitude in [0, 1]."""
        if not self.healthy:
            return np.zeros(3)
        a = float(np.clip(amplitude, 0.0, 1.0))
        return a * self.max_thrust_N * self.axis
