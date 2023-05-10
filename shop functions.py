def Shop(money):
    choice = "frogs"
    while choice != "quit":
        print("1 to buy potion, 2 to buy cupcake, 3 to buy sword,type quit yo quit.")
        choice = input("enter your choice:")
        if choice == 1:
            print("you bought a potion!")
        elif choice == 2:
            print("you bouight a cupcake!")
        elif choice == 3:
            print("you bought a sword!")
        elif choice == "quit":
            print("thanks for stopping by!")
        else:
            print("sorry i don't understand")

room = 1
choice = "frogs"
while choice != "quit":
    if room == 1:
        choice = input("you are in room 1, you can go west")
        if choice == "west":
            room = 2 
    if room == 2: 
        choice = input("you are in room 2, you can go east or go to the shop")
        if choice == "east":
            room = 1
        if choice == "shop":
            Shop(100) 
