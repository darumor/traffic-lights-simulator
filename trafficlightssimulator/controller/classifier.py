class Classifier:
    def __init__(self, ticker):
        self.throughput = 0                                     # maximize
        self.individual_waiting_times = {}                      # minimize
        self.light_change_time = 0                              # minimize
        self.route_waiting_times = {}                           # minimize

        self.total_waiting_time = 0                             # minimize
        self.average_waiting_time = 0                           # minimize
        self.mean_square_error_in_waiting_times = 0             # minimize
        self.max_route_waiting_time = 0                         # minimize

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
        self.analyze()
        print """
-------- classifier-report --------
  Throughput: %d
  Total waiting time: %d
  Average waiting time: %d
  Error in waiting times: %d
  Light changing time: %d
  Max route waiting time: %d
-----------------------------------""" % (self.throughput,
                                             self.total_waiting_time,
                                             self.average_waiting_time,
                                             self.mean_square_error_in_waiting_times,
                                             self.light_change_time,
                                             self. max_route_waiting_time)

    def tick(self, world=None):
        print "classifier: tick"
        for route_id, time in self.route_waiting_times:
            new_time = time + 1
            if new_time > self.max_route_waiting_time:
                self.max_route_waiting_time = new_time
            self.route_waiting_times[route_id] = new_time

    # ---------------- INTERNAL --------------

    def calculate_time_values(self):
        if self.individual_waiting_times.__len__() > 0:
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


