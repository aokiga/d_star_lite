from node import Node


def reconstruct_path(v):
    ans = []
    while v.parent is not None:
        ans.append((v.i, v.j))
        v = v.parent
    return ans[::-1]


def a_star(grid, start, end, OPEN, CLOSED, heuristic):
    open_set = OPEN()
    closed_set = CLOSED()
    found_flag = False
    last_node = None
    start_node = Node(start[0], start[1], 0, heuristic(start[0], start[1], end[0], end[1]))
    end_node = Node(end[0], end[1])
    open_set.add_node(start_node)
    while len(open_set) > 0:
        v = open_set.get_best_node()
        closed_set.add_node(v)
        if v == end_node:
            found_flag = True
            last_node = v
            break
        for coords in grid.get_neighbors(v.i, v.j):
            to = Node(coords[0], coords[1], v.g + 1, heuristic(coords[0], coords[1], end[0], end[1]), v)
            if closed_set.was_expanded(to):
                continue
            open_set.add_node(to)
    return found_flag, last_node, open_set, closed_set


def a_star_replanning(grid, start, end, OPEN, CLOSED, heuristic):
    cur = start
    res_path = [cur]
    while cur != end:
        grid.make_visible(cur[0], cur[1])
        found_flag, last_v, open, closed = a_star(grid, cur, end, OPEN, CLOSED, heuristic)
        if not found_flag:
            return False
        path = reconstruct_path(last_v)
        cur = path[0]
        res_path += [cur]
    return True