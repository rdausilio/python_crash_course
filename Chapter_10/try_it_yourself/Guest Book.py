filename = 'guest_book.txt'

with open(filename, 'w') as file:
    while True:
        prompt = "What is your name?"
        prompt += "\nEnter 'quit' to quit: "
        name = input(prompt)
        if name == 'quit':
            break
        else:
            file.write(name + "\n")