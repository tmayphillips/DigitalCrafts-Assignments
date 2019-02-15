lines = 9
symbol = "*"
space = " "
char = (lines * 2) - 1

count = 1
while count <= lines:
    num_spaces = space * (lines - count)
    num_symbols = symbol * (count * 2 - 1)
    print(f"{num_spaces}{num_symbols}{num_spaces}")
count = count + 1