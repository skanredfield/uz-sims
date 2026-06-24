from enum import Enum


class CellType(Enum):
    EMPTY = 1
    OBSTACLE = 2
    FOREST = 3
    FIRE = 4
    CINDER = 5
    ASH = 6
    
    
class Cell:

    def __init__(self, type: CellType):
        self.type = type

    def set_type(self, type: CellType | int):
        self.type = CellType(type)
