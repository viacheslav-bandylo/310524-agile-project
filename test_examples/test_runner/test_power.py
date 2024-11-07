from math_operations import power
import unittest


class TestPower(unittest.TestCase):
    def test_power_with_arguments(self):
        self.assertEqual(power(6, 3), 216)

    def test_power_by_zero(self):
        self.assertRaises(ValueError, power, 6, 0)
