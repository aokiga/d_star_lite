from src.A_star_Replanning.closed_a_star_replanning import ClosedAStarReplanning
from src.A_star_Replanning.open_a_star_replanning import OpenAStarReplanning
from src.a_star.a_star import a_star
from src.heuristics import manhattan_distance


def reconstruct_path(v):
    ans = []
    while v.parent is not None:
        ans.append((v.i, v.j))
        v = v.parent
    return ans[::-1]


def a_star_replanning(grid, start, end, heuristic=manhattan_distance, vision=1):
    cur = start
    res_path = [cur]
    OPEN = OpenAStarReplanning()
    CLOSED = ClosedAStarReplanning()

    grid.update_vision(cur[0], cur[1], vision)
    found_flag, last_v = a_star(grid, cur, end, OPEN, CLOSED, heuristic)
    if not found_flag:
        OPEN.reset()
        CLOSED.reset()
        return False, res_path, OPEN, CLOSED

    path = reconstruct_path(last_v)
    cur = path[0]
    pos = 1
    res_path += [cur]

    #print(grid.cells[cur[0]][cur[1]].is_visible, grid.cells[cur[0]][cur[1]].type)
    while cur != end:
        #print("Current cell:", cur[0], cur[1])
        #print(grid.cells[cur[0]][cur[1]].is_visible, grid.cells[cur[0]][cur[1]].type)
        new_cells = grid.update_vision(cur[0], cur[1], vision)
        #print("Updated vision: " +  "\n".join(map(lambda x: str(x), new_cells)) + '\n')
        if not new_cells:
            cur = path[pos]
            res_path += [cur]
            pos += 1
            continue

        OPEN.reset()
        CLOSED.reset()
        found_flag, last_v = a_star(grid, cur, end, OPEN, CLOSED, heuristic)
        if not found_flag:
            break
        path = reconstruct_path(last_v)
        cur = path[0]
        pos = 1
        res_path += [cur]
    OPEN.reset()
    CLOSED.reset()
    return found_flag, res_path, OPEN, CLOSED
