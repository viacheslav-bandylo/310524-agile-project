import unittest
from math_operations import add


class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertRaises(TypeError, add(5, "hello"))
        self.assertRaises(TypeError, add(3, None))
