options = {
    1: "Learn Python",
    2: "Learn Java",
    3: "Go swimming",
    4: "Have Dinner",
    5: "Go to bed",
    0: "Exit"
}

choice = 1
while choice != 0:
    print("Please choose your option from the list: ")
    for i in options:
        print(str(i) + ". ", options[i])

    choice = int(input())
    if choice in options:
        print("You selected ", str(choice) + ". ", options[choice])
print("Exiting...")

