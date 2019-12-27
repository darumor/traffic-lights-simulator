from simulator import TrafficLightsSimulator

params = {
    'crossing_data_json_file_name': 'crossing/data/t-crossing.json',
    'tick_rate': 1000,
    'ticks': 1000
}

simulator = TrafficLightsSimulator(params)
simulator.start()

