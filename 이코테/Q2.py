nums = input()

result = 0
for i, num in enumerate(nums):
  num = int(num)
  
  if num == 1 or num==0 or result == 0:
    result += num
  else:
    result *= num


print(result)