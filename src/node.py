import math


class Node:
    def __init__(self, i, j, g=math.inf, h=math.inf, parent=None):
        self.i = i
        self.j = j
        self.g = g
        self.h = h
        self.parent = parent
        self.f = self.g + self.h

    def __hash__(self):
        return hash((self.i, self.j))

    def __eq__(self, other):
        return (self.i, self.j) == (other.i, other.j)

    def __lt__(self, other):
        return (self.f < other.f) or (self.f == other.f and self.h < other.h)
