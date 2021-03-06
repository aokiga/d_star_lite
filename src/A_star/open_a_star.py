import math

from src.node import Node
from src.open_base import OpenBase

from heapdict import heapdict


class OpenAStar(OpenBase):
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
            if item.g < self.elements[key].g:
                self.elements[key] = item
                self.heap[key] = item.f
                return True
            else:
                return False
        else:
            self.elements[key] = item
            self.heap[key] = item.f
            return True

    def get_best_node(self):
        key, _ = self.heap.popitem()
        return self.elements.pop(key)

    def remove(self, item: Node):
        key = item.i, item.j
        self.heap.pop(key)
        return self.elements.pop(key)

    def contains(self, item: Node):
        return (item.i, item.j) in self.elements
