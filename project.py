class User:

    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_name(self):
       return self.name.upper()

    def age(self, current_year):
        # age of the user given birth  year
        return current_year - self.birth_year


user = User("John", 1999)
print(user.age(2023))
print(user.get_name())