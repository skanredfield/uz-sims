from grid import Grid
from cell import CellType


class GridGenerator:

    @staticmethod
    def generate_empty(num_rows: int, num_cols: int) -> Grid:
        grid = Grid(num_rows, num_cols)
        for _ in range(num_rows * num_cols):
            grid.add_cell(CellType.EMPTY)

        return grid