from src.A_star.closed_a_star import ClosedAStar
from src.closed_base import ClosedBase
from src.node import Node


class ClosedLRTA(ClosedBase):
    def __init__(self):
        super().__init__()
        self.closed = ClosedAStar()

    def reset(self):
        self.nodes_added += self.closed.nodes_added
        self.closed = ClosedAStar()

    def __iter__(self):
        return self.closed.__iter__()

    def __len__(self):
        return self.closed.__len__()

    def add_node(self, item: Node):
        self.closed.add_node(item)

    def was_expanded(self, item: Node):
        return self.closed.was_expanded(item)
