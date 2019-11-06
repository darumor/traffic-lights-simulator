import unittest

from crossing.graph import Graph
from crossing.pathfinder import PathFinder


class TestUnitPathFinder(unittest.TestCase):

    def test_trivial_path(self):
        crossing_data_json_file_name = 'data/trivial-crossing.json'

        graph = Graph(crossing_data_json_file_name)
        path_finder = PathFinder(graph)
        path_finder.print_path("node-west-in", "node-south-out")

        assert map(lambda p: p.id, path_finder.find_path("node-west-in", "node-south-out").path_items) == \
               ["node-west-in", "arc-2", "node-south-merge", "arc-3", "node-south-out"]

