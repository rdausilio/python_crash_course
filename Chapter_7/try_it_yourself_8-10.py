#7-8 Deli
sandwich_orders = ['ham', 'pastrami', 'bacon, egg and cheese', 'pastrami', 'grilled cheese', 'pb & j', 'pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami. So please don't order it. I will remove those orders.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


while sandwich_orders:
    for sandwich_order in sandwich_orders:
        made_sandwich = sandwich_orders.pop()
        print("Making the " + made_sandwich + " sandwich now.")

        finished_sandwiches.append(made_sandwich)

print("Finished making all the sandwiches.")

#7-9 No Pastrami (Above)

#7-10 Dream Vacation
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Where do you want to vacation? ")

    responses[name] = response

    repeat = input("Would you like to let another person? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to visit " + response + ".")
