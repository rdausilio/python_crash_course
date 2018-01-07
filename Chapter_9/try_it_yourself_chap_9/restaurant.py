class Restaurant():

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant's name is " + self.name.title() + ".")
        print("The restaurant serves " + self.cuisine_type + " type food.")

    def open_restaurant(self):
        print("The " + self.name.title() + " is open!")

    def number_served(self):
        print("The restaurant has served " + str(self.number_served) + " people.")

    def set_number_served(self, customers):
        self.number_served += customers


class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = ['salty cow', 'mocha mayhem', 'coconut chocolate chunk']

    def display_flavors(self):
        print("The ice cream stand has the following flavors: " + str(self.flavors))


new_restaurant = Restaurant("red rooster", "american")

print("The restaurant is called, " + new_restaurant.name.title() + ".")
print("The type of food served is " + new_restaurant.cuisine_type + ".")
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()

restaurant_1 = Restaurant("five guys", "burgers")
restaurant_2 = Restaurant("salsaritas", "american mexican")
restaurant_3 = Restaurant("gracies", "food poisoning")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

# restaurant_1.set_number_served(120)
# restaurant_1.number_served()

ice_cream_stand = Restaurant("ferris acres creamery", "ice cream")
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()
