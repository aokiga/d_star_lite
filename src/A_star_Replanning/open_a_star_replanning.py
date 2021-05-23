from src.a_star.open_a_star import OpenAStar
from src.node import Node
from src.open_base import OpenBase


class OpenAStarReplanning(OpenBase):
    def __init__(self):
        super().__init__()
        self.open = OpenAStar()

    def reset(self):
        self.open = OpenAStar()

    def __iter__(self):
        return self.open.__iter__()

    def __len__(self):
        return self.open.__len__()

    def is_empty(self):
        return self.open.is_empty()

    def add_node(self, item: Node):
        self.open.add_node(item)

    def get_best_node(self):
        return self.open.get_best_node()