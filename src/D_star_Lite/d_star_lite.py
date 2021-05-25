import math

from src.D_star_Lite.open_d_star import OpenDStar
from src.closed_base import ClosedBase
from src.heuristics import manhattan_distance


class DStarLite:
    def __init__(self, grid, start, end, heuristics, vision):
        self.grid = grid
        self.open = OpenDStar()
        self.closed = ClosedBase()
        self.start = start
        self.end = end
        self.vision = vision
        self.g = dict()
        self.rhs = dict()
        self.g[end] = math.inf
        self.rhs[end] = 0
        self.rhs[start] = self.g[start] = math.inf
        self.k = 0
        self.h = heuristics

    def calc_key(self, v):
        return min(self.g[v], self.rhs[v]) + self.h(self.start[0], self.start[1], v[0], v[1]) + self.k, min(self.g[v], self.rhs[v])

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
            k_old = self.open.find_best()[1]
            v = self.open.get_best_node()
            self.closed.add_node(v)
            if k_old < self.calc_key(v):
                self.open.add_with_key(v, self.calc_key(v))
            elif self.g[v] > self.rhs[v]:
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

        prev = self.start
        res_path = [self.start]

        self.grid.update_vision(self.start[0], self.start[1], self.vision)

        self.compute_shortest_path()
        while self.start != self.end:
            next_v = self.start
            minD = math.inf
            for coord in self.grid.get_neighbors(self.start[0], self.start[1]):
                if coord not in self.g:
                    continue
                if minD > self.g[coord] + 1:
                    next_v = coord
                    minD = self.g[coord] + 1
            if next_v == self.start:
                break
            self.start = next_v
            #print(self.start)
            res_path.append(self.start)
            new_vertexes = self.grid.update_vision(self.start[0], self.start[1], self.vision)
            if new_vertexes:
                self.k += self.h(prev[0], prev[1], self.start[0], self.start[1])
                prev = self.start
                for v in new_vertexes:
                    if self.grid.cells[v[0]][v[1]].traversable():
                        self.update_vertex(v)
                    for coord in self.grid.get_neighbors(v[0], v[1]):
                        self.update_vertex(coord)
                self.compute_shortest_path()

        return self.start == self.end, res_path, self.open, self.closed


def d_star_lite(grid, start, end, heuristic=manhattan_distance, vision=1):
    return DStarLite(grid, start, end, heuristic, vision).run()
