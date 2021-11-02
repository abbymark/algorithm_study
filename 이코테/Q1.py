N = int(input())
scary_scores = list(map(int, input().split()))
scary_scores.sort()

count = 0
start = 0
current = 0
max = len(scary_scores)
while True:
  start = scary_scores[start]
  current += start
  if max > current:
    count += 1
  else:
    break

print(count)