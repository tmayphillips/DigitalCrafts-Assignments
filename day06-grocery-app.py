user_input = ""
shopping_lists = []

class ShoppingList:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.grocery_item = []

class GroceryItem:
    def __init__(self,name,price,quantity):
        self.name = name 
        self.price = price
        self.quantity = quantity

def show_menu():
    print("Enter 1 to add shopping list: ")
    print("Enter 2 to add grocery item: ")
    print("Enter 3 to view shopping lists: ")
    print("Enter q to quit: ")

def add_shopping_list():
    name = input("Enter the name of shopping list: ")
    address = input("Enter address of shopping list: ")
    shopping_list = ShoppingList(name,address)
    shopping_lists.append(shopping_list)

def view_all_shopping_lists():
    for index in range(0,len(shopping_lists)):
        shopping_list = shopping_lists[index]
        print(f"{shopping_list.name} - {shopping_list.address}")
        for grocery_item in shopping_list.grocery_item:
            print(f"{grocery_item.name}")

def add_grocery_item():
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

while user_input != "q":
    show_menu()
    user_input = input("Enter your choice: ")
    if user_input == "1":
        add_shopping_list()
    if user_input == "2":
        add_grocery_item()
    if user_input == "3":
        view_all_shopping_lists()