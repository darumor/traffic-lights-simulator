class Stream:
    def __init__(self, crossing, generator, ticker):
        self.crossing = crossing
        self.generator = generator
        ticker.register_entity(self)

    def tick(self, world=None):
        print "stream-tick"
        self.crossing.handle_batch(
            self.generator.get_next_batch(time_interval=1)
        )
