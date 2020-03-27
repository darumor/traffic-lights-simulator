import trafficlight
import sensor
from calculator import Calculator


class Controller:
    def __init__(self, graph, ticker, time_to_green=100, time_to_red=300, minimum_green_time=500, coefficients=None):
        self.graph = graph
        self.sensors = self.register_sensors()
        self.lights = self.register_lights(ticker, time_to_green, time_to_red, minimum_green_time)
        ticker.register_entity(self)
        self.calculator = Calculator(self.sensors, self.lights, coefficients)

    # every node of the graph may be a sensor
    def register_sensors(self):
        print "register sensors"
        sensors = []
        for node in self.graph.nodes:
            if not node.is_entry and not node.is_exit and len(node.entries) > 0:
                sensors.append(sensor.Sensor(node))
        return sensors

    # every inner node may be a light
    def register_lights(self, ticker, time_to_green=100, time_to_red=300, minimum_green_time=500):
        print "register lights"
        lights = []
        for node in self.graph.nodes:
            if not node.is_entry and not node.is_exit and len(node.entries) > 0 and len(node.exits) > 0:
                for exit_arc in node.exits:
                    lights.append(
                        trafficlight.TrafficLight(ticker, exit_arc, exit_arc.blocks, time_to_green, time_to_red, minimum_green_time))
        return lights

    def tick(self, world=None):
        print "controller-tick"
        self.read_input_and_define_state()
        self.set_lights()

    def read_input_and_define_state(self):
        print " - read values - values from sensors"
        print " - calculate - all variables from sensors"
        print " - define state - calculate variables for each light"
        print " - define state - calculate priorities (coefficients * variables)"

    def set_lights(self):
        print " - set lights according to priorities"

