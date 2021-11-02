import math

nums = input()

count = 0
for i in range(len(nums)-1):
  if nums[i] != nums[i+1]:
    count += 1
print(math.ceil(count /2))