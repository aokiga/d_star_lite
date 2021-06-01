from src.cell import CellType
import math


def euclid_distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


class Grid:
    def __init__(self, height=0, width=0, cells=None):
        self.cells = cells if cells else []
        self.height = height
        self.width = width

    def in_bounds(self, i, j):
        return (0 <= j < self.width) and (0 <= i < self.height)

    def traversable(self, i, j):
        return self.cells[i][j].traversable()

    def get_neighbors(self, i, j):
        delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        neighbors = []
        for dx, dy in delta:
            x, y = dx + i, dy + j
            if self.in_bounds(x, y) and self.traversable(x, y):
                neighbors.append((x, y))
            else:
                pass
                #if (self.in_bounds(x, y)):
                    #print("lkjdnjkas", x, y)
        return neighbors


class ObservableGrid(Grid):
    def __init__(self, height=0, width=0, cells=None):
        super().__init__(height, width, cells)

    def is_visible(self, x1, y1, x2, y2):
        if x1 == x2:
            for i in range(min(y1, y2) + 1, max(y1, y2)):
                if self.cells[x1][i].type == CellType.WALL:
                    return False
            return True
        if y1 == y2:
            for i in range(min(x1, x2) + 1, max(x1, x2)):
                if self.cells[i][y1].type == CellType.WALL:
                    return False
            return True
        if x1 > x2:
            x1, y1, x2, y2 = x2, y2, x1, y1
        len = (y2 - y1) / (x2 - x1)
        sign = 1 if (y2 > y1) else -1
        cur = y1
        prev = y1
        for i in range(x1, x2):
            cur += len
            next1 = math.floor(cur)
            for j in range(prev, next1 + sign, sign):
                if self.cells[i][j].type == CellType.WALL:
                    return False
            prev = next1
        return True

    def update_vision(self, x, y, radius):
        new_cells = []
        for i in range(max(0, x - radius), min(x + radius + 1, self.height)):
            for j in range(max(0, y - radius), min(y + radius + 1, self.width)):
                if euclid_distance(i, j, x, y) > radius:
                    continue
                if self.cells[i][j].is_visible:
                    continue
                if self.is_visible(x, y, i, j):
                    self.cells[i][j].is_visible = True
                    new_cells.append((i, j))
        return new_cells

    def make_visible(self, flag):
        for l in self.cells:
            for cell in l:
                cell.is_visible = flag
