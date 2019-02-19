import unittest
from day07_calculator_with_class import Calculator

class CalculatorTests(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        result = self.calculator.add(2,3)
        self.assertEqual(5,result)

    def test_subtraction(self):
        result = self.calculator.subtract(5,2)
        self.assertEqual(3,result)

    def test_multiplication(self):
        result = self.calculator.multiply(2,5)
        self.assertEqual(10,result)

    def test_division(self):
        result = self.calculator.divide(15,5)
        self.assertEqual(3,result)

    def tearDown(self):
        print("TEARDOWN")


unittest.main()