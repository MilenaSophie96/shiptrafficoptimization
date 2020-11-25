class Node:
    position = -100
    name = None
    active_labels = []
    all_labels = []

    def __init__(self, p, name):
        self.position = p
        self.name = name
