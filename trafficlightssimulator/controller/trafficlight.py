RED = 0
YELLOW_TURNING_GREEN = 1
GREEN = 2
YELLOW_TURNING_RED = 3


class TrafficLight:

    def __init__(self, ticker, arc, blocked_arcs=None, time_from_yellow_to_green=100, time_from_yellow_to_red=300):
        if blocked_arcs is None:
            blocked_arcs = []
        self.arc = arc
        self.arc.open = False
        self.blocked_arcs = blocked_arcs
        self.states = [RED]
        for i in range(0, time_from_yellow_to_green):
            self.states.append(YELLOW_TURNING_GREEN)
        self.states.append(GREEN)
        for i in range(0, time_from_yellow_to_red):
            self.states.append(YELLOW_TURNING_RED)
        ticker.register_entity(self)
        self.state_pointer = 0
        self.target = RED

    def get_state(self):
        return self.states[self.state_pointer]

    def turn_to_green(self):
        print "turning GREEN (%d)" % GREEN
        self.target = GREEN

    def turn_to_red(self):
        print "turning RED (%d)" % RED
        self.target = RED

    def next_state(self):
        if self.get_state() != RED or not self.arc.blocked:
            self.state_pointer = (self.state_pointer + 1) % self.states.__len__()
        print "new state: %d" % self.get_state()

        if self.get_state() == GREEN:
            self.arc.open = True
        elif self.get_state() == YELLOW_TURNING_RED:
            self.arc.open = False
        elif self.get_state() == RED:
            for blocked in self.blocked_arcs:
                blocked.blocked = False
        elif self.get_state() == YELLOW_TURNING_GREEN:
            for blocked in self.blocked_arcs:
                blocked.blocked = True

    def tick(self, world=None):
        if self.get_state() != self.target:
            self.next_state()

