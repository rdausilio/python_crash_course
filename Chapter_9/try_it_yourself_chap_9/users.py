class User():

    def __init__(self, first_name, last_name, age, gender, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        full_name = self.first_name.title() + ' ' + self.last_name.title()
        print("The user's name is: " + full_name + " their age is " + self.age + " their gender is " +
              self.gender + " and their location is " + self.location.title() + ".")

    def greet_user(self):
        print("Hello " + self.first_name.title() + ", how are you today?")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print("Login attempts = " + str(self.login_attempts))

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Login attempts reset.")


class Admin(User):

    def __init__(self, first_name, last_name, age, gender, location):
        super().__init__(first_name, last_name, age, gender, location)
        self.privileges = ['can delete post', 'can ban user', 'can add post']

    def show_privileges(self):
        print("Admin's can: " + str(self.privileges) + ".")


user_1 = User("rowan", "d'ausilio", "18", "male", "rochester")
user_2 = User("athena", "d'ausilio", "4 and a half", "female", "connecticut")
user_3 = User("john", "smith", "13", "male", "new york")

user_1.describe_user()
user_1.greet_user()
print()
user_2.describe_user()
user_2.greet_user()
print()
user_3.describe_user()
user_3.greet_user()
print()
user_1.increment_login_attempts()
user_3.increment_login_attempts()
user_2.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.reset_login_attempts()
user_1.increment_login_attempts()

user_4 = Admin("rowan", "d'ausilio", "18", "male", "rochester")
user_4.describe_user()
user_4.show_privileges()
