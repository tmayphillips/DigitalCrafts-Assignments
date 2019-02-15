number = int(input("Enter a whole number"))
remainder3 = number % 3
remainder5 = number % 5

if remainder3 == 0 and remainder5 == 0:
    print("Fizz Buzz")
elif remainder3 == 0:
    print("Fizz")
elif remainder5 == 0:
    print("Buzz")
else:
    print("Not divisible by 3 or 5")
