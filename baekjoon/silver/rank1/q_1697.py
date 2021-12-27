from collections import deque

n, k = map(int, input().split())

distance = [0] * 100001

queue = deque()
queue.append(n)

distance[n] += 1

while queue:
  n = queue.popleft()
  if n == k:
    print(0)
    break

  nn = n - 1
  if nn >= 0 and nn <= 100000 and distance[nn] == 0:
    if nn == k:
      print(distance[n])
      break
    distance[nn] = distance[n] + 1
    queue.append(nn)

  nn = n + 1
  if nn >= 0 and nn <= 100000 and distance[nn] == 0:
    if nn == k:
      print(distance[n])
      break
    distance[nn] = distance[n] + 1
    queue.append(nn)

  nn = n * 2
  if nn >= 0 and nn <= 100000 and distance[nn] == 0:
    if nn == k:
      print(distance[n])
      break
    distance[nn] = distance[n] + 1
    queue.append(nn)