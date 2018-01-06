#7-1 Rental Car
car = input("What kind of rental car would you like? ")

print("Let me see if I can find you a " + car)

print()

#7-2 Restaurant Seating
people_number = input("How many people are in your dinner group? ")
people_number = int(people_number)

if people_number > 8:
    print("Sorry, you'll have to wait a bit for a table.")
else:
    print("You're table is ready now.")

print()

#7-3 Multiples of Ten
number = input("What number do you want to check? ")
number = int(number)

if number % 10 == 0:
    print(str(number) + " is a multiple of ten.")
else:
    print("Sorry, " + str(number) + " is not a multiple of ten.")