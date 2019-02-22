user_input = ""
shopping_lists = []
total = 0

from day07_grocery_app_modules import *

def show_menu():
    print("Enter 1 to add shopping list: ")
    print("Enter 2 to add grocery item: ")
    print("Enter 3 to view shopping lists: ")
    print("Enter 4 to delete a shopping list: ")
    print("Enter 5 to delete a grocery item: ")
    print("Enter 6 to total the grocery cost: ")
    print("Enter q to quit: ")

def add_shopping_list():
    name = input("Enter the name of shopping list: ")
    address = input("Enter address of shopping list: ")
    shopping_list = ShoppingList(name,address)
    if len(shopping_lists) > 0:
        shopping_list_check = ShoppingList(name,address)
        shopping_list_check.check(shopping_list,shopping_lists)
    shopping_lists.append(shopping_list)

def view_all_shopping_lists():
    for index in range(0,len(shopping_lists)):
        shopping_list = shopping_lists[index]
        print(f"{index + 1} - {shopping_list.name} - {shopping_list.address}")
        for grocery_item in shopping_list.grocery_item:
            print(f"{grocery_item.name}")

def add_grocery_item():
    try:
        for index in range(0,len(shopping_lists)):
            shopping_list = shopping_lists[index]
            print(f"{index + 1} - {shopping_list.name} - {shopping_list.address}")
        shopping_list_number = int(input("Enter the shopping list number: "))
        shopping_list = shopping_lists[shopping_list_number -1]
        name = input("Enter name of the grocery item: ")
        price = float(input("Enter the price of the item: "))
        quantity = int(input("Enter the quantity: "))
        grocery_item = GroceryItem(name,price,quantity)
        shopping_list.grocery_item.append(grocery_item)
    except ValueError:
        "Please make sure you are entering numbers when needed"
        add_grocery_item()

def delete_shopping_list():
    for index in range(0,len(shopping_lists)):
        shopping_list = shopping_lists[index]
        print(f"{index + 1} - {shopping_list.name} - {shopping_list.address}")
    shopping_list_number = int(input("Enter the shopping list number: "))
    del shopping_lists[shopping_list_number -1]

def delete_grocery_item():
    for index in range(0,len(shopping_lists)):
        shopping_list = shopping_lists[index]
        print(f"{index + 1} - {shopping_list.name} - {shopping_list.address}")
        for x in range(0,len(shopping_list.grocery_item)):
            grocery_item = shopping_list.grocery_item[x]
            print(f"{x + 1} - {grocery_item.name}")

    shopping_list_number = int(input("Enter the store number: "))     
    grocery_item_number = int(input("Enter the grocery item numbe: "))
    shopping_list = shopping_lists[shopping_list_number - 1]
    del shopping_list.grocery_item[grocery_item_number - 1]

def view_total():
    grand_total = 0
    for index in range(0,len(shopping_lists)):
        shopping_list = shopping_lists[index]
        print(f"{index + 1} - {shopping_list.name} - {shopping_list.address}")
        total = 0
        for grocery_item in shopping_list.grocery_item:
            print(f"{grocery_item.name} - {grocery_item.price} - {grocery_item.quantity}")
            total += (grocery_item.price * grocery_item.quantity)
            grand_total += (grocery_item.price * grocery_item.quantity)
        print(f"The total for {shopping_list.name} is ${total}.")
    print(f"The grand total for all stores is ${grand_total}")


while user_input != "q":
    show_menu()
    try:
        user_input = input("Enter your choice: ")
        if user_input == "1":
            add_shopping_list()
        if user_input == "2":
            add_grocery_item()
        if user_input == "3":
            view_all_shopping_lists()
        if user_input == "4":
            delete_shopping_list()
        if user_input == "5":
            delete_grocery_item()
        if user_input == "6":
            view_total()
    except ValueError:
        "Please make sure you enter a number"


