import json
import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_reverse_string(self):
        data = {'string': 'hello'}
        response = self.app.post('/reverse', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'reversed_string': 'olleh'})

    def test_square_number(self):
        data = {'number': 5}
        response = self.app.post('/square', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'square': 25})

if __name__ == '__main__':
    unittest.main()