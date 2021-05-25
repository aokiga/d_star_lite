import math

from src.node import Node


class NodeD(Node):
    def __init__(self, i, j, g=math.inf, h=math.inf, parent=None, rhs=math.inf, k=0):
        super().__init__(i, j, g, h, parent)
        self.rhs = rhs
        self.f = (min(self.g, self.rhs) + self.h + k, min(self.g, self.rhs))

    def __lt__(self, other):
        return self.f < other.f
