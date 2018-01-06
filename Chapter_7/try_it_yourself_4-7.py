#7-4 Pizza Toppings
prompt = "\nWhat topping(s) do you want to add to the pizza?"
prompt += "\nEnter 'quit' to exit. "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print("Adding " + topping + " to pizza!")

#7-5 Movie Tickets
print()

prompt_1 = "\nWhat is the age?"
prompt_1 += "\nEnter 'quit' to exit. "

while True:
    ticket_age = (input(prompt_1))
    if ticket_age == 'quit':
        break
    elif int(ticket_age) < 3:
        print("Your ticket is free!")
    elif int(ticket_age) < 12 and int(ticket_age) >= 3:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")

#7-6 Three Exits
prompt_2 = "\nWhat topping(s) do you want to add to the pizza?"
prompt_2 += "\nYou are allowed only 6 toppings. Enter 'quit' to stop early"

topping_num = 0
while topping_num <= 6:
    topping = input(prompt_2)

    if topping == 'quit':
        break
    else:
        print("Adding " + topping + " to pizza!")
        topping_num += 1

#7-7 Infinity

while True:
    print("Hello world!")