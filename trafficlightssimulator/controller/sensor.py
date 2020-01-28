
class Sensor:

    def __init__(self, node):
        self.node = node

    def get_signal(self):
        return self.node.signal

    def reset_signal(self):
        self.node.signal = 0
