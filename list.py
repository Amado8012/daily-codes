room = 1 

while True:
    if room == 1:
        choice = input("you are in room1, you can go south")
        if choice == "south":
            room = 2
    if room == 2:
        if inventory[0]!="key": 
            print("you see a key on the floor")
        choice = input("you are in room 2, you can go south or noeth")
        if choice == "south":
            room = 3
        if choice == "north":
            room = 1
    if room == 3:
        choice = input("you are in room1, you can go east or north")
        if choice == "east":
            room = 4
        if choice == "north":
            room = 2
    if room == 4:
        choice = input("you are in room1, you can go west")
        if choice == "west":
            room = 3