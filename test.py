import unittest

class app:
    def calculate(self, val: float, _from: str, _to: str) -> float:
        diction = {
            "rur" : {
                "rur": 1,
                "usd": 0.0124,
                "eur": 0.0109
            },
            "usd" : {
                "rur": 80.9644,
                "usd": 1,
                "eur": 0.8808
            },
            "eur" : {
                "rur": 91.9169,
                "usd": 1.1353,
                "eur": 1
            }
        }
        return val * diction[_from][_to]




class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app()

    def test_rur_to_rur(self):
        self.assertEqual(self.app.calculate(100, "rur", "rur"), 100)

    def test_rur_to_usd(self):
        self.assertEqual(self.app.calculate(100, "rur", "usd"), 1.24)

    def test_rur_to_eur(self):
        self.assertEqual(self.app.calculate(100, "rur", "eur"), 1.09)

    def test_usd_to_rur(self):
        self.assertEqual(self.app.calculate(100, "usd", "rur"), 8096.44)

    def test_usd_to_usd(self):
        self.assertEqual(self.app.calculate(100, "usd", "usd"), 100)

    def test_usd_to_eur(self):
        self.assertEqual(self.app.calculate(100, "usd", "eur"), 88.08)



if __name__ == '__main__':
    unittest.main()