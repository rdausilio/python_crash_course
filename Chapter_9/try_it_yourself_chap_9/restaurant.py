class Restaurant():

    def __init__(self, name, cusine_type):
        self.name = name
        self.cusine_type = cusine_type

    def describe_restaurant(self):
        print("The restaurant's name is " + self.name.title() + ".")
        print("The restaurant serves " + self.cusine_type + " type food.")

    def open_restaurant(self):
        print("The " + self.name.title() + " is open!")

new_restaurant = Restaurant("red rooster", "american")

print("The restaurant is called, " + new_restaurant.name.title() + ".")
print("The type of food served is " + new_restaurant.cusine_type + ".")
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()

restaurant_1 = Restaurant("five guys", "burgers")
restaurant_2 = Restaurant("salsaritas", "american mexican")
restaurant_3 = Restaurant("gracies", "food poisoning")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()