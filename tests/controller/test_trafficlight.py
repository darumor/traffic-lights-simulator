import unittest
from trafficlightssimulator.controller import trafficlight
from trafficlightssimulator.world.ticker import Ticker

class TestUnitTrafficLight(unittest.TestCase):

    def test_states(self):
        ticker = Ticker(max_ticks=100)
        arc = self.TrivialArc()
        traffic_light = trafficlight.TrafficLight(ticker, arc, [],  2, 3)
        assert traffic_light.states == [0, 1, 1, 2, 3, 3, 3]
        assert traffic_light.get_state() == trafficlight.RED
        assert not arc.open
        assert not arc.blocked
        ticker.run_some(15)
        assert traffic_light.get_state() == trafficlight.RED
        assert not arc.open
        traffic_light.turn_to_green()
        ticker.run_some(2)
        assert traffic_light.get_state() == trafficlight.YELLOW_TURNING_GREEN
        assert not arc.open
        ticker.run_some(15)
        assert traffic_light.get_state() == trafficlight.GREEN
        assert arc.open
        traffic_light.turn_to_red()
        ticker.run_some(2)
        assert traffic_light.get_state() == trafficlight.YELLOW_TURNING_RED
        assert not arc.open
        ticker.run_some(15)
        assert traffic_light.get_state() == trafficlight.RED
        assert not arc.open

    def test_blocking(self):
        ticker = Ticker(max_ticks=100)
        arc1 = self.TrivialArc()
        arc2 = self.TrivialArc()
        traffic_light1 = trafficlight.TrafficLight(ticker, arc1, [arc2], 2, 3)
        traffic_light2 = trafficlight.TrafficLight(ticker, arc2, [arc1], 2, 3)
        assert traffic_light1.states == [0, 1, 1, 2, 3, 3, 3]
        assert traffic_light1.get_state() == trafficlight.RED
        assert not arc1.open
        assert not arc1.blocked
        assert not arc2.open
        assert not arc2.blocked

        ticker.run_some(15)
        assert traffic_light1.get_state() == trafficlight.RED
        assert not arc1.open
        assert not arc1.blocked
        assert not arc2.open
        assert not arc2.blocked

        traffic_light1.turn_to_green()
        ticker.run_some(2)
        assert traffic_light1.get_state() == trafficlight.YELLOW_TURNING_GREEN
        assert traffic_light2.get_state() == trafficlight.RED
        assert not arc1.open
        assert not arc1.blocked
        assert not arc2.open
        assert arc2.blocked

        ticker.run_some(15)
        assert traffic_light1.get_state() == trafficlight.GREEN
        assert traffic_light2.get_state() == trafficlight.RED
        assert arc1.open
        assert not arc1.blocked
        assert not arc2.open
        assert arc2.blocked

        traffic_light1.turn_to_red()
        ticker.run_some(2)
        assert traffic_light1.get_state() == trafficlight.YELLOW_TURNING_RED
        assert traffic_light2.get_state() == trafficlight.RED
        assert not arc1.open
        assert not arc1.blocked
        assert not arc2.open
        assert arc2.blocked

        ticker.run_some(15)
        assert traffic_light1.get_state() == trafficlight.RED
        assert traffic_light2.get_state() == trafficlight.RED
        assert not arc1.open
        assert not arc1.blocked
        assert not arc2.open
        assert not arc2.blocked

    class TrivialArc:
        def __init__(self):
            self.open = True
            self.blocked = False
