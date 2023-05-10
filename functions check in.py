import random
Monster = []

def MonsterGen(): 
    num = random.randrange(1,100)
    if num < 20:
        Monster.append("Skelition")
        print("a Skeltion appered!")
    
    if num < 50:
        Monster.append("Zombie")
        print("a Zombie appered!")
    
    if num < 60:
         Monster.append("Witch")
         print("a Witch appered!")

    else:
        print("no Monsters appered")

while(1):
    MonsterGen()
    input()