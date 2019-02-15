numbers = [0,1,2,4,5,7,8,9]
missing_number = []
number = 0

while number < 10:
    if number in numbers:
        next
    else:
        missing_number.append(number)
    number = number + 1

print(missing_number)