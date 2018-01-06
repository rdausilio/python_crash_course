#8-3 T-Shirt
def make_shirt(size, text):
    print("\nThe size of the shirt is " + size + ".")
    print("The text on the shirt is " + text + ".")

make_shirt("small", "hello")
make_shirt(size="large", text="hello")

#8-4 Large Shirt

def make_shirt_2(size="large", text="I love python"):
    print("\nThe size of the shirt is " + size + ".")
    print("The text on the shirt is " + text + ".")

make_shirt_2()
make_shirt_2(size="medium")
make_shirt_2(size="small", text="test")

#8-5 Cities

def describe_city(name, country="Italy"):
    print("The city of " + name + " is in the country of " + country + ".")

describe_city(name="Rome")
describe_city(name="Venice")
describe_city(name="New York", country="United States")