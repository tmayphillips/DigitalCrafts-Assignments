names = ["Alex","John","Mary","Steve","John", "Steve"]
names_no_repeat = []

for value in names:
    if value in names_no_repeat:
        next
    else:
        names_no_repeat.append(value)

print(names_no_repeat)