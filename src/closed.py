from src.node import Node


class Closed:
    def __init__(self):
        self.elements = set()

    def __iter__(self):
        return iter(self.elements)

    def __len__(self):
        return len(self.elements)

    def add_node(self, item: Node):
        if item in self.elements:
            return
        self.elements.add(item)

    def was_expanded(self, item: Node):
        return item in self.elements
