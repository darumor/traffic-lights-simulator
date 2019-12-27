from crossing import Graph, Crossing
from controller import Controller, Classifier
from world import Ticker
from traffic import Stream, Generator


class TrafficLightsSimulator:
    def __init__(self, params):
        self.crossing_data_json_file_name = params['crossing_data_json_file_name']
        self.ticker = Ticker(params['tick_rate'], params['ticks'])

        self.graph = Graph(self.crossing_data_json_file_name)
        self.classifier = Classifier(self.ticker)
        self.crossing = Crossing(self.graph, self.classifier)
        self.generator = Generator(self.graph)
        self.stream = Stream(self.crossing, self.generator, self.ticker)
        self.controller = Controller(self.graph, self.ticker)

    def start(self):
        self.ticker.run()
