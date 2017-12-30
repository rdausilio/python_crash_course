#5-8 Hello Admin/ 5-9 No Users
usernames = ['rowan', 'nancy', 'anthony', 'skyler', 'admin']

if usernames != []:
    for name in usernames:
        if name == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + name + ", thank you for logging in again.")
else:
    print("We need to find more users!")

#5-10 Checking Usernames
current_users = ['rowan', 'nancy', 'anthony', 'kate', 'athena']

new_users = ['morgan', 'brett', 'chris', 'athena', 'nancy']

for new_user in new_users:
    if new_user in current_users:
        print("Sorry the username: " + new_user + " is already taken. Please pick a new usernmae.")
    else:
        print("That username is available!")

#5-11 Ordinal Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(str(number) + 'th')