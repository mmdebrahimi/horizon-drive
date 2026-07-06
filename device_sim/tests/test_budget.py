"""Budget must reproduce the verified figures within 2%."""
import math
from device_sim import default_params
from device_sim.cell import cell_thrust
from device_sim.budget import budget_report


def _close(a, b, tol=0.02):
    return abs(a - b) <= tol * abs(b)


def test_cell_thrust_240N():
    p = default_params()
    assert _close(cell_thrust(1000.0, p.Q, p.eta), 240.0)


def test_budget_matches_verified():
    r = budget_report(default_params())
    assert r.cells == 62
    assert _close(r.rf_power_kW, 62.0)
    assert _close(r.cryo_power_kW, 61.0, tol=0.03)
    assert _close(r.total_power_kW, 126.0, tol=0.03)
    assert _close(r.cryocooler_mass_kg, 490.0, tol=0.05)
    assert 1050 <= r.core_dry_mass_kg <= 1150   # ~1,100 kg


def test_battery_does_not_close():
    r = budget_report(default_params())
    # 60-min Li-ion battery is heavy (~505 kg) — the endurance wall
    assert r.battery_mass_kg(60.0) > 450.0
