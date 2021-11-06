food_times = list(map(int, input().split()))
k = int(input())

count = 0
result = 0
element_to_decrease =0
while k != 0:

  element_to_decrease = count%len(food_times)
  if food_times[element_to_decrease] > 0:
    food_times[element_to_decrease] -= 1
    count += 1
  else:
    count += 1
    continue

  k -= 1

  element_to_decrease = count%len(food_times)

  result = element_to_decrease+1

print(result)