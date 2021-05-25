import math

from src.A_star.a_star import a_star
from src.A_star.closed_a_star import ClosedAStar
from src.A_star.open_a_star import OpenAStar
from src.LSS_LRTA_star.closed import ClosedLRTA
from src.LSS_LRTA_star.open import OpenLRTA
from src.heuristics import manhattan_distance


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
        self.h = heuristic
        self.vision = vision
        self.lookahead = lookahead
        self.open = OpenLRTA()
        self.closed = ClosedLRTA()

    def run(self):
        path = [self.start]
        self.grid.update_vision(self.start[0], self.start[1], self.vision)
        while self.start != self.end:
            print("suka")
            found_path, last = a_star(self.grid, self.start, self.end, self.open, self.closed, self.h, self.lookahead)
            if self.open.is_empty() and not found_path:
                break
            ans = None
            min_dist = math.inf
            for v in self.closed:
                if v.f < min_dist:
                    min_dist = v.f
                    ans = v
            if not ans:
                break
            path = reconstruct_path(ans)
            for to in path:
                if self.grid.cells[to[0]][to[1]].traversable():
                    self.start = to
                    path.append(to)
                    self.grid.update_vision(self.start[0], self.start[1], self.vision)
            self.open.reset()
            self.closed.reset()
        return self.start == self.end, path, self.open, self.closed


def lss_lrta_star(grid, start, end, heuristic=manhattan_distance, vision=1, lookahead=10):
    return LSS_LRTA_star(grid, start, end, heuristic, vision, lookahead).run()
