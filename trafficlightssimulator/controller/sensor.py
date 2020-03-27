
class Sensor:

    def __init__(self, node):
        self.node = node

    def get_signal(self):
        return self.node.signal

    def reset_signal(self):
        self.node.signal = 0

    def set_signal(self, value):
        self.node.signal = value

    def up_signal(self):
        self.node.signal = self.node.signal + 1

    def down_signal(self):
        self.node.signal = self.node.signal - 1
