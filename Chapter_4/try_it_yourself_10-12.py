#4-10 Slices
players = ['charles', 'martin', 'michael', 'florence', 'eli']

print("The first three items in the list are:")
print(players[0:2])

print("\nThree items from the middle of the list are:")
print(players[1:4])

print("\nThe last three items in the list are:")
print(players[-3:])

#4-11 My Pizzas, Your Pizzas
my_pizzas = ['pepperoni', 'cheese', 'bacon and pepperoni']
friend_pizzas = my_pizzas[:]

my_pizzas.append('four cheese')
friend_pizzas.append('steak')
print("\nMy favorite pizzas are:")
for pizzas in my_pizzas:
    print(pizzas.title())

print("\nMy friend's favorite pizzas are:")
for pizzas in friend_pizzas:
    print(pizzas.title())

print()

#4-12 More Loops
my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli']
friend_foods = ['pizza', 'falafel', 'carrot cake', 'ice cream']
for food in my_foods:
    print(food.title())

print()

for food in friend_foods:
    print(food.title())

