import unittest
from main import generate_price_curve

class TestPriceCurves(unittest.TestCase):
    def test_generate_price_curve_returns_expected_elements(self):
        prices = generate_price_curve(5)
        assert len(prices) == 5
