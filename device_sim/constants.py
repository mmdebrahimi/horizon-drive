"""Physical constants + frozen design parameters (provenance-documented)."""
from __future__ import annotations
from dataclasses import dataclass
import math

# --- physical constants (CODATA) ---
C = 2.99792458e8       # speed of light, m/s
G0 = 9.80665           # standard gravity, m/s^2


@dataclass(frozen=True)
class DesignParams:
    """Frozen craft/effect design parameters.

    Defaults reproduce the verified budget in the build-instructions memo:
    240 N per 1 kW cell (Q=1e10), 62 cells for a 1000 kg craft at TWR 1.5,
    ~126 kW total electrical, ~490 kg of cryocoolers.
    """
    # effect / thrust law
    eta: float = 0.0072            # geometry/efficiency, calibrated to Eagleworks 1.2 mN/kW @ Q~5e4
    Q: float = 1.0e10              # SRF cavity quality factor (Nb at 4 K)
    cell_power_W: float = 1000.0   # RF power per cell

    # craft
    craft_mass_kg: float = 1000.0
    twr: float = 1.5               # design thrust-to-weight (useful flight, not just hover)

    # array geometry (hex-ish disc on the underside)
    array_radius_m: float = 1.2    # radius over which cells are distributed
    yaw_cant_rad: float = 0.05     # small tangential cant enabling a yaw couple

    # cryogenics (4 K stage)
    cryo_reject_T: float = 300.0   # warm-side reject temperature, K
    cryo_cold_T: float = 4.0       # cold stage, K
    cryo_carnot_frac: float = 0.15 # fraction-of-Carnot of a real cryocooler
    heat_leak_per_cell_W: float = 2.0

    # masses (kg) for the dry-mass rollup
    mass_per_cell_kg: float = 3.0
    cryostat_mass_kg: float = 120.0
    cryocooler_kg_per_kW: float = 8.0   # compressor mass per kW input
    rf_amp_kg_per_kW: float = 1.5
    structure_mass_kg: float = 180.0
    avionics_mass_kg: float = 40.0
    control_power_W: float = 3000.0

    def cells_needed(self) -> int:
        """Cells to reach the design thrust-to-weight."""
        from device_sim.cell import cell_thrust
        f_total = self.twr * self.craft_mass_kg * G0
        return math.ceil(f_total / cell_thrust(self.cell_power_W, self.Q, self.eta))


def default_params() -> DesignParams:
    """The verified baseline design."""
    return DesignParams()
