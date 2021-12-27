from collections import deque
import copy

n, m = map(int, input().split())

graph = []

for i in range(n):
  graph.append(list(input()))


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

distances = []

def bfs(x, y):
  queue = deque()
  queue.append((x, y))

  if graph[x][y] == 'W':
    return

  temp = copy.deepcopy(graph)
  temp[x][y] = 0

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue

      if temp[nx][ny] == 'W':
        continue
      
      if temp[nx][ny] == 'L':
        temp[nx][ny] = temp[x][y] + 1
        distances.append(temp[nx][ny])
        queue.append((nx, ny))
  return

for i in range(n):
  for j in range(m):
    bfs(i, j)

print(max(distances))
