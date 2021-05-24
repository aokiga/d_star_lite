from src.D_star_Lite.node_d_star import NodeD
from src.a_star.closed_a_star import ClosedAStar
from src.a_star.open_a_star import OpenAStar

#TODO("пока что нихуя не работает")

def update_vertex():
    pass


def compute_shortest_path():
    pass


def d_star_lite(grid, start, end, heuristic, vision):
    cur = start
    prev = cur
    res_path = [cur]
    OPEN = OpenAStar()
    CLOSED = ClosedAStar()
    k = 0
    grid.update_vision(start[0], start[1], vision)
    h_start = heuristic(start[0], start[1], end[0], end[1])
    OPEN.add_node(NodeD(start[0], start[1], 0, h_start, None, k))

    compute_shortest_path()
    while cur != end:
        #TODO MOVE
        new_vertexes = grid.update_vision(cur[0], cur[1], vision)
        if new_vertexes:
            k += heuristic(prev[0], prev[1], cur[0], cur[1])
            prev = cur

    return res_path, OPEN, CLOSED
