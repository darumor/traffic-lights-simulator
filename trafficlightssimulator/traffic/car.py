class Car:
    def __init__(self, car_id, timestamp, entry_node, exit_node, path, speed=0.1):
        self.car_id = car_id
        self.timestamp = timestamp
        self.entry_node = entry_node
        self.exit_node = exit_node
        self.current_arc = None
        self.path = path
        self.speed = speed      # distance / tick
        self.location = self.Location(node=self.entry_node)

    def __str__(self):
        return self.car_id

    def update_location(self, distance=None):
        print "car - update_location"
        local_distance = distance
        if local_distance is None:
            local_distance = self.speed

        if self.location.node is not None:
            if self.location.node == self.exit_node:
                print "should do something when exiting"

            next_path_item = self.path.next_item_by_item_id(self.location.node.id)
            if next_path_item is not None and next_path_item.open:      # after a node there is always an arc, if not an exit node
                if local_distance < next_path_item.length:
                    self.location = self.Location(None, next_path_item, local_distance)
                else:
                    self.location = self.Location(None, next_path_item, next_path_item.length)  # no arc should ever be this short
                    local_distance = local_distance - next_path_item.length
        elif self.location.arc is not None:
            if local_distance < self.location.arc.length - self.location.distance:
                self.location.distance = self.location.distance + local_distance
            else:
                next_path_item = self.path.next_item_by_item_id(self.location.arc.id)    # after an arc there is always a node
                self.location = self.Location(next_path_item, None, 0)
                local_distance = local_distance - (self.location.arc.length - self.location.distance)

        if local_distance > 0:
            self.update_location(local_distance)

    class Location:

        def __init__(self, node=None, arc=None, distance=0):
            self.node = node
            self.arc = arc
            self.distance = distance
            assert (node is None) != (arc is None)
