import unittest
import json

from trafficlightssimulator.crossing.graph import Graph
from trafficlightssimulator.crossing.pathfinder import PathFinder


class TestUnitPathFinder(unittest.TestCase):

    def test_trivial_path(self):
        trivial_crossing_filename = 'tests/crossing/data/trivial-crossing.json'
        with open(trivial_crossing_filename, 'r') as f:
            graph_data = json.load(f)
        graph = Graph(graph_data)
        path_finder = PathFinder(graph)
        path_finder.print_path("node-west-in", "node-south-out")

        assert map(lambda p: p.id, path_finder.find_path("node-west-in", "node-south-out").path_items) == \
            ["node-west-in", "arc-2", "node-south-merge", "arc-3", "node-south-out"]
