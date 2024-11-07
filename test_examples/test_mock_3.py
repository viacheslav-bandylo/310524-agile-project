import base64
import os

from unittest.mock import create_autospec


class IDGenerator:
    def generate(self):
        return base64.urlsafe_b64encode(os.urandom(6)).decode('utf-8')


# Создаем mock-объект с autospec
mock_id_generator = create_autospec(IDGenerator)
mock_id_generator.generate.return_value = "mocked_id_with_autospec"

print(mock_id_generator.generate())
