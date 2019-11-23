# ticker ticks every 1/rate seconds, default 1/1000 s, and provides time for the world

import time


class Ticker:

    def __init__(self, rate=1000, ticks=5000, world=None):
        self.rate = rate
        self.max_ticks = ticks
        self.current_tick = 0
        self.entities = []
        self.running = False
        self.world = world

    def register_entity(self, entity):
        if "tick" in dir(entity):
            self.entities.append(entity)

    def run(self):
        self.running = True
        while self.running and self.current_tick < self.max_ticks:
            self.current_tick = self.current_tick + 1
            for entity in self.entities:
                entity.tick(self.world)
            time.sleep(1 / self.rate)

    def stop(self):
        self.running = False
