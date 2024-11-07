from unittest.mock import Mock
import base64
import os


def generate_id():
    return base64.urlsafe_b64encode(os.urandom(6)).decode('utf-8')


# Создаем mock-объект с side_effect
def custom_side_effect():
    return "mocked_id_with_side_effect"


# Создаем mock-объект с return_value
# mock_generate_id = Mock(return_value="mocked_id")
mock_generate_id = Mock(side_effect=custom_side_effect)

# Использование mock-объекта
print(mock_generate_id())
