word = input("Enter a word: ")
word = word.lower()

if word == word[::-1]:
    print("palindrome")
else:
    print("not palindrome")