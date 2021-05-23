import math

from src.node import Node
from src.closed_base import ClosedBase
from src.open_base import Open

"""
TODO("LPA_STAR")

class LPA_Star:
    def __init__(self, grid, start, end, heuristic):
        self.grid = grid
        self.start = start
        self.end = end
        self.heuristic = heuristic
        self.open = Open()
        self.closed = Closed()

    class NodeLPA(Node):
        def __init__(self, i, j, g=math.inf, rhs=math.inf, h=math.inf, parent=None):
            super().__init__(i, j, g, h, parent)
            self.rhs = rhs

    def init(self):
        pass

    def calc_key(self, node):
        return min(node.g, node.rhs) + node.h, min(node.g, node.rhs)

    def update(self, node):
        if (node.i, node.j) == self.start:
            return
        node.rhs = math.inf
        

    def compute_shortest_path(self):
        end_node = self.NodeLPA(self.end[0], self.end[1])
        while not open_set.is_empty():
            v = open_set.get_best_node()
            if closed_set.was_expanded(end):
                end_node = closed_set.get_g(end_node)

            for coords in grid.get_neighbors(v.i, v.j):
                pass

    def run(self):
        h_start = self.heuristic(self.start[0], self.start[1], self.end[0], self.end[1])
        self.open.add_node(self.NodeLPA(self.start[0], self.start[1], g=0, rhs=0, h=h_start))
        while True:
            self.compute_shortest_path()
            return
            
"""
