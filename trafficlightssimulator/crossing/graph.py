import json


class Graph:
    def __init__(self, json_file):
        with open(json_file, 'r') as f:
            data = json.load(f)

        self.name = data["name"]
        self.nodes = {}
        self.init_nodes(data["nodes"])
        self.arcs = {}
        self.init_arcs(data["arcs"])
        self.entries = []
        self.init_entries(data["entries"])
        self.exits = []
        self.init_exits(data["exits"])

#        print self

    def init_nodes(self, nodes_data):
        nodes = {}
        for node in nodes_data:
            nodes[node["id"]] = Graph.Node(node, self)
        self.nodes = self.clean_duplicates_dict(nodes)

    def init_arcs(self, arcs_data):
        arcs = {}
        for arc in arcs_data:
            arcs[arc["id"]] = Graph.Arc(arc, self)
        for arc in arcs_data:
            for blocked_arc in arc["blocks"]:
                arcs[arc["id"]].blocks.append(arcs[blocked_arc])
        self.arcs = self.clean_duplicates_dict(arcs)

    def init_entries(self, entries_data):
        entries = []
        for entry_node in entries_data:
            entries.append(self.nodes[entry_node["id"]])
            self.nodes[entry_node["id"]].is_entry = True
        self.entries = self.clean_duplicates_list(entries)

    def init_exits(self, exits_data):
        exits = []
        for exit_node in exits_data:
            exits.append(self.nodes[exit_node["id"]])
            self.nodes[exit_node["id"]].is_exit = True
        self.exits = self.clean_duplicates_list(exits)

    def __str__(self):
        string = self.name
        string += '\nNODES:'
        for k, node in self.nodes.items():
            string += '\n ' + node.__str__()
        string += '\nARCS:'
        for k, arc in self.arcs.items():
            string += '\n ' + arc.__str__()
        return string

    @staticmethod
    def clean_duplicates_list(input_list):
        output_list = []
        for item in input_list:
            if item not in output_list:
                output_list.append(item)
        return output_list

    @staticmethod
    def clean_duplicates_dict(input_dict):
        output_dict = {}
        for key, value in input_dict.items():
            output_dict[key] = value
        return output_dict

    class Node:
        def __init__(self, node_data, graph):
            self.id = node_data["id"]
            self.type = 'Node'
            self.entries = []                                    # arcs
            self.exits = []                                      # arcs
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

    class Arc:
        def __init__(self, arc_data, network):
            self.id = arc_data["id"]
            self.type = 'Arc'
            self.start = network.nodes[arc_data["start"]]          # node
            self.end = network.nodes[arc_data["end"]]              # node
            self.length = int(arc_data["length"])
            self.blocks = []                                       # arcs
            self.open = True                                       # semaphore
            self.blocked = False                                   # semaphore
            network.nodes[self.start.id].exits.append(self)
            network.nodes[self.end.id].entries.append(self)

        def __str__(self):
            string = self.id
            string += ' Start: ' + self.start.id
            string += ' End: ' + self.end.id
            string += ' Length: ' + str(self.length)
            string += ' Blocks: ' + map(lambda b: b.id, self.blocks).__str__()
            return string
