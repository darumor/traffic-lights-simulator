from trafficlightssimulator.crossing.pathfinder import PathFinder


class Controller:
    def __init__(self, graph, ticker):
        self.graph = graph
        self.routes = self.register_routes()
        self.sensors = self.register_sensors()
        self.lights = self.register_lights()
        ticker.register_entity(self)

    def register_routes(self):
        print "register routes"
        routes = []
        pathfinder = PathFinder(self.graph)
        for entry_node in self.graph.entries:
            for exit_node in self.graph.exits:
                route_id = entry_node.id + '_' + exit_node.id
                try:
                    routes.append({'route_id': route_id,
                                   'path': pathfinder.find_path(entry_node.id, exit_node.id)})
                except Exception as e:
                    print str(e.message) + ": route_id = " + route_id
        return routes

    def register_sensors(self):
        print "register sensors"
        return []

    def register_lights(self):
        print "register lights"
        return []

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
