import math


def manhattan_distance(x1, y1, x2, y2):
    d1 = abs(x1 - x2)
    d2 = abs(y1 - y2)
    return d1 + d2