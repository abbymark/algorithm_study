n = int(input())

votes = []
for i in range(n):
  votes.append(int(input()))

count = 0
while True:
  is_not_max = False

  for i in range(1, n):
    if votes[i] >= votes[0]:
      is_not_max = True

    if votes[i] == max(votes):
      votes[i] -= 1
      votes[0] += 1
      count += 1
      break
  
  if not is_not_max:
    break

print(count)