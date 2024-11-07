from datetime import datetime
import unittest
from datetime import datetime
from unittest.mock import patch

from get_datetime import get_current_date


class TestDateOperations(unittest.TestCase):
    @patch('get_datetime.datetime')
    def test_get_current_date(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 6, 11)
        self.assertEqual(get_current_date(), '2024-06-11')


if __name__ == '__main__':
    unittest.main()
