from collections import OrderedDict

glossary = OrderedDict()

glossary["string"] = "words stored in single quotes or double quotes"
glossary["if statement"] = "a statement that compares a value"
glossary["dictionary"] = "an array of key-value pairs"
glossary["list"] = "a list of value, can be anything and is mutable"
glossary["boolean"] = "a true false value"
glossary["for loop"] = "a way of iteratively going through items in an array"
glossary["integer"] = "a number object"
glossary["key-value pair"] = "an item and the value(s) that are associated with it"
glossary["print statement"] = "a built in function of python"
glossary["loop (general)"]="a structure or series that goes back to the beginning"

for term, definition in glossary.items():
    print(term.title() + " is defines as " + definition)