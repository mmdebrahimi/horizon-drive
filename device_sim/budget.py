"""Power / thermal / mass budget — ports the verified /tmp/craft.py figures."""
from __future__ import annotations
from dataclasses import dataclass
import math
from device_sim.constants import DesignParams, G0
from device_sim.cell import cell_thrust


@dataclass
class BudgetReport:
    thrust_per_cell_N: float
    cells: int
    rf_power_kW: float
    cryo_cop: float
    cryo_power_kW: float
    control_power_kW: float
    total_power_kW: float
    cryocooler_mass_kg: float
    core_dry_mass_kg: float
    # endurance (source-mass for a target minutes)
    def battery_mass_kg(self, minutes: float, wh_per_kg: float = 250.0) -> float:
        return (self.total_power_kW * 1000.0 * minutes / 60.0) / wh_per_kg  # Wh / (Wh/kg)


def budget_report(p: DesignParams) -> BudgetReport:
    f_cell = cell_thrust(p.cell_power_W, p.Q, p.eta)
    cells = math.ceil(p.twr * p.craft_mass_kg * G0 / f_cell)

    rf_W = cells * p.cell_power_W
    # cryogenics: Carnot COP * realistic fraction; input power = heat_leak / COP
    carnot = p.cryo_cold_T / (p.cryo_reject_T - p.cryo_cold_T)
    cop = carnot * p.cryo_carnot_frac
    heat_leak_W = cells * p.heat_leak_per_cell_W
    cryo_W = heat_leak_W / cop

    total_W = rf_W + cryo_W + p.control_power_W

    cryocooler_kg = (cryo_W / 1000.0) * p.cryocooler_kg_per_kW
    dry = (cells * p.mass_per_cell_kg
           + p.cryostat_mass_kg
           + cryocooler_kg
           + (rf_W / 1000.0) * p.rf_amp_kg_per_kW
           + p.structure_mass_kg
           + p.avionics_mass_kg)

    return BudgetReport(
        thrust_per_cell_N=f_cell,
        cells=cells,
        rf_power_kW=rf_W / 1000.0,
        cryo_cop=cop,
        cryo_power_kW=cryo_W / 1000.0,
        control_power_kW=p.control_power_W / 1000.0,
        total_power_kW=total_W / 1000.0,
        cryocooler_mass_kg=cryocooler_kg,
        core_dry_mass_kg=dry,
    )
