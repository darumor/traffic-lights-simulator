import crossing
crossing_data_json_file_name = 'crossing/data/t-crossing.json'

graph = crossing.graph.Graph(crossing_data_json_file_name)
path_finder = crossing.pathfinder.PathFinder(graph)
path_finder.print_path("node-west-in", "node-south-out")

