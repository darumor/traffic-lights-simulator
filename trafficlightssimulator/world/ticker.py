# ticker ticks every 1/rate seconds, default 1/1000 s, and provides time for the world
import time
import threading


class Ticker(threading.Thread):

    def __init__(self, rate=1000, max_ticks=5000, world=None):
        threading.Thread.__init__(self)
        self.rate = rate
        self.max_ticks = max_ticks
        self.current_tick = 0
        self.entities = []
        self.running = False
        self.world = world

    def register_entity(self, entity):
        if "tick" in dir(entity):
            print entity
            self.entities.append(entity)

    def run(self):
        self.running = True
        while self.running and self.current_tick < self.max_ticks:
            self.current_tick = self.current_tick + 1
            print "ticker - tick %d" % self.current_tick
            for entity in self.entities:
                entity.tick(self.world)
            time.sleep(1 / self.rate)

    def run_some(self, some_ticks):
        self.running = True
        local_ticks = 0
        while self.running and self.current_tick < self.max_ticks:
            self.current_tick = self.current_tick + 1
            print "ticker - tick %d" % self.current_tick
            for entity in self.entities:
                entity.tick(self.world)
            time.sleep(1 / self.rate)
            local_ticks = local_ticks + 1
            if local_ticks >= some_ticks:
                self.running = False

    def stop(self):
        self.running = False
