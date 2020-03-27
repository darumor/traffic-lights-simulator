RED = 0
YELLOW_TURNING_GREEN = 1
GREEN = 2
YELLOW_TURNING_RED = 3


class TrafficLight:

    def __init__(self, ticker, arc,
                 blockable_arcs=None,
                 time_from_yellow_to_green=100,
                 time_from_yellow_to_red=300,
                 minimum_green_time=500):
        if blockable_arcs is None:
            blockable_arcs = []
        self.arc = arc
        self.id = "light-%s" % arc.id
        self.arc.open = False
        self.blockable_arcs = blockable_arcs
        self.blocked_arcs = []
        self.states = [RED]
        for i in range(0, time_from_yellow_to_green):
            self.states.append(YELLOW_TURNING_GREEN)
        for i in range(0, minimum_green_time):
            self.states.append(GREEN)
        for i in range(0, time_from_yellow_to_red):
            self.states.append(YELLOW_TURNING_RED)
        ticker.register_entity(self)
        self.state_pointer = 0
        self.target_state = RED
        self.timer = 0

    def get_state(self):
        return self.states[self.state_pointer]

    def turn_to_green(self):
        print "turning GREEN (%d)" % GREEN
        self.target_state = GREEN

    def turn_to_red(self):
        print "turning RED (%d)" % RED
        self.target_state = RED

    def resolve_state(self):
        if (self.get_state() != RED or not self.arc.is_blocked()) and \
                (self.get_state() == self.next_state() or self.get_state() != self.target_state):
            self.increase_state_pointer()

        if self.get_state() == GREEN:
            self.block_blockable_arcs()
            self.arc.open = True
            self.timer = 0
        elif self.get_state() == YELLOW_TURNING_RED:
            self.block_blockable_arcs()
            self.arc.open = False
        elif self.get_state() == RED:
            self.release_blocked_arcs()
        elif self.get_state() == YELLOW_TURNING_GREEN:
            self.block_blockable_arcs()

    def block_blockable_arcs(self):
        for blockable in self.blockable_arcs:
            blockable.block(self)
            self.blocked_arcs.append(blockable)

    def release_blocked_arcs(self):
        for blocked in self.blocked_arcs:
            blocked.unblock(self)
            self.blocked_arcs.remove(blocked)

    def increase_state_pointer(self):
        self.state_pointer = self.next_pointer()
        print "new state: %d" % self.get_state()

    def next_state(self):
        temp_pointer = self.next_pointer()
        return self.states[temp_pointer]

    def next_pointer(self):
        return (self.state_pointer + 1) % self.states.__len__()

    def tick(self, world=None):
        self.timer = self.timer + 1
        self.resolve_state()

