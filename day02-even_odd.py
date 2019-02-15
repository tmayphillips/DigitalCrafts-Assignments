number = int(input("Enter a whole number"))
remainder = number % 2

if remainder == 0:
    print("Even")
elif remainder == 1:
    print("Odd")
else:
    print("I said a whole number")
