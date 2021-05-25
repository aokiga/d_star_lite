from src.node import Node
from src.open_base import OpenBase

from heapdict import heapdict


class OpenDStar(OpenBase):
    def __init__(self):
        super().__init__()
        self.elements = dict()
        self.heap = heapdict()

    def __len__(self):
        return len(self.elements)

    def __iter__(self):
        return iter(self.elements.values())

    def is_empty(self):
        return len(self.elements) == 0

    def add_node(self, item: Node):
        super().add_node(item)
        key = item.i, item.j
        if key in self.elements:
            if item < self.elements[key]:
                self.elements[key] = item
                self.heap[key] = item.f
        else:
            self.elements[key] = item
            self.heap[key] = item.f

    def get_best_node(self):
        key, _ = self.heap.popitem()
        return self.elements.pop(key)

    def find_best(self):
        return self.heap.peekitem()

    def in_heap(self, i, j):
        return (i, j) in self.elements

    def remove(self, i, j):
        self.heap.pop((i, j))
        self.elements.pop((i, j))