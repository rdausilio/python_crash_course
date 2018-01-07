filename = 'responses.txt'

with open(filename, 'w') as file:
    while True:
        prompt = "Why do you like programming?"
        prompt += "Enter 'q' to quit: "
        reason = input(prompt)
        if reason == 'q':
            break
        else:
            file.write(reason + "\n")
