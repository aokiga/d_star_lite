from src.node import Node


class ClosedBase:
    def __init__(self):
        pass

    def __iter__(self):
        return iter([])

    def __len__(self):
        return 0

    def add_node(self, item: Node):
        return

    def was_expanded(self, item: Node):
        return False
