import random
from car import Car
from trafficlightssimulator.crossing.pathfinder import PathFinder


class Generator:
    def __init__(self, graph, params=None):
        self.graph = graph
        self.timestamp = 0
        self.pointer = 0
        self.paths = self.register_paths()
        self.default_params = {
            'min_interval': 1,
            'max_interval': 10,
            'number_of_cars': 50,
            'car_speed': 0.1,
            'car_speed_variation': 2
        }
        if params is None:
            params = self.default_params
        self.traffic = self.generate_traffic(params=params)

    def register_paths(self):
        print "register paths"
        paths = {}
        pathfinder = PathFinder(self.graph)
        for entry_node in self.graph.entries:
            for exit_node in self.graph.exits:
                path_id = entry_node.id + '_' + exit_node.id
                try:
                    paths[path_id] = pathfinder.find_path(entry_node.id, exit_node.id)
                except Exception as e:
                    print str(e.message) + ": paths_id = " + path_id
        return paths

    def generate_traffic(self, filename=None, params=None):
        traffic = []
        if params is None:
            params = self.default_params
        if filename:
            raise NotImplemented('Generating traffic based on a file is not implemented yet')
        else:
            generated_cars = 0
            local_timestamp = 0
            while generated_cars < params['number_of_cars']:
                for entry_node in self.graph.entries:
                    for exit_node in self.graph.exits:
                        interval = self.random_interval(params)
                        local_timestamp = local_timestamp + interval
                        car_id = entry_node.id + '_' + exit_node.id + '_' + str(local_timestamp)
                        path_id = entry_node.id + '_' + exit_node.id
                        car = Car(car_id, local_timestamp, entry_node, exit_node, self.paths[path_id], self.random_speed(params))
                        traffic.append(car)
                        generated_cars = generated_cars + 1
                        print "generator - added car %s" % car
        return traffic

    @staticmethod
    def random_speed(params):
        return random.randrange(params['car_speed'] - params['car_speed_variation'],
                                params['car_speed'] + params['car_speed_variation'],
                                1)

    @staticmethod
    def random_interval(params):
        start = params['min_interval'] * 10
        stop = params['max_interval'] * 10
        return random.randrange(start, stop, 1) / 10

    def get_next_batch(self, time_interval=1):
        local_timestamp = 0
        self.timestamp = self.timestamp + time_interval
        batch = []
        while local_timestamp < self.timestamp and self.pointer < self.traffic.__len__():
            car = self.traffic.__getitem__(self.pointer)
            if car.timestamp < self.timestamp:
                batch.append(car)
                print "generator - added (%d) car %s to batch" % (self.pointer, car)
                local_timestamp = car.timestamp
                self.pointer = self.pointer + 1
            else:
                local_timestamp = self.timestamp
        return batch

    def reset_pointer(self):
        self.pointer = 0

    def has_more(self):
        return self.pointer < self.traffic.__len__()