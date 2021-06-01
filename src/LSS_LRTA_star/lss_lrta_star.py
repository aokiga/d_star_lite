import math

from src.LSS_LRTA_star.closed_lss_lrta import ClosedLRTA
from src.LSS_LRTA_star.open_lss_lrta import OpenLRTA
from src.heuristics import manhattan_distance
from src.node import Node


def reconstruct_path(v):
    ans = []
    while v.parent is not None:
        ans.append((v.i, v.j))
        v = v.parent
    return ans[::-1]


class LSS_LRTA_star:
    def __init__(self, grid, start, end, heuristic, vision, lookahead):
        self.grid = grid
        self.start = start
        self.end = end
        self.heuristic = heuristic
        self.vision = vision
        self.lookahead = lookahead
        self.open = OpenLRTA()
        self.closed = ClosedLRTA()
        self.h = dict()

    def a_star(self):
        found_flag = False
        last_node = None
        h_start = self.heuristic(self.start[0], self.start[1], self.end[0], self.end[1])
        if self.start in self.h:
            h_start = self.h[self.start]
        else:
            self.h[self.start] = h_start
        start_node = Node(self.start[0], self.start[1], 0, h_start)
        end_node = Node(self.end[0], self.end[1])
        self.open.add_node(start_node)
        expansions = 0
        while len(self.open) > 0:
            if expansions >= self.lookahead:
                break
            v = self.open.get_best_node()
            self.closed.add_node(v)
            expansions += 1
            if v == end_node:
                found_flag = True
                last_node = v
                break
            for coords in self.grid.get_neighbors(v.i, v.j):
                h_next = self.heuristic(coords[0], coords[1], self.end[0], self.end[1])
                if h_next in self.h:
                    h_next = self.h[coords]
                else:
                    self.h[coords] = h_next
                to = Node(coords[0], coords[1], v.g + 1, h_next, v)
                if self.closed.was_expanded(to):
                    continue
                self.open.add_node(to)
        return found_flag, last_node

    def dijkstra(self):
        for c in self.closed:
            self.h[(c.i, c.j)] = math.inf
        while len(self.closed) > 0:
            v = self.open.get_best_node_h()
            if self.closed.was_expanded(v):
                self.closed.remove(v)
            for coord in self.grid.get_neighbors(v.i, v.j):
                to_tmp = Node(coord[0], coord[1], math.inf, math.inf, v)
                if self.closed.was_expanded(to_tmp) and self.h[coord] > 1 + self.h[(v.i, v.j)]:
                    self.h[coord] = 1 + self.h[(v.i, v.j)]
                    to = Node(coord[0], coord[1], math.inf, self.h[coord], v)
                    self.open.add_node(to)

    def run(self):
        res_path = [self.start]
        self.grid.update_vision(self.start[0], self.start[1], self.vision)
        while self.start != self.end:
            found_path, _ = self.a_star()
            if self.open.is_empty():
                break
            ans = None
            min_dist = math.inf
            for v in self.open:
                if v.f < min_dist:
                    min_dist = v.f
                    ans = v
            self.dijkstra()
            path = reconstruct_path(ans)
            for to in path:
                if self.grid.cells[to[0]][to[1]].traversable():
                    self.start = to
                    res_path.append(to)
                    self.grid.update_vision(self.start[0], self.start[1], self.vision)
                else:
                    break
            self.open.reset()
            self.closed.reset()
        return self.start == self.end, res_path, self.open, self.closed


def lss_lrta_star(grid, start, end, heuristic=manhattan_distance, vision=1, lookahead=50):
    return LSS_LRTA_star(grid, start, end, heuristic, vision, lookahead).run()
