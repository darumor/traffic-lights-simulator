import unittest
from trivial_tickee import TrivialTickee
from trafficlightssimulator.world.ticker import Ticker


class TestUnitTicker(unittest.TestCase):

    def test_trivial_tick(self):
        tickee = TrivialTickee()
        ticker = Ticker(1000, 1000)
        ticker.register_entity(tickee)
        ticker.run()
        assert tickee.value == 1000
