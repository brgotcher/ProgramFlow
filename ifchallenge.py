name = input("Please enter your name: ")

age = int(input("Please enter your age: "))

if 18 <= age <= 30:
    print("Welcome to whatever, {}!".format(name))
else:
    print("GTFO, {}!".format(name))
