from grid import Grid
from grid_generator import GridGenerator
from cell import CellType
from rules import burn, propagate, update_state
from appstate import AppState

import time


TIMESTEP = 0.00005
PROPAGATION_DELAY = 1.0

def init_grid() -> Grid:
    grid = GridGenerator.generate_empty(10, 10)
    grid.set_cell_type(5, 5, CellType.FIRE)

    grid.set_cell_type(4, 4, CellType.FOREST)
    grid.set_cell_type(4, 5, CellType.FOREST)
    grid.set_cell_type(4, 6, CellType.FOREST)
    grid.set_cell_type(5, 4, CellType.FOREST)
    grid.set_cell_type(5, 6, CellType.FOREST)
    grid.set_cell_type(6, 4, CellType.FOREST)
    grid.set_cell_type(6, 5, CellType.FOREST)
    grid.set_cell_type(6, 6, CellType.FOREST)

    return grid

def logic_loop(grid: Grid, appstate: AppState):
    for cell in grid._cells:
        if cell.fuel01 <= 0:
            continue
        propagate(cell, grid, TIMESTEP)
        burn(cell, grid, TIMESTEP)
        update_state(cell, grid)

    appstate.mark_update_available()
