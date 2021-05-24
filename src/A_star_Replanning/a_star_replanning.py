from src.A_star_Replanning.closed_a_star_replanning import ClosedAStarReplanning
from src.A_star_Replanning.open_a_star_replanning import OpenAStarReplanning
from src.a_star.a_star import a_star
from src.grid import Grid


def reconstruct_path(v):
    ans = []
    while v.parent is not None:
        ans.append((v.i, v.j))
        v = v.parent
    return ans[::-1]


def a_star_replanning(grid: Grid, start, end, heuristic, vision):
    cur = start
    res_path = [cur]
    OPEN = OpenAStarReplanning()
    CLOSED = ClosedAStarReplanning()
    path = []
    pos = 0
    while cur != end:
        new_cells = grid.update_vision(cur[0], cur[1], vision)
        if not new_cells:
            cur = path[pos]
            res_path += [cur]
            pos += 1
            continue
        OPEN.reset()
        CLOSED.reset()
        found_flag, last_v = a_star(grid, cur, end, OPEN, CLOSED, heuristic)
        if not found_flag:
            return False
        path = reconstruct_path(last_v)
        cur = path[0]
        pos = 1
        res_path += [cur]
    OPEN.reset()
    CLOSED.reset()
    return res_path, OPEN, CLOSED
