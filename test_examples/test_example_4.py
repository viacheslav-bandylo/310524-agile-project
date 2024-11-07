import unittest


def add(a, b):
    return a + b


def create_test(param1, param2):
    def test(self):
        self.assertEqual(add(param1, param2), param1 + param2)

    return test


class TestAddFunction(unittest.TestCase):
    pass


# Создание тестов динамически и добавление их в TestCase
test_cases = [
    (1, 2, 3),
    (3, 4, 7),
    (0, 0, 0),
    (-1, 1, 0)
]

for i, (param1, param2, expected) in enumerate(test_cases):
    test_name = f'test_add_{i}'
    test = create_test(param1, param2)
    setattr(TestAddFunction, test_name, test)

if __name__ == '__main__':
    unittest.main()
