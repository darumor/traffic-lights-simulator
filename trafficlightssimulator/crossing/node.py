class Node:
    def __init__(self, node_data, graph):
        self.id = node_data["id"]
        self.type = 'Node'
        self.entries = []  # arcs
        self.exits = []  # arcs
        self.is_entry = False
        self.is_exit = False
        self.signal = 0
        self.graph = graph

    def __str__(self):
        string = self.id + ' '
        if self.is_entry:
            string += '(entry) '
        if self.is_exit:
            string += '(exit) '
        string += 'Entries: ' + map(lambda e: e.id, self.entries).__str__()
        string += ' Exits: ' + map(lambda e: e.id, self.exits).__str__()
        return string
