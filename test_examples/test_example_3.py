import unittest
from parameterized import parameterized_class


def add(a, b):
    return a + b


@parameterized_class(('a', 'b', 'expected'), [
        (1, 2, 3),
        (3, 4, 7),
        (0, 0, 0),
        (-1, 1, 0),
        (-2, 1, -1),
    ])
class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(self.a, self.b), self.expected)

    # def test_add(self):
    #     test_cases = [
    #         (1, 2, 3),
    #         (3, 4, 7),
    #         (0, 0, 0),
    #         (-1, 1, 0)
    #     ]
    #
    #     for param1, param2, expected in test_cases:
    #         with self.subTest(param1=param1, param2=param2):
    #             self.assertEqual(add(param1, param2), expected)


if __name__ == '__main__':
    unittest.main()
