class ShoppingList:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.grocery_item = []

    def check(self,shopping_list,shopping_lists):
        self.shopping_list = shopping_list
        self.shopping_lists = shopping_lists

class GroceryItem:
    def __init__(self,name,price,quantity):
        self.name = name 
        self.price = price
        self.quantity = quantity

# total for each list
# total across all lists
# add duplicates

