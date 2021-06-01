import random

from src.A_star.a_star import a_star
from src.A_star.closed_a_star import ClosedAStar
from src.A_star.open_a_star import OpenAStar
from src.cell import Cell
from src.grid import *
from src.heuristics import manhattan_distance

random.seed(100500)

maps_number = 100
maps_size = 50


def is_good_map(Map, start, end):
    Map.make_visible(True)
    found_flag, _ = a_star(Map, start, end, OpenAStar(), ClosedAStar())
    Map.make_visible(False)
    return found_flag


maps = []

denses = [random.uniform(0.1, 0.3) for _ in range(maps_number)]
for dens in denses:
    c = [[0 for _ in range(maps_size)] for _ in range(maps_size)]
    for i in range(maps_size):
        for j in range(maps_size):
            if random.random() < dens:
                c[i][j] = Cell(CellType.WALL)
            else:
                c[i][j] = Cell(CellType.EMPTY)
    c[0][0] = Cell(CellType.EMPTY)
    c[-1][-1] = Cell(CellType.EMPTY)
    grid = ObservableGrid(maps_size, maps_size, c)
    if is_good_map(grid, (0, 0), (maps_size - 1, maps_size - 1)):
        maps.append(grid)


def test_big(search_function, *args):
    va = 0
    exp = 0
    length = 0
    for cur_map in maps:
        status, p, nodes_opened, nodes_expanded = search_function(cur_map, (0, 0), (maps_size - 1, maps_size - 1),
                                                                  manhattan_distance, 1, *args)

        va += nodes_opened.nodes_added / (maps_size * maps_size)
        exp += nodes_expanded.nodes_added / (maps_size * maps_size)
        length += len(p) / (maps_size * maps_size)

    return va / 100.0, exp / 100.0, length / 100.0
