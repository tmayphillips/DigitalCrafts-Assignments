name = input("What's your name?\n")

with open('guess.txt', 'w') as file_object:
    file_object.write(name)

user_input = ""

with open('programming.txt', 'w') as file_object:
    while user_input != "q":
        user_input = input("What do you like about programming?\nPress q to quit\n")
        file_object.write(user_input)

        file_object.write("\n")
