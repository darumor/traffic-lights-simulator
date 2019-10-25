import crossing

crossing_data_json_file_name = 'crossing/data/t-crossing.json'

network = crossing.network.Network(crossing_data_json_file_name)
path_finder = crossing.pathfinder.PathFinder(network)
path_finder.print_path("node-west-in", "node-south-out")

