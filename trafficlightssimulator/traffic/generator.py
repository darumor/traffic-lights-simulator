import random
from car import Car


class Generator:
    def __init__(self, graph):
        self.graph = graph
        self.timestamp = 0
        self.pointer = 0
        self.default_params = {
            'min_interval': 1,
            'max_interval': 10,
            'number_of_cars': 50
        }
        self.traffic = self.generate_traffic()

    def generate_traffic(self, filename=None):
        traffic = []
        if filename:
            raise NotImplemented('Generating traffic based on a file is not implemented yet')
        else:
            generated_cars = 0
            local_timestamp = 0
            while generated_cars < self.default_params['number_of_cars']:
                for entry_node in self.graph.entries:
                    for exit_node in self.graph.exits:
                        interval = self.random_interval()
                        local_timestamp = local_timestamp + interval
                        car_id = entry_node.id + '_' + exit_node.id + '_' + str(local_timestamp)
                        car = Car(car_id, local_timestamp, entry_node, exit_node)
                        traffic.append(car)
                        generated_cars = generated_cars + 1
                        print "generator - added car %s" % car
        return traffic

    def random_interval(self):
        start = self.default_params['min_interval'] * 10
        stop = self.default_params['max_interval'] * 10
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
