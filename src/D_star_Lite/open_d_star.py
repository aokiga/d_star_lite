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

    def add_with_key(self, item, prior):
        super().add_node(item)
        self.elements[item] = item
        self.heap[item] = prior

    def get_best_node(self):
        key, _ = self.heap.popitem()
        return self.elements.pop(key)

    def find_best(self):
        return self.heap.peekitem()

    def in_heap(self, v):
        return v in self.elements

    def remove(self, v):
        self.heap.pop(v)
        self.elements.pop(v)
