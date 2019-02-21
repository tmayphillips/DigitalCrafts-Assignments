import json

# ACTIVITY 1 #
print("Activity 1")
name = input("What's your name?\n")

with open('name.json', 'w') as file_object:
    json.dump(name,file_object)

print("Activity 1 completed")

# ACTIVITY 2 #
print("Activity 2")
with open('name.json') as file_object:
    names = json.load(file_object)
    print(names)

print("Activity 2 completed")

# ACTIVITY 3 #
print("Activity 3")
import re


full_name = input("Enter your first and last name: \n")
name_list = re.sub("[^\w]", " ",  full_name).split()
name_dictionary = {"first_name": name_list[0], "last_name": name_list[1]}

with open('name.json', 'w') as file_object:
    json.dump(name_dictionary,file_object)
print("Activity 3 completed")

# ACTIVITY 4 #
print("Activity 4")
with open('name.json') as file_object:
    names = json.load(file_object)
    print(names)


print("Activity 4 completed")

