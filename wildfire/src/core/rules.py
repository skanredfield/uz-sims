import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "neighborhood"))

from cell import Cell, CellType
from grid import Grid
from neighborhood.von_neumann import VonNeumannNeighborhood
from neighborhood.moore import MooreNeighborhood


COMBUSTION_DRYNESS_THRESHOLD = 0.7

def burn(cell: Cell, grid: Grid, timestep: float):
    if cell.burn_timer > 0 and cell.dryness01 > COMBUSTION_DRYNESS_THRESHOLD:
        cell.burn_timer -= timestep
        cell.burn_progress01 = 1.0 - cell.burn_timer / cell.burn_duration
        range_conversion_factor = (1.0 - cell.initial_dryness01) # / 1.0 (technically divided by the old range, which happens to be 1.0 - 0.0)
        dryness_progress01 = cell.burn_progress01 * range_conversion_factor + cell.initial_dryness01
        cell.dryness01 = cell.dryness01 + dryness_progress01

        if cell.type != CellType.FIRE:
            cell.set_type(CellType.FIRE)
            grid.num_burning_cells += 1


def propagate(cell: Cell, grid: Grid, timestep: float):
    if cell.type == CellType.FIRE:
        neighbors = VonNeumannNeighborhood.get_neighborhood(cell.row, cell.col, grid)
        for n in neighbors:
            burn(n, grid, timestep)

def update_state(cell: Cell, grid: Grid):
    match(cell.type):
        case CellType.FIRE:
            if cell.burn_progress01 >= 0.7:
                cell.set_type(CellType.CINDER)
        case CellType.CINDER:
            if cell.burn_progress01 >= 1.0:
                cell.set_type(CellType.ASH)
                grid.num_burning_cells -= 1
        case _:
            pass