#8-9 Magicians
magician_name_list = ["houdini", "pen", "teller"]

def show_magicians(magicians):
    for magician in magician_name_list:
        print("The magician's name is " + magician.title() + ".")

show_magicians(magician_name_list)

#8-10 Great Magicians
great_magician_list = []

def make_great_magicians(magicians):
    for magician in magician_name_list:
        great_magician = (magician.title() + " The Great")
        great_magician_list.append(great_magician)
    print(great_magician_list)

make_great_magicians(magician_name_list)

#8-11 Unchanged Magicans
def show_unchanged(list):
    new_list = make_great_magicians(list)
    old_list = show_magicians(list)
    print(new_list)
    print(old_list)

show_unchanged(magician_name_list)