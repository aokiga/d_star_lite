from node import Node


class OpenBase:
    def __init__(self):
        pass

    def __iter__(self):
        return iter([])

    def __len__(self):
        return 0

    def is_empty(self):
        return True

    def add_node(self, item: Node):
        return

    def get_best_node(self):
        return None
