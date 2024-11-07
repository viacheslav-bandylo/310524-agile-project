from unittest.mock import Mock


# Сложный класс с методами и атрибутами
class DatabaseConnector:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        self.connection = f"Connected to {self.db_name}"
        return self.connection

    def disconnect(self):
        self.connection = None
        return "Disconnected"

    def execute_query(self, query):
        return f"Executing {query} on {self.db_name}"


# Создаем mock-объект с spec
mock_db_connector = Mock(spec=DatabaseConnector)

# Установка значений для атрибутов и методов mock-объекта
mock_db_connector.db_name = "mock_db"
mock_db_connector.connect.return_value = "Mocked connection established"
mock_db_connector.disconnect.return_value = "Mocked disconnection"
mock_db_connector.execute_query.return_value = "Mocked query execution"

# Использование mock-объекта
print(mock_db_connector.connect())  # Вывод: Mocked connection established
print(mock_db_connector.db_name)  # Вывод: mock_db
print(mock_db_connector.execute_query("SELECT * FROM users"))  # Вывод: Mocked query execution
