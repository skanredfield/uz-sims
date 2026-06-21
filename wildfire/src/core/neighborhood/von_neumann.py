from typing import override
from neighborhood import Neighborhood
from grid import Grid


class VonNeumannNeighborhood(Neighborhood):

    @override
    def get_neighborhood(cls, row: int, col: int, grid: Grid):
        neightbors = []
        cls._append_if_not_none(neightbors, grid.get_cell(row, col-1))
        cls._append_if_not_none(neightbors, grid.get_cell(row, col+1))
        cls._append_if_not_none(neightbors, grid.get_cell(row+1, col))
        cls._append_if_not_none(neightbors, grid.get_cell(row-1, col))
        return neightbors
