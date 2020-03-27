from math import sqrt
import numpy as np


class Calculator:

    def __init__(self, sensors=None, lights=None, coefficients=None):
        self.sensors = sensors
        if self.sensors is None:
            self.sensors = []
        self.lights = lights
        if self.lights is None:
            self.lights = []

        if coefficients is None:
            self.coefficients = self.calculate_default_coefficients()
        else:
            self.coefficients = np.array(coefficients)

    def which_light_should_be_green(self):
        comparatives = self.calculate_comparatives()
        return self.lights[np.argmax(comparatives)]

    def calculate_comparatives(self):
        variables = self.collect_variables(self.sensors, self.lights)
        return np.matmul(self.coefficients, variables)

    def calculate_default_coefficients(self):
        variables = self.collect_variables(self.sensors, self.lights)
        return np.ones((len(self.lights), len(variables)))

    @staticmethod
    def collect_variables(sensors, lights):
        all_values = []
        for sensor in sensors:
            all_values.append(sensor.get_signal())
        for light in lights:
            all_values.append(light.timer)
        all_variables = []
        for value in all_values:
            all_variables.append(value)
            all_variables.append(value * value)
            all_variables.append(sqrt(value))
        return np.array(all_variables)
