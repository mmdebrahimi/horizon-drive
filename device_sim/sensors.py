"""Noisy sensor model: position, attitude, and gyro measurements with Gaussian noise.

Emulates a real avionics suite: a position source (GPS/laser/optical, ~cm noise),
an attitude reference (~0.5 deg noise), and a rate gyro (~0.01 rad/s noise).
"""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from device_sim.dynamics import quat_mul


@dataclass
class SensorNoise:
    pos_sigma: float = 0.03          # m   (position source)
    att_sigma: float = 0.0087        # rad (~0.5 deg attitude)
    gyro_sigma: float = 0.01         # rad/s (rate gyro)


class Sensors:
    def __init__(self, noise: SensorNoise | None = None, seed: int = 0):
        self.noise = noise or SensorNoise()
        self.rng = np.random.default_rng(seed)

    def measure(self, body) -> dict:
        n = self.noise
        pos_m = body.pos + self.rng.normal(0, n.pos_sigma, 3)
        omega_m = body.omega + self.rng.normal(0, n.gyro_sigma, 3)
        # attitude: perturb true quaternion by a small random rotation
        dtheta = self.rng.normal(0, n.att_sigma, 3)
        dq = np.concatenate([[1.0], 0.5 * dtheta])
        dq = dq / np.linalg.norm(dq)
        quat_m = quat_mul(body.quat, dq)
        quat_m = quat_m / np.linalg.norm(quat_m)
        return {"pos": pos_m, "quat": quat_m, "omega": omega_m}
