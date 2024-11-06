from unittest import TestCase
from simple_test import divide

class TestFunctions(TestCase):

    def test_result(self):
        dividend = 15
        divisor = 3
        result = 5.0
        self.assertAlmostEqual(divide(dividend, divisor), result, delta = 0.0001)

    def test_result_negative(self):
        dividend = 15
        divisor = -3
        result = -5.0
        self.assertAlmostEqual(divide(dividend, divisor), result, delta=0.0001)

    def test_result_zero(self):
        dividend = 0
        divisor = 3
        result = 0.0
        self.assertEqual(divide(dividend, divisor), result)

    def test_error(self):
        with self.assertRaises(ValueError):
            divide(25, 0)