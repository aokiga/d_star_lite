from src.node import Node


class ClosedBase:
    def __init__(self):
        self.nodes_added = 0

    def __iter__(self):
        return iter([])

    def __len__(self):
        return 0

    def add_node(self, item: Node):
        self.nodes_added += 1

    def was_expanded(self, item: Node):
        return False
