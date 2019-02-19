import unittest
from day07_factorial_with_class import Factorial

class PalindromeTests(unittest.TestCase):
    def setUp(self):
        self.factorial = Factorial()

    def test_factorial(self):
        result = self.factorial.factorial(5)
        self.assertEqual(120,result)

unittest.main()