# read lights, move cars and send signals
class Crossing:
    def __init__(self, ticker, graph, classifier):
        self.ticker = ticker
        self.graph = graph
        self.classifier = classifier
        self.cars = []
        self.car_locations = {}
        ticker.register_entity(self)

    def handle_batch(self, batch):
        print "crossing - handle_batch"
        for car in batch:
            self.cars.append(car)

    def tick(self, world=None):
        print "crossing - tick"
        for car in self.cars:
            car.update_location()



