import math

from src.D_star_Lite.closed_d_star import ClosedDStar
from src.D_star_Lite.node_d_star import NodeD
from src.D_star_Lite.open_d_star import OpenDStar
from src.cell import CellType


def calc_key(node, k):
    return min(node.g, node.rhs) + node.h + k, min(node.g, node.rhs)


def update_vertex(grid, i, j, end, OPEN, CLOSED, dist, heuristics, k):
    if (i, j) not in dist:
        dist[(i, j)] = NodeD(i, j, g=math.inf, rhs=math.inf, h=heuristics(i, j, end[0], end[1]), k=k)
    if (i, j) != end:
        rhs = math.inf
        for coord in grid.get_neighbors(i, j):
            rhs = min(rhs, dist[coord].g + 1)
        dist[(i, j)].rhs = rhs
    if OPEN.in_heap((i, j)):
        OPEN.remove(i, j)
    if CLOSED.in_closed(i, j):
        CLOSED.remove(i, j)
    if dist[(i, j)].g != dist[(i, j)].rhs:
        dist[(i, j)].f = calc_key(dist[(i, j)], k)
        OPEN.add_node(dist[(i, j)])
    else:
        CLOSED.add_node(dist[(i, j)])


def compute_shortest_path(grid, cur, end, OPEN, CLOSED, dist, heuristics, k):
    while OPEN.find_best()[1] < dist[cur].f or dist[cur].f != dist[cur].g:
        v = OPEN.get_best_node()
        if v.f < calc_key(v, k):
            dist[(v.i, v.j)].f = calc_key(dist[(v.i, v.j)], k)
            OPEN.add_node(dist[(v.i, v.j)])
        elif v.g > v.rhs:
            v.g = v.rhs
            dist[(v.i, v.j)] = v
            for coord in grid.get_neighbors(v.i, v.j):
                if grid.cells[coord[0]][coord[1]].traversable():
                    update_vertex(grid, coord[0], coord[1], end, OPEN, CLOSED, dist, heuristics, k)
        else:
            v.g = math.inf
            if grid.cells[v.i][v.y].traversable():
                update_vertex(grid, v.i, v.j, end, OPEN, CLOSED, dist, heuristics, k)
            for coord in grid.get_neighbors(v.i, v.j):
                if grid.cells[coord[0]][coord[1]].traversable():
                    update_vertex(grid, coord[0], coord[1], end, OPEN, CLOSED, dist, heuristics, k)



def d_star_lite(grid, start, end, heuristic, vision):
    cur = start
    prev = cur
    res_path = [cur]
    dist = dict()
    OPEN = OpenDStar()
    CLOSED = ClosedDStar()
    k = 0
    grid.update_vision(start[0], start[1], vision)
    h_start = heuristic(start[0], start[1], end[0], end[1])
    node_start = NodeD(start[0], start[1], 0, h_start, None, k)
    dist[start] = node_start
    OPEN.add_node(node_start)

    compute_shortest_path(grid, cur, end, OPEN, CLOSED, dist, heuristic, k)
    while cur != end:
        next_v = cur
        minD = math.inf
        for coord in grid.get_neighbors(cur[0], cur[1]):
            if coord not in dist:
                continue
            if minD > dist[coord].g + 1:
                next_v = coord
                minD = dist[coord].g + 1
        cur = next_v
        res_path.append(cur)
        new_vertexes = grid.update_vision(cur[0], cur[1], vision)
        if new_vertexes:
            k += heuristic(prev[0], prev[1], cur[0], cur[1])
            prev = cur
            for (x, y) in new_vertexes:
                if grid.cells[x][y].traversable():
                    update_vertex(grid, x, y, end, OPEN, CLOSED, dist, heuristic, k)
                for coord in grid.get_neighbors(x, y):
                    update_vertex(grid, coord[0], coord[1], end, OPEN, CLOSED, dist, heuristic, k)
            compute_shortest_path(grid, cur, end, OPEN, CLOSED, dist, heuristic, k)

    return res_path, OPEN, CLOSED
