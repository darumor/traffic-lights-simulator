import json
from crossing import Graph, Crossing
from controller import Controller, Classifier
from world import Ticker
from traffic import Stream, Generator


class TrafficLightsSimulator:
    def __init__(self, params):
        self.ticker = Ticker(params['tick_rate'], params['ticks'])
        self.crossing_data_json_file_name = params['crossing_data_json_file_name']
        with open(self.crossing_data_json_file_name, 'r') as f:
            graph_data = json.load(f)
        self.graph = Graph(graph_data)

        self.classifier = Classifier(self.ticker)
        self.crossing = Crossing(self.ticker, self.graph, self.classifier)
        self.generator = Generator(self.graph)
        self.stream = Stream(self.crossing, self.generator, self.ticker)
        self.controller = Controller(self.graph, self.ticker)

    def start(self):
        threads = [self.ticker]
        for t in threads:
            t.start()
            t.join()
        self.classifier.report()
