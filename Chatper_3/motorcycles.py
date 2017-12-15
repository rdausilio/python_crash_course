motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles1 = ['honda', 'yamaha', 'suzuki']
motorcycles1.append('ducati')
print(motorcycles1)

motorcycles2 = []
motorcycles2.append('honda')
motorcycles2.append('yamaha')
motorcycles2.append('suzuki')
print(motorcycles2)

motorcycles3 = motorcycles1 = ['honda', 'yamaha', 'suzuki']
motorcycles3.insert(0, 'ducati')
print(motorcycles3)

motorcycles4 = ['honda', 'yamaha', 'suzuki']
del motorcycles4[0]
print(motorcycles4)

motorcycles5 = ['honda', 'yamaha', 'suzuki']
print(motorcycles5)
popped_motorcycle = motorcycles5.pop()
print(motorcycles5)
print(popped_motorcycle)

last_owned = motorcycles4.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

first_owned = motorcycles4.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

print(motorcycles3)
motorcycles3.remove('honda')
print(motorcycles3)

too_expensive = 'honda'
motorcycles5.remove(too_expensive)
print(motorcycles5)
print("\nA " + too_expensive.title() + " is too expensive for me.")

