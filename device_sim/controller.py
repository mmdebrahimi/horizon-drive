"""Cascaded flight controller: position/attitude -> a 6-DOF body wrench demand.

Outer loop (world): PD on position/velocity -> desired horizontal acceleration +
vertical force. Desired horizontal accel is converted to a small target tilt.
Inner loop (body): PD on attitude error + body rates -> torque demand.
"""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from device_sim.dynamics import RigidBody, quat_to_rot
from device_sim.constants import G0


@dataclass
class ControllerGains:
    kp_pos: float = 0.50           # wn~0.7 rad/s, ~10x below the attitude loop
    kd_pos: float = 1.4            # ~critically damped (zeta~1.0)
    # attitude loop is specified as a physical bandwidth; the actual torque gains
    # are scaled by the craft's moment of inertia so the inner loop is FAST
    # relative to position regardless of vehicle size (cascade separation).
    att_bandwidth: float = 6.0     # rad/s natural frequency of the attitude loop
    att_damping: float = 1.0       # critically damped
    max_tilt: float = 0.15         # rad, clamp on commanded tilt (gentle translation)


class FlightController:
    def __init__(self, mass: float, gains: ControllerGains | None = None,
                 inertia: np.ndarray | None = None):
        self.mass = mass
        self.g = gains or ControllerGains()
        # per-axis torque gains = wn^2 * I  (stiffness) and 2*zeta*wn * I (damping)
        I = np.diag(inertia) if inertia is not None else np.ones(3)
        wn, z = self.g.att_bandwidth, self.g.att_damping
        self._kp_att = wn * wn * I
        self._kd_att = 2.0 * z * wn * I

    def wrench_demand(self, body: RigidBody, target_pos: np.ndarray) -> np.ndarray:
        g = self.g
        # --- outer position loop (world frame) ---
        e_pos = target_pos - body.pos
        des_acc = g.kp_pos * e_pos - g.kd_pos * body.vel      # world accel command
        # vertical force: hold weight + vertical accel term
        Fz_world = self.mass * (G0 + des_acc[2])
        # horizontal accel -> target tilt (small-angle): ax ~ g*theta
        ax, ay = des_acc[0], des_acc[1]
        theta_y = np.clip(ax / G0, -g.max_tilt, g.max_tilt)   # pitch for +x
        theta_x = np.clip(-ay / G0, -g.max_tilt, g.max_tilt)  # roll for +y

        # --- inner attitude loop (body frame) ---
        R = quat_to_rot(body.quat)                            # body->world
        # current roll/pitch from R (small-angle read-off)
        cur_roll = np.arctan2(R[2, 1], R[2, 2])
        cur_pitch = np.arctan2(-R[2, 0], np.hypot(R[2, 1], R[2, 2]))
        e_roll = theta_x - cur_roll
        e_pitch = theta_y - cur_pitch
        kp, kd = self._kp_att, self._kd_att
        tau = np.array([
            kp[0] * e_roll - kd[0] * body.omega[0],
            kp[1] * e_pitch - kd[1] * body.omega[1],
            -kd[2] * body.omega[2],                           # damp yaw
        ])

        # body-frame force: the array thrusts along +z_body; ask for the vertical
        # world force projected back (approx: thrust magnitude ~ Fz_world / cos tilt).
        Fz_body = Fz_world / max(R[2, 2], 0.5)
        F_body = np.array([0.0, 0.0, max(Fz_body, 0.0)])
        return np.concatenate([F_body, tau])
