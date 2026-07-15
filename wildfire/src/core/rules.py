import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "neighborhood"))

from cell import Cell, CellType
from grid import Grid
from neighborhood.von_neumann import VonNeumannNeighborhood
# from neighborhood.moore import MooreNeighborhood


def burn(cell: Cell, grid: Grid, timestep: float):
    # print(f"Cell ({cell.row}, {cell.col}) has {cell.fuel01} fuel left and {cell.burn_progress01} burn progress")

    match(cell.type):
        case CellType.FIRE:
            if cell.burn_progress01 >= 0.7:
                cell.set_type(CellType.CINDER)
            else:
                propagate(cell, grid)
        case CellType.CINDER:
            if cell.burn_progress01 >= 1.0:
                cell.set_type(CellType.ASH)
        case _:
            pass

    if cell.type == CellType.FIRE or cell.type == CellType.CINDER:
        cell.fuel01 -= 0.1 * timestep
        if cell.fuel01 < 0.0:
            cell.fuel01 = 0.0
        cell.burn_progress01 = 1.0 - cell.fuel01 / cell.initial_fuel01



def propagate(cell: Cell, grid: Grid):
        neighbors = VonNeumannNeighborhood.get_neighborhood(cell.row, cell.col, grid)
        for n in neighbors:
            if n.fuel01 > 0.0 and n.type != CellType.FIRE:
                n.set_type(CellType.FIRE)
