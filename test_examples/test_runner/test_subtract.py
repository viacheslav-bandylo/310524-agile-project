import unittest
from math_operations import subtract


class TestSubtract(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
