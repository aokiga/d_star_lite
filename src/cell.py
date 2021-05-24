from enum import Enum


class CellType(Enum):
    EMPTY = 0
    WALL = 1
    START = 2
    END = 3


class Cell:
    def __init__(self, cell_type=CellType.EMPTY, is_visible=False):
        self.type = cell_type
        self.is_visible = is_visible

    def traversable(self):
        return self.type != CellType.WALL or not self.is_visible
