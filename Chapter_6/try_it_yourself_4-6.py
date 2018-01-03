#6-4 Glossary 2
glossary = {
    "string": "words stored in single quotes or double quotes",
    "if statement": "a statement that compares a value",
    "dictionary": "an array of key-value pairs",
    "list": "a list of value, can be anything and is mutable",
    "boolean": "a list that can also be anything, but is immutable",
    "for loop": "a way of iteratively going through items in an array",
    "key-value pair": "an item and the value(s) that are associated with it",
    "integer": "a number object",
    "print statement": "a built in function of python",
    "loop (general)": "a structure or series that goes back to the beginning"
}

for term, definition in glossary.items():
    print("\nThe term, " + "'" + term.title() + "'" +
    "has a definition of " + definition.title() + ".")

#6-5 Rivers
rivers = {
    'egypt': 'nile',
    'mississippi': 'mississippi',
    'washington d.c': 'potomac'
}

for place, river in rivers.items():
    print("\nThe, " + river.title() + " river" +
          " flows through " + place.title())

#6-6 Polling
print()

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

friends = ['phil', 'sarah', 'juston', 'devin']
for name in friends:
    print(name.title())

    if name in favorite_languages:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + " !")
    elif name not in favorite_languages.keys():
        print(name.title() + ", please take our poll!")
