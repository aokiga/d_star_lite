import math

from src.node import Node
from src.open_base import OpenBase


class OpenAStar(OpenBase):
    def __init__(self):
        super().__init__()
        self.elements = []

    def __iter__(self):
        return iter(self.elements)

    def __len__(self):
        return len(self.elements)

    def is_empty(self):
        if len(self.elements) != 0:
            return False
        return True

    def add_node(self, item: Node):
        for elem in self.elements:
            if elem == item:
                if elem.g > item.g:
                    elem.g = item.g
                    elem.f = item.f
                    elem.parent = item.parent
                return
        self.elements.append(item)
        return

    def get_best_node(self):
        best_f = math.inf
        best_h = math.inf
        best_coord = 0
        for i in range(len(self.elements)):
            if self.elements[i].f < best_f:
                best_coord = i
                best_f = self.elements[i].f
            elif self.elements[i].f == best_f and self.elements[i].h < best_h:
                best_coord = i
                best_f = self.elements[i].f
                best_h = self.elements[i].h

        best = self.elements.pop(best_coord)
        return best
