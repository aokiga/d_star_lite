from src.A_star_Replanning.closed_a_star_replanning import ClosedAStarReplanning
from src.A_star_Replanning.open_a_star_replanning import OpenAStarReplanning
from src.a_star.a_star import a_star

def reconstruct_path(v):
    ans = []
    while v.parent is not None:
        ans.append((v.i, v.j))
        v = v.parent
    return ans[::-1]


def a_star_replanning(grid, start, end, heuristic):
    cur = start
    res_path = [cur]
    OPEN = OpenAStarReplanning()
    CLOSED = ClosedAStarReplanning()
    while cur != end:
        grid.make_visible(cur[0], cur[1])
        OPEN.reset()
        CLOSED.reset()
        found_flag, last_v = a_star(grid, cur, end, OPEN, CLOSED, heuristic)
        if not found_flag:
            return False
        path = reconstruct_path(last_v)  # TODO("Not effective")
        cur = path[0]
        res_path += [cur]
    return res_path, open, CLOSED
