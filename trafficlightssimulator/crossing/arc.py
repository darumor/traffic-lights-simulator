class Arc:
    def __init__(self, arc_data, network):
        self.id = arc_data["id"]
        self.type = 'Arc'
        self.start = network.nodes[arc_data["start"]]  # node
        self.end = network.nodes[arc_data["end"]]  # node
        self.length = int(arc_data["length"])
        self.blocks = []  # arcs
        self.open = True  # semaphore
        self.blocking_arcs = set([])  # semaphore
        network.nodes[self.start.id].exits.append(self)
        network.nodes[self.end.id].entries.append(self)

    def __str__(self):
        string = self.id
        string += ' Start: ' + self.start.id
        string += ' End: ' + self.end.id
        string += ' Length: ' + str(self.length)
        string += ' Blocks: ' + map(lambda b: b.id, self.blocks).__str__()
        return string

    def is_blocked(self):
        return self.blocking_arcs.__len__() > 0

    def block(self, arc):
        self.blocking_arcs.add(arc)

    def unblock(self, arc):
        self.blocking_arcs.discard(arc)
