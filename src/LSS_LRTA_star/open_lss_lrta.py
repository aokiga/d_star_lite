from heapdict import heapdict

from src.A_star.open_a_star import OpenAStar
from src.node import Node
from src.open_base import OpenBase


class OpenAStarH(OpenBase):
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
        self.elements[key] = item
        self.heap[key] = item.h

    def get_best_node(self):
        key, _ = self.heap.popitem()
        return self.elements.pop(key)

    def remove(self, item: Node):
        key = item.i, item.j
        self.heap.pop(key)
        return self.elements.pop(key)


class OpenLRTA(OpenBase):
    def __init__(self):
        super().__init__()
        self.open = OpenAStar()
        self.open_h = OpenAStarH()

    def reset(self):
        self.nodes_added += self.open.nodes_added
        self.nodes_added += self.open_h.nodes_added
        self.open = OpenAStar()
        self.open_h = OpenAStarH()

    def __iter__(self):
        return self.open.__iter__()

    def __len__(self):
        return len(self.open)

    def is_empty(self):
        return self.open.is_empty()

    def add_node(self, item: Node, flag=True):
        if flag:
            if self.open.add_node(item):
                self.open_h.add_node(item)
        else:
            self.open.add_node(item)
            self.open_h.add_node(item)

    def get_best_node(self):
        ans = self.open.get_best_node()
        self.open_h.remove(ans)
        return ans

    def get_best_node_h(self):
        ans = self.open_h.get_best_node()
        self.open.remove(ans)
        return ans

    def get_best_key(self):
        key, prior = self.open.heap.peekitem()
        return prior

    def contains(self, item: Node):
        return self.open.contains(item)
