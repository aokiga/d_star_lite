from src.closed_base import ClosedBase
from src.node import Node


class ClosedDStar(ClosedBase):
    def __init__(self):
        super().__init__()
        self.elements = dict()

    def __iter__(self):
        return iter(self.elements)

    def __len__(self):
        return len(self.elements)

    def add_node(self, item: Node):
        if (item.i, item.j) in self.elements:
            return
        super().add_node(item)
        self.elements[(item.i, item.j)] = item

    def in_closed(self, i, j):
        return (i, j) in self.elements

    def remove(self, i, j):
        self.elements.pop((i, j))
