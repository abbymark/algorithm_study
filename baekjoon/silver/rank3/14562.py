from collections import deque
import copy

c = int(input())

graph = [0] * 130

def bfs(s, t):
  queue = deque()
  queue.append((s, t, 0))

  if s == t:
    return 0
  
  while queue:
    s, t, count = queue.popleft()
    if s <= t and temp[s] == 0:
      queue.append((s + 1, t, count + 1))
      queue.append((s * 2, t + 3, count + 1))
      if s == t:
        return count


for i in range(c):
  s, t = map(int, input().split())
  temp = copy.deepcopy(graph)
  print(bfs(s, t))
