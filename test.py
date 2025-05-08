import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_form_post_valid_data(self):
        test_cases = [
            {"from": "rur", "to": "usd", "convertable": "100", "expected": 1.24},
            {"from": "usd", "to": "eur", "convertable": "50", "expected": 44.04},
            {"from": "eur", "to": "rur", "convertable": "10", "expected": 919.169},
        ]

        for case in test_cases:
            response = self.app.post(
                '/',
                data={
                    'from': case['from'],
                    'to': case['to'],
                    'convertable': case['convertable']
                }
            )
            self.assertIn(str(case['expected']), response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()