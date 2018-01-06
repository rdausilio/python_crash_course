#8-12 Sandwiches
def make_sandwich(*items):
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print("- " + item)

make_sandwich("bacon", "egg", "cheese")
make_sandwich("cheese")
make_sandwich("cheese", "burger", "bacon", "ketchup")

print()

#8-13 User Profile
def build_profile(first, last, **user_info):
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile("rowan", "d'ausilio", location="rochester", field="computing security", age=18)

print(user_profile)

print()

#8-14 Cars
def build_car(make, model,**car_info):
    car = {}
    car["make"] = make
    car["model"] = model
    for key, value in car_info.items():
        car[key] = value
    return car

car = build_car("chevrolet", "silverado", year=2017, color="silver")

print(car)