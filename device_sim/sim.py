"""Closed-loop simulation harness + scenarios (hover, translate, quench)."""
from __future__ import annotations
from dataclasses import dataclass, field
import numpy as np
from device_sim.constants import DesignParams, default_params
from device_sim.array import ThrusterArray
from device_sim.allocation import allocate
from device_sim.dynamics import RigidBody, solid_disc_inertia, quat_to_rot
from device_sim.controller import FlightController
from device_sim.actuator import SlewActuator
from device_sim.sensors import Sensors, SensorNoise
from device_sim.estimator import StateEstimator
from device_sim.constants import G0


@dataclass
class SimResult:
    t: np.ndarray
    pos: np.ndarray            # (T,3)
    tilt_deg: np.ndarray       # (T,) max roll/pitch magnitude in degrees
    max_pos_err: float
    max_tilt_deg: float
    diverged: bool


def _tilt_deg(body: RigidBody) -> float:
    R = quat_to_rot(body.quat)
    roll = np.degrees(np.arctan2(R[2, 1], R[2, 2]))
    pitch = np.degrees(np.arctan2(-R[2, 0], np.hypot(R[2, 1], R[2, 2])))
    return float(max(abs(roll), abs(pitch)))


def run(target_pos=np.array([0.0, 0.0, 0.0]),
        duration=60.0, dt=0.01,
        params: DesignParams | None = None,
        quench_at: float | None = None, quench_cells: int = 1,
        start_pos=np.array([0.0, 0.0, 0.0]),
        slew_hz: float | None = None,
        sensor_noise: SensorNoise | None = None,
        use_estimator: bool = False,
        seed: int = 0) -> SimResult:
    """Closed-loop run.

    slew_hz        None -> ideal thrust; else per-cell first-order actuator lag (10-100 Hz).
    sensor_noise   None -> perfect sensing; else Gaussian noise on pos/att/gyro.
    use_estimator  True -> controller flies on a Kalman/complementary ESTIMATE of the
                   noisy measurements (not ground truth). Metrics track the TRUE trajectory.
    """
    p = params or default_params()
    array = ThrusterArray(p)
    inertia = solid_disc_inertia(p.craft_mass_kg, p.array_radius_m)
    body = RigidBody(mass=p.craft_mass_kg, inertia=inertia,
                     pos=np.asarray(start_pos, float).copy())
    ctrl = FlightController(mass=p.craft_mass_kg, inertia=inertia)
    actuator = SlewActuator(array.n, slew_hz) if slew_hz else None

    sensing = (sensor_noise is not None) or use_estimator
    sensors = Sensors(sensor_noise, seed=seed) if sensing else None
    est = StateEstimator(pos0=start_pos,
                         pos_sigma=(sensor_noise.pos_sigma if sensor_noise else 0.03)) \
        if use_estimator else None
    last_accel = np.zeros(3)

    n = int(duration / dt)
    ts = np.zeros(n); poss = np.zeros((n, 3)); tilts = np.zeros(n)
    quenched = False
    diverged = False
    for k in range(n):
        t = k * dt
        if quench_at is not None and not quenched and t >= quench_at:
            for i in range(min(quench_cells, array.n)):
                array.cells[i].healthy = False
            quenched = True

        # --- state for the controller: estimate, raw noisy, or ground truth ---
        if est is not None:
            meas = sensors.measure(body)
            est.predict(last_accel, dt)
            est.update(meas)
            ctrl_state = est.estimate()
        else:
            ctrl_state = body

        demand = ctrl.wrench_demand(ctrl_state, np.asarray(target_pos, float))
        amp_cmd = allocate(array, demand)
        amps = actuator.update(amp_cmd, dt) if actuator is not None else amp_cmd
        w = array.wrench(amps)
        body.step(w, dt)

        if est is not None:                        # feed the KF the applied accel (est frame)
            R_est = quat_to_rot(est.quat)
            last_accel = R_est @ (w[0:3] / p.craft_mass_kg) + np.array([0, 0, -G0])
        ts[k] = t; poss[k] = body.pos; tilts[k] = _tilt_deg(body)
        if (not np.all(np.isfinite(body.pos))) or np.linalg.norm(body.pos - target_pos) > 50.0:
            diverged = True
            ts = ts[:k+1]; poss = poss[:k+1]; tilts = tilts[:k+1]
            break

    errs = np.linalg.norm(poss - np.asarray(target_pos, float), axis=1)
    # settling metrics: ignore the first 20% (transient) for the hold check
    hold = slice(int(len(errs) * 0.2), None)
    return SimResult(
        t=ts, pos=poss, tilt_deg=tilts,
        max_pos_err=float(errs[hold].max()) if len(errs) else float("inf"),
        max_tilt_deg=float(tilts[hold].max()) if len(tilts) else float("inf"),
        diverged=diverged,
    )
