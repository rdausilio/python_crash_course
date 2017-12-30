#5-3 Alien Colors #1
alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'red':
    print("I guess you can earn 5 points!")

#5-4 Alien Colors #2
if alien_color == 'green':
    print("You got 5 points for shooting the alien!")
else:
    print("You just got 10 points.")

#5-5 Alien Colors #3
if alien_color == 'green':
    print("You've just earned 5 points!")
elif alien_color == 'yellow':
    print("You've just earned 10 points!")
elif alien_color == 'red':
    print("You've just earned 15 points!")

#5-6 Stages of Life
age = 62
if age < 2:
    print("You're a baby.")
elif age > 2 and age < 4:
    print("You're a toddler.")
elif age > 4 and age < 13:
    print("You're a kid.")
elif age > 13 and age < 20:
    print("You're a teenager.")
elif age > 20 and age < 65:
    print("You're an adult.")
elif age > 65:
    print("You're an elder.")

#5-7 Favorite Fruit
favorite_fruits = ['strawberry', 'blueberry', 'raspberry']
if 'strawberry' in favorite_fruits:
    print('You really like strawberries!')
if 'blueberry' in favorite_fruits:
    print("You really like blueberries!")
if 'raspberry' in favorite_fruits:
    print("You really like raspberries!")
if 'library' in favorite_fruits:
    print("Libraries aren't a fruit.")
if 'kiwi' in favorite_fruits:
    print("Kiwis are gross.")
