import unittest


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


class TestDivideFunction(unittest.TestCase):
    def test_divide_positive_numbers(self):
        self.assertEqual(divide(6, 3), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(6, 0)


class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)


class TestSubtractFunction(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)


def loader():
    loader = unittest.TestLoader()

    suite = loader.discover('test_example/', pattern='test_*.py')

    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    loader()

# if __name__ == '__main__':
#     # Создаем тестовый набор
#     suite = unittest.TestSuite()
#     suite.addTest(unittest.makeSuite(TestAddFunction))
#     suite.addTest(unittest.makeSuite(TestSubtractFunction))
#
#     # Запускаем тесты из набора
#     runner = unittest.TextTestRunner()
#     runner.run(suite)
