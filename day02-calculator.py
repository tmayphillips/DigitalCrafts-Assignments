no1 = int(input("Enter the first number"))
operator = input("Enter the operator")
no2 = int(input("Enter the second number"))

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def display_results(result):
    print(result)

if operator == "+":
    display_results(add(no1,no2))
elif operator == ("-"):
    display_results(subtract(no1,no2))
elif operator == ("*"):
    display_results(multiply(no1,no2))
elif operator == ("/"):
    display_results(divide(no1,no2))
else:
    print("Not a correct operator")
