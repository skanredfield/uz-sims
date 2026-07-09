from typing import override
from grid import Grid
from src.core.neighborhood.neighborhood import Neighborhood


class MooreNeighborhood(Neighborhood):

    @classmethod
    @override
    def get_neighborhood(cls, row: int, col: int, grid: Grid):
        neighbors = []
        cls._append_if_not_none(neighbors, grid.get_cell(row, col-1))
        cls._append_if_not_none(neighbors, grid.get_cell(row, col+1))
        cls._append_if_not_none(neighbors, grid.get_cell(row+1, col))
        cls._append_if_not_none(neighbors, grid.get_cell(row-1, col))
        cls._append_if_not_none(neighbors, grid.get_cell(row-1, col-1))
        cls._append_if_not_none(neighbors, grid.get_cell(row+1, col+1))
        cls._append_if_not_none(neighbors, grid.get_cell(row+1, col-1))
        cls._append_if_not_none(neighbors, grid.get_cell(row-1, col+1))
        return neighbors
