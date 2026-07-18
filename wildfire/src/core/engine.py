from grid import Grid
from grid_generator import GridGenerator
from cell import CellType
from rules import burn


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

def gather_updateable(grid: Grid):
    for cell in grid._cells:
        if cell.fuel01 >= 0.0:
            if cell.type == CellType.FIRE or cell.type == CellType.CINDER:
                grid.enqueue_for_update(cell)

def sim_advance_state(grid: Grid, dt: float) -> bool:
    is_any_fuel_left = False
    while not grid.are_updates_finished():
        cell = grid.get_cell_for_update()
        is_any_fuel_left = True
        burn(cell, grid, dt)
    
    return is_any_fuel_left


