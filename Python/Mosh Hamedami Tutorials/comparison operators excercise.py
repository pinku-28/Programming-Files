from unicodedata import name


username = input('What is your name? ')

if len(username) <= 3:
    print("Username must be at least 3 characters long.")
elif len(username) >= 15:
    print("Username must have 15 characters maximum.")
else:
    print("Sheesh, what a username!")
