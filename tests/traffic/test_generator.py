import unittest
import json

from trafficlightssimulator.traffic.generator import Generator
from trafficlightssimulator.crossing.graph import Graph


class TestUnitGenerator(unittest.TestCase):

    def test_simple(self):
        trivial_crossing_filename = 'tests/crossing/data/trivial-crossing.json'
        with open(trivial_crossing_filename, 'r') as f:
            graph_data = json.load(f)
        graph = Graph(graph_data)
        generator = Generator(graph, {'min_interval': 1, 'max_interval': 10, 'number_of_cars': 20, 'car_speed': 20, 'car_speed_variation': 2})
        assert generator.traffic.__len__() == 20

    def test_batch(self):
        trivial_crossing_filename = 'tests/crossing/data/trivial-crossing.json'
        with open(trivial_crossing_filename, 'r') as f:
            graph_data = json.load(f)
        graph = Graph(graph_data)
        generator = Generator(graph, {'min_interval': 1, 'max_interval': 20, 'number_of_cars': 50, 'car_speed': 20, 'car_speed_variation': 2})
        timestamp = 0
        cars = []

        while generator.has_more():
            batch = generator.get_next_batch(10)
            cars.extend(batch)
            timestamp = timestamp + 10

        assert cars.__len__() == 50
        assert generator.get_next_batch(10) == []
        assert 50 <= timestamp <= 1000

    def test_reset(self):
        trivial_crossing_filename = 'tests/crossing/data/trivial-crossing.json'
        with open(trivial_crossing_filename, 'r') as f:
            graph_data = json.load(f)
        graph = Graph(graph_data)
        generator = Generator(graph, {'min_interval': 1, 'max_interval': 20, 'number_of_cars': 20, 'car_speed': 20, 'car_speed_variation': 2})
        timestamp = 0
        cars = []

        while generator.has_more():
            batch = generator.get_next_batch(10)
            cars.extend(batch)
            timestamp = timestamp + 10

        assert generator.has_more() is False
        generator.reset_pointer()
        assert generator.has_more() is True

        while generator.has_more():
            batch = generator.get_next_batch(10)
            cars.extend(batch)
            timestamp = timestamp + 10

        assert cars.__len__() == 40
