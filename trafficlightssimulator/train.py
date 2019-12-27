from crossing import Graph
from controller import Controller
from world import Ticker

crossing_data_json_file_name = 'crossing/data/t-crossing.json'

graph = Graph(crossing_data_json_file_name)
controller = Controller(graph)

ticker = Ticker()
ticker.register_entity(controller)

## todo this is only a reminder that some method of training a model should be implemented