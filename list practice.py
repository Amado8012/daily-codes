colors = ["blue", "red", "teal", "magenta", "green"] #a list in python 
print(colors[0]) #print 3
print(colors[2]) #prints "teal"
print(colors[4])  #reoresents slot #4 with false 
colors.append("purple") #adds an item to the end of the list 
print(colors) #prints the wgole list 

num = [583, 548, 500, 625]
sum = 0 
for i in range(len(num)):
    sum  += num[i] 

print("all paychecks:", sum)#print totak


foods = []
num = int(input(" what is the number of types of foods they want to pack on their trip to Mars."))
for i in range(num): 
    stuff = input("enter food")
    foods.append(stuff)
print(foods)
#set up empty square brackets
#ask for a number and store 
#for loop to walk through list (use the number you just got)
#get more user input
#use the append function to add it to the list
#print it out
