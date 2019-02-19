import unittest
from day07_palindrome_with_class import Palindrome

class PalindromeTests(unittest.TestCase):
    def setUp(self):
        self.palindrome = Palindrome()

    def test_palindrome(self):
        result = self.palindrome.palindrome("mom")
        self.assertEqual("palindrome",result)

    def test_non_palindrome(self):
        result = self.palindrome.palindrome("spies")
        self.assertEqual("not palindrome",result)

unittest.main()