numbers = [15,5,25,14,99,53]
max_number = numbers[0]

for value in numbers:
    if value > max_number:
        max_number = value
    else:
        next

print(max_number)