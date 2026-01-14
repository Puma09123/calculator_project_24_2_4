import unittest
from calculator.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add_positive(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_subtract_positive(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_multiply_positive(self):
        self.assertEqual(self.calc.multiply(3, 5), 15)

    def test_divide_positive(self):
        self.assertEqual(self.calc.divide(20, 4), 5)


if __name__ == "__main__":
    unittest.main()
