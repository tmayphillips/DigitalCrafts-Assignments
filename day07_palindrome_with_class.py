class Palindrome():
    def __init__ (self):
        pass

    def palindrome(self,word):
        self.word = word
        if self.word == self.word[::-1]:
            return ("palindrome")
            print("palindrome")
        else:
            return ("not palindrome")
            print("not palindrome")

word = Palindrome()
word.palindrome(input("Enter a word: ").lower())