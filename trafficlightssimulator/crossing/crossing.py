class Crossing:
    def __init__(self, graph, classifier):
        self.graph = graph
        self.classifier = classifier

    def handle_batch(self, batch):
        print "crossing-handle_batch"
