import unittest
import numpy as np
from math import sqrt
from trafficlightssimulator.controller.calculator import Calculator


class TestUnitCalculator(unittest.TestCase):

    def test_trivial_calculator(self):
        sensor1 = self.TrivialSensor(1)
        sensor2 = self.TrivialSensor(2)
        light1 = self.TrivialLight('zero', 0)
        light2 = self.TrivialLight('two', 2)
        coefficients = np.array([
            [   # LIGHT1
                1, 0, 0,   # sensor1
                2, 0, 0,   # sensor2
                1, 0, 0,   # light1
                2, 1, 0    # light2
            ],
            [   # LIGHT2
                1, 0, 0,  # sensor1
                1, 1, 0,  # sensor2
                1, 0, 0,  # light1
                1, 2, 0   # light2
            ]
        ])

        calculator1 = Calculator([sensor1, sensor2], [light1, light2], coefficients)

        # 1*(1) + 0*(1)^2 + 0*sqrt(1) =  1
        # 2*(2) + 0*(2)^2 + 0*sqrt(2) =  4
        # 1*(0) + 0*(0)^2 + 0*sqrt(0) =  0
        # 2*(2) + 1*(2)^2 + 0*sqrt(2) =  8
        # --------------------------------
        #                 SUM(LIGHT1) = 13

        # 1*(1) + 0*(1)^2 + 0*sqrt(1) =  1
        # 1*(2) + 1*(2)^2 + 0*sqrt(2) =  6
        # 1*(0) + 0*(0)^2 + 0*sqrt(0) =  0
        # 1*(2) + 2*(2)^2 + 0*sqrt(2) = 10
        # --------------------------------
        #                 SUM(LIGHT2) = 17

        assert np.array_equal(calculator1.calculate_comparatives(), np.array([13, 17]))
        assert calculator1.which_light_should_be_green().id == 'two'

        calculator2 = Calculator([sensor1, sensor2], [light1, light2])

        # 1*(1) + 1*(1)^2 + 1*sqrt(1) =  1 + 1^2 + sqrt(1)
        # 1*(2) + 1*(2)^2 + 1*sqrt(2) =  2 + 2^2 + sqrt(2)
        # 1*(0) + 1*(0)^2 + 1*sqrt(0) =  0
        # 1*(2) + 1*(2)^2 + 1*sqrt(2) =  2 + 2^2 + sqrt(2)
        # ----------------------------------------------------
        #                 SUM(LIGHTX) =  5 +  9  + 1 + 2*2*sqrt(2)

        default_comparative = 5 + 9 + 1 + 2 * sqrt(2)
        assert np.array_equal(calculator2.calculate_comparatives(), np.array([default_comparative, default_comparative]))
        assert calculator2.which_light_should_be_green().id == 'zero'

    class TrivialSensor:
        def __init__(self, signal):
            self.signal = signal

        def get_signal(self):
            return self.signal

    class TrivialLight:
        def __init__(self, name,  timer):
            self.id = name
            self.timer = timer
