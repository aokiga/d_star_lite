from src.grid import Grid
from test.movingAI_loader import *

datasets = ['test1', 'test2', 'test3']


def test_mai(search_function, *args):
    results = dict()
    for dataset in datasets:
        va = 0
        exp = 0

        width, height, cells = read_map_from_ai_file("data/" + dataset + ".map")
        task_grid = Grid(width, height, cells)
        tasks = read_tasks_from_ai_file("data/" + dataset + ".scen")

        for task in tasks:
            nodes_opened, nodes_expanded = search_function(task_grid, task[0], task[1], task[2], task[3], *args)

            va += nodes_opened.va / (width * height)
            exp += nodes_expanded.exp / (width * height)

        results[dataset] = (va / 100.0, exp / 100.0)

    return results
