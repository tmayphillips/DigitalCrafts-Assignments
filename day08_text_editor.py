with open('learning_python.txt', 'w') as file_object:
    file_object.write("In Python you can create and use variables.\n")
    file_object.write("In Python you can create classes.\n")
    file_object.write("In Python you can do unit tests.\n")
    file_object.write("In Python you can create and edit files.\n")

with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents)

with open('learning_python.txt') as file_object:
    for line in file_object:
        print(line)

with open('learning_python.txt') as file_object:
    lines = file_object.readline()

print(lines)