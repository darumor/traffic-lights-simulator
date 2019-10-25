class Car:
    def __init__(self, id, entry_node, exit_node):
        self.id = id
        self.entry = entry_node
        self.exit = exit_node

    def find_path(self):
        print self.id
