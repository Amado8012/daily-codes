for i in range(-20, 40, 5):
    print(i, end = " ")
 
print() 

for i in range(2):
    for j in  range(5):
        print("*", end = "")
    print()

num = 50
while num >= 0:
    print(num, end = " ")
    num-=10 

print()
choice = "heres a cookie!"
while choice != "yes":
    print(choice)
    choice = input("do you want another one?:")

print("here take another cookie. goodbye")