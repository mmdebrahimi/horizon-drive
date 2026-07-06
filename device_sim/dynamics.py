"""6-DOF rigid-body flight dynamics (Newton-Euler), quaternion attitude."""
from __future__ import annotations
from dataclasses import dataclass, field
import numpy as np
from device_sim.constants import G0


def quat_mul(q, r):
    w0, x0, y0, z0 = q
    w1, x1, y1, z1 = r
    return np.array([
        w0*w1 - x0*x1 - y0*y1 - z0*z1,
        w0*x1 + x0*w1 + y0*z1 - z0*y1,
        w0*y1 - x0*z1 + y0*w1 + z0*x1,
        w0*z1 + x0*y1 - y0*x1 + z0*w1,
    ])


def quat_to_rot(q):
    w, x, y, z = q / np.linalg.norm(q)
    return np.array([
        [1-2*(y*y+z*z), 2*(x*y-z*w),   2*(x*z+y*w)],
        [2*(x*y+z*w),   1-2*(x*x+z*z), 2*(y*z-x*w)],
        [2*(x*z-y*w),   2*(y*z+x*w),   1-2*(x*x+y*y)],
    ])


@dataclass
class RigidBody:
    mass: float
    inertia: np.ndarray                      # 3x3 body-frame inertia tensor
    pos: np.ndarray = field(default_factory=lambda: np.zeros(3))     # world
    vel: np.ndarray = field(default_factory=lambda: np.zeros(3))     # world
    quat: np.ndarray = field(default_factory=lambda: np.array([1.0, 0, 0, 0]))  # body->world
    omega: np.ndarray = field(default_factory=lambda: np.zeros(3))   # body-frame angular vel

    def step(self, wrench_body: np.ndarray, dt: float):
        """Integrate one step under a body-frame wrench [F(3), tau(3)] + gravity."""
        F_body = wrench_body[0:3]
        tau = wrench_body[3:6]
        R = quat_to_rot(self.quat)                 # body->world

        # translation (world frame): thrust rotated to world, plus gravity
        F_world = R @ F_body
        acc = F_world / self.mass + np.array([0.0, 0.0, -G0])
        self.vel = self.vel + acc * dt
        self.pos = self.pos + self.vel * dt

        # rotation (body frame): Euler's equation
        I = self.inertia
        omega = self.omega
        ang_acc = np.linalg.solve(I, tau - np.cross(omega, I @ omega))
        self.omega = omega + ang_acc * dt

        # quaternion kinematics
        wq = np.concatenate([[0.0], self.omega])
        qdot = 0.5 * quat_mul(self.quat, wq)
        self.quat = self.quat + qdot * dt
        self.quat = self.quat / np.linalg.norm(self.quat)


def solid_disc_inertia(mass: float, radius: float, height: float = 0.4) -> np.ndarray:
    """Inertia tensor of a uniform solid cylinder (thrust disc + body), body frame."""
    Ixx = Iyy = mass * (3*radius**2 + height**2) / 12.0
    Izz = 0.5 * mass * radius**2
    return np.diag([Ixx, Iyy, Izz])
