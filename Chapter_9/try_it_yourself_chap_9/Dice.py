from random import randint


class Die:

    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


die1 = Die(6)
die2 = Die(10)
die3 = Die(20)


print("rolling d6")

count = 0
while count <= 10:
    die1.roll_die()
    count += 1

print("Rolling d10")

count = 0
while count <= 10:
    die2.roll_die()
    count += 1

print("rolling d20")

count = 0
while count <= 10:
    die3.roll_die()
    count += 1