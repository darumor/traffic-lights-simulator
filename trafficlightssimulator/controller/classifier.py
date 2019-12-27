class Classifier:
    def __init__(self, ticker):
        self.throughput = 0                                     # maximize
        self.individual_waiting_times = {}                      # minimize
        self.light_change_time = 0                              # minimize
        self.route_waiting_times = {}                           # minimize

        self.total_waiting_time = 0                             # minimize
        self.average_waiting_time = 0                           # minimize
        self.mean_square_error_in_waiting_times = 0             # minimize

        ticker.register_entity(self)

    # --------------- API ----------------
    def add_to_throughput(self, number=1):
        self.throughput = self.throughput + number

    def add_to_individual_waiting_time(self, individual_id, time=0):
        if not self.individual_waiting_times[individual_id]:
            self.individual_waiting_times[individual_id] = 0
        self.individual_waiting_times[individual_id] = self.individual_waiting_times[individual_id] + time

    def add_to_light_change_time(self, time=0):
        self.light_change_time = self.light_change_time + time

    def reset_route_waiting_time(self, route_id):
        self.route_waiting_times[route_id] = 0

    def report(self):
        print "classifier-report"

    def tick(self, world=None):
        for route_id, time in self.route_waiting_times:
            self.route_waiting_times[route_id] = time + 1

    # ---------------- INTERNAL --------------

    def calculate_time_values(self):
        self.total_waiting_time = 0
        for individual_id, time in self.individual_waiting_times:
            self.total_waiting_time = self.total_waiting_time + time
        self.average_waiting_time = self.total_waiting_time / self.individual_waiting_times.__len__()

        total_squares = 0
        for individual_id, time in self.individual_waiting_times:
            total_squares = total_squares + pow(self.average_waiting_time - time, 2)

        self.mean_square_error_in_waiting_times = total_squares / self.individual_waiting_times.__len__()

    def analyze(self):
        self.calculate_time_values()


