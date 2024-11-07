import unittest

if __name__ == '__main__':
    # Используем загрузчик для поиска всех тестов
    loader = unittest.TestLoader()
    suite = loader.discover('.', pattern='test_*.py')

    # Запускаем все тесты
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
