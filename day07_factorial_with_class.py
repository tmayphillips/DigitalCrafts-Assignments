
class Factorial():
    def __init__ (self):
        pass

    def factorial(self,number):
        self.number = number
        self.factorial = self.number

        while self.number > 1:
            self.factorial = self.factorial * (self.number-1)
            self.number -= 1

        return(self.factorial)

number = Factorial()
number.factorial(int(input("Enter a number: ")))
print(number.factorial)