class Car:
    def __init__(self, car_id, timestamp, entry_node, exit_node):
        self.car_id = car_id
        self.timestamp = timestamp
        self.entry = entry_node
        self.exit = exit_node

    def find_path(self):
        print self.car_id

    def __str__(self):
        return self.car_id
