class TrivialTickee:

    def __init__(self):
        self.value = 0

    def tick(self, world=None):
        self.value = self.value + 1
