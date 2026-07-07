from typing import List
from cell import Cell, CellType


class Grid:

    def __init__(self, num_rows: int, num_cols: int):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.num_burning_cells = 0
        self.fire_origins: List[Cell] = []
        self._cells: List[Cell] = []

    def get_cell(self, row: int, col: int) -> Cell | None:
        if row >= 0 and col >= 0 and row < self.num_rows and col < self.num_cols:
            return self._cells[col + self.num_cols * row]
        return None
    
    def set_cell_type(self, row: int, col: int, type: CellType | int):
        self._cells[col + self.num_cols * row].set_type(type)
        if type == CellType.FOREST:
            self._cells[col + self.num_cols * row].dryness01 = 0.71
        if type == CellType.FIRE:
            self._cells[col + self.num_cols * row].dryness01 = 0.71
            self.fire_origins.append(self._cells[col + self.num_cols * row])
            self.num_burning_cells += 1
    
    def add_cell(self, type: CellType):
        next_index = len(self._cells)
        row = next_index // self.num_cols
        col = next_index % self.num_cols
        if col > self.num_cols:
            row += 1
            col -= self.num_cols
        if row > self.num_rows:
            raise("Trying to exceed the grid size.")
        cell = Cell(type, row, col)
        if type == CellType.EMPTY:
            cell.dryness01 = 0.0
        self._cells.append(cell)
        if type == CellType.FIRE:
            self.fire_origins.append(cell)
            self.num_burning_cells += 1

    #TODO: perhaps move to interfaces.py
    def tolist2d(self) -> list[list[int]]:
        list2d = []
        for i in range(self.num_rows):
            list2d.append([])
            for j in range(self.num_cols):
                list2d[i].append(self.get_cell(i, j).type.value)
        return list2d
