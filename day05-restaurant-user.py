class Restaurant():
    def __init__(self,restaurant_name,restaurant_cuisine):
        self.restaurant_name = restaurant_name
        self.restaurant_cuisine = restaurant_cuisine

    def describe_restaurant(self,restaurant):
        print(restaurant.restaurant_name)
        print(restaurant.restaurant_cuisine)
    def open_restaurant(self):
        print("The restaurant is open!")

marios = Restaurant("Mario's","Italian")
print(marios.restaurant_name)
print(marios.restaurant_cuisine)
marios.describe_restaurant(marios)
marios.open_restaurant()

labrisa = Restaurant("La Brisa's","Mexican")
burger = Restaurant("Burger Joint","American")

labrisa.describe_restaurant(labrisa)
burger.describe_restaurant(burger)

class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name}{last_name}"
        self.height = ""
        self.weight = ""
        self.eye_color = ""
        self.hair_color = ""

    def describe_user(self):
        print(f"First name is {self.first_name}")
        print(f"Last name is {self.last_name}")
        print(f"Height is {self.height}")
        print(f"Weight is {self.weight}")
        print(f"Eye color is {self.eye_color}")
        print(f"Hair color is {self.hair_color}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}! How're you today?")

tiffanymayphillips = User("Tiffany","May-Phillips")
tiffanymayphillips.height = 62
tiffanymayphillips.weight = 140
tiffanymayphillips.eye_color = "Hazel"
tiffanymayphillips.hair_color = "Brown"

johndoe = User("John","Doe")
johndoe.height = 74
johndoe.weight = 185
johndoe.eye_color = "Blue"
johndoe.hair_color = "Blonde"

janedoe = User("Jane","Doe")
janedoe.height = 66
janedoe.weight = 155
janedoe.eye_color = "Brown"
janedoe.hair_color = "Red"

tiffanymayphillips.describe_user()
johndoe.describe_user()
janedoe.describe_user()

tiffanymayphillips.greet_user()
johndoe.greet_user()
janedoe.greet_user()