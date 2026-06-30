from enum import Enum


class CellType(Enum):
    EMPTY = 1
    OBSTACLE = 2
    FOREST = 3
    FIRE = 4
    CINDER = 5
    ASH = 6
    GRASS = 7
    ROCK = 8
    
    
class Cell:

    def __init__(self, type: CellType, x: int, y: int, dryness01: float = 0.71, burn_modifier: float = 1.0):
        self.type = type
        self.x = x
        self.y = y
        self.dryness01 = dryness01
        self.initial_dryness01 = dryness01
        self.burn_duration = 5.0 * dryness01 * burn_modifier
        self.burn_timer = self.burn_duration
        self.burn_progress01 = 0.0

    def set_type(self, type: CellType | int):
        self.type = CellType(type)

    @staticmethod
    def create_rock(x: int, y: int):
        return Cell(CellType.ROCK, x, y, dryness=0.0)
    
    @staticmethod
    def create_dry_grass(x: int, y: int):
        return Cell(CellType.GRASS, x, y, dryness=1.0)
