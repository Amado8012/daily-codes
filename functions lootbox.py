import random
item = []

def itemDropper():
    num = random.randrange(1, 100)
    if num < 25:
        item[3]="potion"
        print("you got a potion")

    if num < 50:
        item.append("sock")
        print("you got a sock")
    if num < 60:
        item.append("coin")
        print("you got a coin")

    else: 
        print("no item dropped")

    print("your inventory:", item)

while(1):
    itemDropper()
    input()
