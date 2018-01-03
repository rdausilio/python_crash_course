#6-1 Person
person = {
    "first_name": "rowan",
    "last_name": "d'ausilio",
    "age": 18,
    "city": "rochester"
}
print("Hi, my name is " + person["first_name"].title() + " " + person["last_name"].title() + ".")
print("I am " + str(person["age"]) + " years old.")
print("I live in the city of " + person["city"].title() + ".")

print()

#6-2 Favorite Number
numbers = {
    "nick": "14",
    "rowan": "13",
    "terry": "5",
    "declan": "19",
    "juston": "0"
}

print("Nick's favorite number is " + numbers["nick"] + ".")
print("Rowan's favorite number is " + numbers["rowan"] + ".")
print("Terry's favorite number is " + numbers["terry"] + ".")
print("Declan's favorite number is " + numbers["declan"] + ".")
print("Juston's favorite number is " + numbers["juston"] + ".")

print()

#6-3 Glossary
glossary = {
    "string": "words stored in single quotes or double quotes",
    "if statement": "a statement that compares a value",
    "dictionary": "an array of key-value pairs",
    "list": "a list of value, can be anything and is mutable",
    "boolean": "a list that can also be anything, but is immutable"
}

print("'string': " + glossary["string"] + ".")
print("\n'if statement': " + glossary["if statement"] + ".")
print("\n'dictionary' : " + glossary["dictionary"] + ".")
print("\n'list' : " + glossary["list"] + ".")
print("\n'boolean' : " + glossary["boolean"] + ".")