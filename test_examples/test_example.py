import unittest


def suite():
    group_suite = unittest.TestSuite()
    group_suite.addTest(TestCalculator('test_add'))
    group_suite.addTest(TestCalculator('test_subtract'))

    return group_suite


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)

    def tearDown(self):
        del self.calc


if __name__ == '__main__':
    # unittest.main()
    group_suite = unittest.TestSuite()
    group_suite.addTest(TestCalculator('test_add'))
    group_suite.addTest(TestCalculator('test_subtract'))
