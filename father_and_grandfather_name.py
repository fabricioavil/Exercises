names = {"a":"b", "b":"c", "c":"d", "d":"e", "e":"f"}
choice = None

while choice != "0":
    print(
    """
    Father and Grandfather's name
    
    1 - Look up a father's name
    2 - Look up a grandfather's name
    0 - Quit
    """
    )
    
    choice = input("Choice: ")

    if choice == "1":
        name = input("What is your name? ")
        if name in names:
            father = names[name]
            print("\n", name, "'s father is ", father, "." ,sep='')
        else:
            print("\nSorry, I don't know", name)

    if choice == "2":
        name = input("What is your name? ")
        if name in names:
            father = names[name]
            grandfather = names[father]
            print("\n", name, "'s grandfather is ", grandfather, "." ,sep='')
        else:
            print("\nSorry, I don't know", name)

input("\n\nPress the enter key to exit.")