import math

from src.D_star_Lite.open_d_star import OpenDStar
from src.closed_base import ClosedBase
from src.heuristics import manhattan_distance


class LPA_Star:
    def __init__(self, grid, start, end, heuristics):
        self.grid = grid
        self.open = OpenDStar()
        self.closed = ClosedBase()
        self.start = start
        self.end = end
        self.g = dict()
        self.rhs = dict()
        self.g[end] = math.inf
        self.rhs[end] = 0
        self.rhs[start] = self.g[start] = math.inf
        self.h = heuristics

    def calc_key(self, v):
        return min(self.g[v], self.rhs[v]) + self.h(self.start[0], self.start[1], v[0], v[1]), min(self.g[v], self.rhs[v])

    def update_vertex(self, v):
        if v not in self.g:
            self.g[v] = math.inf
        if v != self.end:
            rhs = math.inf
            for coord in self.grid.get_neighbors(v[0], v[1]):
                if coord in self.g:
                    rhs = min(rhs, self.g[coord] + 1)
            self.rhs[v] = rhs
        if self.open.in_heap(v):
            self.open.remove(v)
        if self.g[v] != self.rhs[v]:
            self.open.add_with_key(v, self.calc_key(v))

    def compute_shortest_path(self):
        while len(self.open) and (self.open.find_best()[1] < self.calc_key(self.start) or self.rhs[self.start] != self.g[self.start]):
            v = self.open.get_best_node()
            if self.g[v] > self.rhs[v]:
                self.closed.add_node(v)
                self.g[v] = self.rhs[v]
                for coord in self.grid.get_neighbors(v[0], v[1]):
                    self.update_vertex(coord)
            else:
                self.g[v] = math.inf
                if self.grid.cells[v[0]][v[1]].traversable():
                    self.update_vertex(v)
                for coord in self.grid.get_neighbors(v[0], v[1]):
                    self.update_vertex(coord)

    def run(self):
        self.open.add_with_key(self.end, self.calc_key(self.end))
        self.grid.update_graph()

        while True:
            self.compute_shortest_path()

            new_vertexes = self.grid.update_graph()
            if new_vertexes:
                for v in new_vertexes:
                    if self.grid.cells[v[0]][v[1]].traversable():
                        self.update_vertex(v)
                    for coord in self.grid.get_neighbors(v[0], v[1]):
                        self.update_vertex(coord)


def lpa_star(grid, start, end, heuristic=manhattan_distance):
    return LPA_Star(grid, end, start, heuristic).run()
