num_one = []
num_two = []
operator = ""

class Calculator():
    def __init__(self):
        pass
    
    def add(self,a,b):
        return a+b

    def subtract(self,a,b):
        return a-b

    def multiply(self,a,b):
        return a*b

    def divide(self,a,b):
        return a/b

def display_results(result):
    print(result)

class ChooseOperation():
    def __init__(self):
        pass

    def operate(self,operator,num_one,num_two):
        self.operator = operator
        self.num_one = num_one
        self.num_two = num_two
        try:  
            if self.operator == "+":
                display_results(calculator.add(num_one, num_two))
            elif self.operator == ("-"):
                display_results(calculator.subtract(num_one, num_two))
            elif self.operator == ("*"):
                display_results(calculator.multiply(num_one, num_two))
            elif self.operator == ("/"):
                display_results(calculator.divide(num_one, num_two))
            else:
                print("Please input a correct operator.")
                user_input.input()
        except:
            print("Something went wrong.")


class UserInput():
    def __init__(self):
        pass

    def input(self):
        try:
            self.num_one = int(input("Enter the first number: "))
            self.operator = input("Enter the operator: ")
            self.num_two = int(input("Enter the second number: "))
        except ValueError:
            print("Please input only numbers")
            user_input.input()
        choose_operation.operate(self.operator,self.num_one,self.num_two)

calculator = Calculator()
user_input = UserInput()
choose_operation = ChooseOperation()

user_input.input()
