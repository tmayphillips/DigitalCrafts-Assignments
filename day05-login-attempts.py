class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name}{last_name}"
        self.height = ""
        self.weight = ""
        self.eye_color = ""
        self.hair_color = ""
        self.login_attempts = 0

    def describe_user(self):
        print(f"First name is {self.first_name}")
        print(f"Last name is {self.last_name}")
        print(f"Height is {self.height}")
        print(f"Weight is {self.weight}")
        print(f"Eye color is {self.eye_color}")
        print(f"Hair color is {self.hair_color}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}! How're you today?")

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        self.login_attempts = 0

johndoe = User("John","Doe")
johndoe.increment_login_attempts()
johndoe.increment_login_attempts()
print(johndoe.login_attempts)
johndoe.reset_login_attempts()
print(johndoe.login_attempts)