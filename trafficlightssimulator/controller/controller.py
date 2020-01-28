
from trafficlightssimulator.controller import trafficlight
from trafficlightssimulator.controller import sensor


class Controller:
    def __init__(self, graph, ticker, time_to_green=100, time_to_red=300):
        self.graph = graph
        self.routes = self.register_routes()
        self.sensors = self.register_sensors()
        self.lights = self.register_lights(ticker, time_to_green, time_to_red)
        ticker.register_entity(self)



    def register_sensors(self):
        print "register sensors"
        sensors = []
        for node in self.graph.nodes:
            if not node.is_entry and not node.is_exit and len(node.entries) > 0:
                sensors.append(sensor.Sensor(node))
        return sensors

    def register_lights(self, ticker, time_to_green=100, time_to_red=300):
        print "register lights"
        lights = []
        for node in self.graph.nodes:
            if not node.is_entry and not node.is_exit and len(node.entries) > 0 and len(node.exits) > 0:
                for exit_arc in node.exits:
                    lights.append(
                        trafficlight.TrafficLight(ticker, time_to_green, time_to_red, exit_arc, exit_arc.blocks))
        return lights

    def tick(self, world=None):
        print "controller-tick"
        self.read_values()
        self.define_state()
        self.set_lights()

    def read_values(self):
        print " - read values"

    def define_state(self):
        print " - define state"

    def set_lights(self):
        print " - set lights"

    def change_light(self, light, start, end):
        light.change(start, end)
