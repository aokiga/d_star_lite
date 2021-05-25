import random

random.seed(100500)

from src.grid import Grid, ObservableGrid
from src.cell import *

sensors_radiuses = [1, 5, 10, 15, 20]

sensor_maps = []
denses = [random.uniform(0.1, 0.3) for _ in range(100)]

for dens in denses:
    c = [[0 for _ in range(64)] for _ in range(25)]
    for i in range(25):
        for j in range(64):
            if (random.random() < dens):
                c[i][j] = Cell(CellType.WALL)
            else:
                c[i][j] = Cell(CellType.EMPTY)
    c[0][0] = Cell(CellType.START)
    c[-1][-1] = Cell(CellType.END)
    grid = ObservableGrid(25, 64, c)
    sensor_maps.append(grid)


def test_sensor(search_function, *args):
    results = dict()
    for radius in sensors_radiuses:
        va = 0
        exp = 0
        for test_map in sensor_maps:
            f, p, nodes_opened, nodes_expanded = search_function(test_map, (0, 0), (24, 63), *args)

            va += nodes_opened.nodes_added / (64 * 25)
            exp += nodes_expanded.nodes_added / (64 * 25)

        results[radius] = (va / 100.0, exp / 100.0)
    return results
