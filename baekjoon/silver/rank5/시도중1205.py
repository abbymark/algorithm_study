import sys
n, new_score, p = map(int, input().split())

def solution():
  for i in range(n):
    if new_score >= scores[i]:
      scores.insert(i, new_score)
      break

  index = len(scores) - 1 - scores[::-1].index(new_score) + 1

  if index > p:
    print(-1)
  else:
    print(scores.index(new_score) + 1)

if n == 0:
  print(1)
else:
  scores = list(map(int, input().split()))
  solution()

