class ShoppingList:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.grocery_item = []

    def check(self,shopping_list,shopping_lists):
        self.shopping_list = shopping_list
        self.shopping_lists = shopping_lists

    def delete_list(self,shopping_list,shopping_lists):
        self.shopping_list = shopping_list
        self.shopping_lists = shopping_lists

        shopping_lists.pop(shopping_list)


class GroceryItem:
    def __init__(self,name,price,quantity):
        self.name = name 
        self.price = price
        self.quantity = quantity


# delete items
# delete lists
# total for each list
# total across all lists
# add duplicates

