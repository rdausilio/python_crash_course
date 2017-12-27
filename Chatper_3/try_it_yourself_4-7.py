#3-4 Guest List
dinner_guests = ['gerard way', 'barack obama', 'matt bomer', 'j.d. salinger']
print("Hey " + dinner_guests[0].title() + ", you want to come to dinner?")
print("Hey " + dinner_guests[1].title() + ", you want to come to dinner?")
print("Hey " + dinner_guests[2].title() + ", you want to come to dinner?")
print("Hey " + dinner_guests[3].title() + ", you want to come to dinner?")

#3-5 Changing Guest List
print("Unfortunately, " + dinner_guests[1] + " couldn't make it to dinner.")
dinner_guests[1] = 'patty bomer'
print("Hey " + dinner_guests[1] + " you can come to dinner now I guess.")

#3-6 More Guests
dinner_guests.insert(0, 'shannon mchale')
dinner_guests.insert(3, 'devin matte')
dinner_guests.append('bennett')
print("I'm lazy but here's the full list, " + str(dinner_guests))

#3-7 Shrinking Guest List
print("Shit. I can only invite two people for dinner.")
name1 = dinner_guests.pop()
print("I'm sorry, " + name1 + " I can't invite you to dinner.")
name1 = dinner_guests.pop()
print("I'm sorry, " + name1 + " I can't invite you to dinner.")
name1 = dinner_guests.pop()
print("I'm sorry, " + name1 + " I can't invite you to dinner.")
name1 = dinner_guests.pop()
print("I'm sorry, " + name1 + " I can't invite you to dinner.")
name1 = dinner_guests.pop()
print("I'm sorry, " + name1 + " I can't invite you to dinner.")
print(dinner_guests[0], " I can invite you to dinner. Congrats.")
print(dinner_guests[1], " I can invite you to dinner. Congrats.")
del dinner_guests[0]
del dinner_guests[0]
print(dinner_guests)