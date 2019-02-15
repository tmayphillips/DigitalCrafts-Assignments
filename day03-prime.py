number = int(input("Enter a number: "))

x = number-1
prime = True

while x > 1:
    if number % x == 0:
        prime = False
    x = x-1

if prime == True:
    print("Prime")
else:
    print("Not Prime")
