import base64
import os

from unittest.mock import Mock


def generate_id():
    return base64.urlsafe_b64encode(os.urandom(6)).decode('utf-8')


# Создаем mock-объект с name
mock_generate_id = Mock(return_value="mocked_id_with_name", name="IDGeneratorMock")

print(mock_generate_id())
print(mock_generate_id)
