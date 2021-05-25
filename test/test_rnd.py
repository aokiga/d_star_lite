import random

from src.cell import Cell
from src.grid import *

random.seed(100500)

maps_sizes = [10, 15, 20, 25, 30, 35, 40]

maps = {}
for size in maps_sizes:
    cur_maps = []
    denses = [random.uniform(0.1, 0.3) for _ in range(100)]
    for dens in denses:
        c = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                if (random.random() < dens):
                    c[i][j] = Cell(CellType.WALL)
                else:
                    c[i][j] = Cell(CellType.EMPTY)
        c[0][0] = Cell(CellType.EMPTY)
        c[-1][-1] = Cell(CellType.EMPTY)
        grid = ObservableGrid(size, size, c)
        cur_maps.append(grid)
    maps[size] = cur_maps


def test_rnd(search_function, *args):
    results = dict()
    for size in maps_sizes:
        va = 0
        exp = 0
        for test_map in maps[size]:
            status, p, nodes_opened, nodes_expanded = search_function(test_map, (0, 0), (size - 1, size - 1), *args)

            va += nodes_opened.nodes_added / (size * size)
            exp += nodes_expanded.nodes_added / (size * size)

        results[size] = (va / 100.0, exp / 100.0)
    return results
