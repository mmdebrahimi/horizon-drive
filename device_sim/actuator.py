"""Per-cell thrust-slew actuator model.

Real cells cannot change thrust instantly: the piezo tuner + thermal settling cap
the amplitude slew rate at ~10-100 Hz. We model each cell's *actual* amplitude as
a first-order lag toward the commanded amplitude, with a bandwidth f_bw (Hz):

    da/dt = (a_cmd - a) / tau,   tau = 1 / (2*pi*f_bw)

Discrete update (exact for a first-order hold over dt):
    a <- a + (a_cmd - a) * (1 - exp(-dt / tau))
"""
from __future__ import annotations
import numpy as np


class SlewActuator:
    """First-order amplitude lag, per cell."""

    def __init__(self, n: int, bandwidth_hz: float):
        if bandwidth_hz <= 0:
            raise ValueError("bandwidth must be > 0 Hz")
        self.tau = 1.0 / (2.0 * np.pi * bandwidth_hz)
        self.amp = np.zeros(n)

    def update(self, amp_cmd: np.ndarray, dt: float) -> np.ndarray:
        alpha = 1.0 - np.exp(-dt / self.tau)
        self.amp = self.amp + (np.asarray(amp_cmd, float) - self.amp) * alpha
        return self.amp
