from src.closed_base import ClosedBase
from src.node import Node


class ClosedAStar(ClosedBase):
    def __init__(self):
        super().__init__()
        self.elements = set()

    def __iter__(self):
        return iter(self.elements)

    def __len__(self):
        return len(self.elements)

    def add_node(self, item: Node):
        if item in self.elements:
            return
        super().add_node(item)
        self.elements.add(item)

    def was_expanded(self, item: Node):
        return item in self.elements

    def remove(self, item: Node):
        self.elements.remove(item)
