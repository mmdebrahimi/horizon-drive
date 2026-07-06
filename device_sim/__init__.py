"""device_sim — digital twin of the quantised-inertia / horizon-drive thruster craft.

Suspend-disbelief engineering simulation (physics ASSUMED proven): models the
superconducting thruster array, its 6-DOF flight dynamics, and a fly-by-wire
control-allocation loop, so the control approach can be validated before any
hardware exists. Physics + budget provenance: research_outputs/antigravity-
working-device-build-instructions-2026-07-04.md (verified /tmp/craft.py).

Thrust law:  F = eta * P * Q / c   (eta=0.0072 calibrated to Eagleworks; Q=1e10).
"""
from device_sim.constants import DesignParams, default_params, C, G0

__all__ = ["DesignParams", "default_params", "C", "G0"]
