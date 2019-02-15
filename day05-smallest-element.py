numbers = [15,5,25,14,99,53]
smallest_number = numbers[0]

for value in numbers:
    if value < smallest_number:
        smallest_number = value
    else:
        next

print(smallest_number)