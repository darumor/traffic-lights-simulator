from arc import Arc
from node import Node


class Graph:
    def __init__(self, graph_data={}):
        self.name = graph_data["name"]
        self.nodes = {}
        self.init_nodes(graph_data["nodes"])
        self.arcs = {}
        self.init_arcs(graph_data["arcs"])
        self.entries = []
        self.init_entries(graph_data["entries"])
        self.exits = []
        self.init_exits(graph_data["exits"])

#        print self

    def init_nodes(self, nodes_data):
        nodes = {}
        for node in nodes_data:
            nodes[node["id"]] = Node(node, self)
        self.nodes = self.clean_duplicates_dict(nodes)

    def init_arcs(self, arcs_data):
        arcs = {}
        for arc in arcs_data:
            arcs[arc["id"]] = Arc(arc, self)
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


