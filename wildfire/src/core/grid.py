from typing import List
from cell import Cell, CellType


class Grid:

    def __init__(self, num_rows: int, num_cols: int):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._cells: List[Cell] = []

    def get_cell(self, row: int, col: int) -> Cell | None:
        if row >= 0 and col >= 0 and row < self.num_rows and col < self.num_cols:
            return self._cells[col + self.num_cols * row]
        return None
    
    def set_cell_type(self, row: int, col: int, type: CellType | int):
        self._cells[col + self.num_cols * row].set_type(type)
    
    def add_cell(self, type: CellType):
        self._cells.append(Cell(type))

    #TODO: perhaps move to interfaces.py
    def tolist2d(self) -> list[list[int]]:
        list2d = []
        for i in range(self.num_rows):
            list2d.append([])
            for j in range(self.num_cols):
                list2d[i].append(self.get_cell(i, j).type.value)
        return list2d
