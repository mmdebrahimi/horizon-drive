"""Control allocation: 6-DOF wrench demand -> per-cell amplitudes.

Fast path: a cached weighted pseudo-inverse (recomputed only when the healthy-cell
set changes) gives the unconstrained least-squares solution; if it already lies in
[0,1] (the common hover/translate case) it is returned directly. Only when the box
is violated do we fall back to scipy's bounded solve (lsq_linear). Force rows are
weighted above torque rows so vertical hold is never sacrificed. Quenched cells are
dropped from the solve entirely, so neighbours reallocate.
"""
from __future__ import annotations
import numpy as np

try:
    from scipy.optimize import lsq_linear
    _HAVE_SCIPY = True
except Exception:                       # pragma: no cover - fallback path
    _HAVE_SCIPY = False

from device_sim.array import ThrusterArray

# row weights: [Fx,Fy,Fz, Tx,Ty,Tz] — vertical force dominates, then torque.
_ROW_W = np.array([1.0, 1.0, 4.0, 2.0, 2.0, 2.0])
_SW = np.sqrt(_ROW_W)


def _solver(array: ThrusterArray, healthy: np.ndarray):
    """Return (weighted-B on healthy cols, healthy indices, weighted pinv), cached
    on the array keyed by the healthy-cell signature."""
    sig = healthy.tobytes()
    cache = getattr(array, "_alloc_cache", None)
    if cache is not None and cache[0] == sig:
        return cache[1], cache[2], cache[3]
    cols = np.where(healthy)[0]
    Bw = (array.effectiveness() * _SW[:, None])[:, cols]
    pinv = np.linalg.pinv(Bw)
    array._alloc_cache = (sig, Bw, cols, pinv)
    return Bw, cols, pinv


def allocate(array: ThrusterArray, wrench_demand: np.ndarray,
             health_weights: np.ndarray | None = None) -> np.ndarray:
    """Return per-cell amplitudes (in [0,1]) that best meet the wrench demand."""
    n = array.n
    d = np.asarray(wrench_demand, float)
    if health_weights is None:
        healthy = np.array([c.healthy for c in array.cells], dtype=bool)
    else:
        healthy = np.asarray(health_weights, float) > 0.5

    amps = np.zeros(n)
    Bw, cols, pinv = _solver(array, healthy)
    if cols.size == 0:
        return amps

    dw = d * _SW
    x = pinv @ dw                                   # fast unconstrained solve
    if x.min() >= -1e-9 and x.max() <= 1.0 + 1e-9:  # already in the box -> done
        amps[cols] = np.clip(x, 0.0, 1.0)
        return amps

    if _HAVE_SCIPY:                                 # box violated -> bounded solve
        res = lsq_linear(Bw, dw, bounds=(0.0, 1.0), method="bvls", max_iter=200)
        amps[cols] = np.clip(res.x, 0.0, 1.0)
    else:                                           # pragma: no cover
        amps[cols] = np.clip(x, 0.0, 1.0)
    return amps
