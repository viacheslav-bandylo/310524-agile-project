import unittest
from math_operations import divide


class TestDivide(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, divide, 6, 0)

    # def test_divide_by_zero(self):
    #     with self.assertRaises(ValueError):
    #         divide(6, 0)
