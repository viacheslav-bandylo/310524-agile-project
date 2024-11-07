import json
import unittest


def parse_json(data):
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON data")


class TestParseJson(unittest.TestCase):
    def setUp(self):
        self.valid_json = '''
       [
           {
               "pk": 1,
               "name": "Мистика"
           },
           {
               "pk": 2,
               "name": "Биография"
           },
           {
               "pk": 3,
               "name": "Ужасы"
           },
           {
               "pk": 4,
               "name": "Детектив"
           }
       ]
       '''
        self.single_object_json = '{"pk": 1, "name": "Мистика"}'
        self.empty_object_json = '{}'
        self.empty_array_json = '[]'
        self.invalid_json = 'invalid json'
        self.partial_invalid_json = '{"pk": 1, "name": "Мистика"'
        self.null_json = None
        self.large_json = json.dumps([{"pk": i, "name": f"Category {i}"} for i in range(1000)])
        self.nested_json = json.dumps({
            "pk": 1,
            "details": {
                "description": "A detailed description",
                "metadata": {
                    "created": "2023-06-23",
                    "modified": "2023-06-24"
                }
            },
            "tags": ["fiction", "mystery", "thriller"]
        })

    def test_valid_json(self):
        self.assertEqual(parse_json(self.valid_json)[0], {"pk": 1, "name": "Мистика"})
        self.assertIsInstance(parse_json(self.valid_json), list)

    def test_single_object_json(self):
        self.assertEqual(parse_json(self.single_object_json), {"pk": 1, "name": "Мистика"})
        self.assertIsInstance(parse_json(self.single_object_json), dict)

    def test_empty_object_json(self):
        self.assertEqual(parse_json(self.empty_object_json), {})
        self.assertIsInstance(parse_json(self.empty_object_json), dict)

    def test_empty_array_json(self):
        self.assertEqual(parse_json(self.empty_array_json), [])
        self.assertIsInstance(parse_json(self.empty_array_json), list)

    def test_invalid_json(self):
        with self.assertRaises(ValueError):
            parse_json(self.invalid_json)

    def test_partial_invalid_json(self):
        with self.assertRaises(ValueError):
            parse_json(self.partial_invalid_json)

    def test_none_type_json(self):
        with self.assertRaises(TypeError):
            parse_json(self.null_json)

    def test_large_json(self):
        parsed_data = parse_json(self.large_json)
        self.assertIsInstance(parsed_data, list)
        self.assertEqual(len(parsed_data), 1000)
        self.assertEqual(parsed_data[0], {"pk": 0, "name": "Category 0"})

    def test_nested_json(self):
        parsed_data = parse_json(self.nested_json)
        self.assertIsInstance(parsed_data, dict)
        self.assertIn("details", parsed_data)
        self.assertIn("tags", parsed_data)
        self.assertIsInstance(parsed_data["details"], dict)
        self.assertIsInstance(parsed_data["tags"], list)

    def tearDown(self):
        del self.valid_json
        del self.single_object_json
        del self.empty_object_json
        del self.empty_array_json
        del self.invalid_json
        del self.partial_invalid_json
        del self.null_json
        del self.large_json
        del self.nested_json


if __name__ == '__main__':
    unittest.main()
