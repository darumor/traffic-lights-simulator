class PathFinder:

    def __init__(self, network):
        self.network = network

    def print_path(self, entry_node_id, exit_node_id):
        print self.find_path(entry_node_id, exit_node_id)

    def find_path(self, entry_node_id, exit_node_id):
        path = PathFinder.Path()
        path.append(self.network.nodes[entry_node_id])

        # todo tähän varsinainen etsintäalgoritmi



        path.append(self.network.nodes[exit_node_id])
        return path

    class Path:
        def __init__(self):
            self.path_items = []

        def __str__(self):
            return map(lambda i: i.id, self.path_items).__str__()

        def append(self, path_item):
            self.path_items.append(path_item)

    class PathItem:
        def __init__(self, item):
            self.id = item.id
            self.type = item.type

        def __str__(self):
            return '{self.type}:{self.id}'.format(self=self)
