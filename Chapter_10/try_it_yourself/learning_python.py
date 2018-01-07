filepath = '../learning_python.txt'

with open(filepath) as file:
    lines = file.read()
print(lines)

with open(filepath) as file:
    for line in file:
        print(line.rstrip())

with open(filepath) as file:
    lines = file.readlines()

for line in lines:
    print(line.rstrip())