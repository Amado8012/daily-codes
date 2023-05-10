import random

nums = [] #empty list
for i in range (0, 9):
    nums.append(random.randrange(0, 100))

print(nums)


nums.sort()
print(nums)

print(nums[8]) #print biggest
print(nums[0])#smallest
print(nums[4])

