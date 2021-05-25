import math

from src.node import Node


def a_star(grid, start, end, open_set, closed_set, heuristic, lookahead=math.inf):
    found_flag = False
    last_node = None
    start_node = Node(start[0], start[1], 0, heuristic(start[0], start[1], end[0], end[1]))
    end_node = Node(end[0], end[1])
    open_set.add_node(start_node)
    expansions = 0
    while len(open_set) > 0:
        if expansions >= lookahead:
            break
        v = open_set.get_best_node()
        closed_set.add_node(v)
        expansions += 1
        if v == end_node:
            found_flag = True
            last_node = v
            break
        for coords in grid.get_neighbors(v.i, v.j):
            to = Node(coords[0], coords[1], v.g + 1, heuristic(coords[0], coords[1], end[0], end[1]), v)
            if closed_set.was_expanded(to):
                continue
            open_set.add_node(to)
    return found_flag, last_node
