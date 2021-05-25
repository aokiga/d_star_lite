from src.a_star.closed_a_star import ClosedAStar
from src.a_star.open_a_star import OpenAStar
from src.heuristics import manhattan_distance

# TODO("  ")

def lss_lrta_star(grid, start, end, heuristic=manhattan_distance, vision=1):
    OPEN = OpenAStar()
    CLOSED = ClosedAStar()
    cur = start
    while start != end:
        pass
