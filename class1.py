class User():

    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        print(self.first_name, self.last_name, self.age, self.city)

    def greet_use(self):
        print("""Hello my dear """ + self.first_name, self.last_name)


djon = User('Djon', 'Smit', 23, 'NY')
nick = User('Nick', 'Fly', 28, 'NY')
alis = User('Alis', 'Rain', 29, 'NY')

djon.describe_user(),djon.greet_use()