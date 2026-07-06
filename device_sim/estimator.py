"""State estimator: a linear Kalman filter for position/velocity + a
complementary filter for attitude/rate.

The controller consumes .pos/.vel/.quat/.omega, so the estimate is exposed as a
lightweight object with those attributes (drop-in for the true RigidBody).
"""
from __future__ import annotations
from dataclasses import dataclass, field
import numpy as np
from device_sim.dynamics import quat_mul


@dataclass
class Estimate:
    pos: np.ndarray
    vel: np.ndarray
    quat: np.ndarray
    omega: np.ndarray


class StateEstimator:
    """KF on [pos(3), vel(3)] with an acceleration control input;
    complementary blend on attitude + low-pass on gyro."""

    def __init__(self, pos0=None, pos_sigma=0.03, att_gain=0.05, gyro_lp=0.3):
        self.x = np.zeros(6)
        if pos0 is not None:
            self.x[0:3] = np.asarray(pos0, float)
        # covariance
        self.P = np.eye(6) * 1.0
        # process noise (accel jitter) and measurement noise (position)
        self.q_acc = 0.5
        self.r_pos = pos_sigma ** 2
        # attitude/rate filter state
        self.quat = np.array([1.0, 0, 0, 0])
        self.omega = np.zeros(3)
        self.att_gain = att_gain           # blend toward measured attitude
        self.gyro_lp = gyro_lp             # low-pass factor on gyro

    def predict(self, accel_ctrl: np.ndarray, dt: float):
        F = np.eye(6)
        F[0:3, 3:6] = dt * np.eye(3)
        B = np.zeros((6, 3))
        B[0:3, :] = 0.5 * dt * dt * np.eye(3)
        B[3:6, :] = dt * np.eye(3)
        self.x = F @ self.x + B @ np.asarray(accel_ctrl, float)
        Q = np.zeros((6, 6))
        Q[3:6, 3:6] = self.q_acc * dt * np.eye(3)
        Q[0:3, 0:3] = self.q_acc * (dt ** 3) / 3.0 * np.eye(3)
        self.P = F @ self.P @ F.T + Q
        # attitude predict: integrate the current (filtered) gyro
        wq = np.concatenate([[0.0], self.omega])
        self.quat = self.quat + 0.5 * quat_mul(self.quat, wq) * dt
        self.quat = self.quat / np.linalg.norm(self.quat)

    def update(self, meas: dict):
        # --- position Kalman update ---
        H = np.zeros((3, 6)); H[:, 0:3] = np.eye(3)
        R = self.r_pos * np.eye(3)
        y = np.asarray(meas["pos"], float) - H @ self.x
        S = H @ self.P @ H.T + R
        K = self.P @ H.T @ np.linalg.inv(S)
        self.x = self.x + K @ y
        self.P = (np.eye(6) - K @ H) @ self.P
        # --- attitude complementary blend + gyro low-pass ---
        qm = np.asarray(meas["quat"], float)
        if np.dot(self.quat, qm) < 0:
            qm = -qm
        self.quat = (1 - self.att_gain) * self.quat + self.att_gain * qm
        self.quat = self.quat / np.linalg.norm(self.quat)
        self.omega = (1 - self.gyro_lp) * self.omega + self.gyro_lp * np.asarray(meas["omega"], float)

    def estimate(self) -> Estimate:
        return Estimate(pos=self.x[0:3].copy(), vel=self.x[3:6].copy(),
                        quat=self.quat.copy(), omega=self.omega.copy())
