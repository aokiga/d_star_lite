from src.node import Node


class OpenBase:
    def __init__(self):
        self.nodes_added = 0
        pass

    def __iter__(self):
        return iter([])

    def __len__(self):
        return 0

    def is_empty(self):
        return True

    def add_node(self, item: Node):
        self.nodes_added += 1
        return

    def get_best_node(self):
        return None
