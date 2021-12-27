from collections import deque

m, n = map(int, input().split())

graph = []

for i in range(n):
  graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
  queue = deque()
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 1:
        queue.append((i, j))
  
  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue

      if graph[nx][ny] == 0:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
    
  return
      
bfs()
max_day = 0
not_complete = False
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      not_complete = True
      break
    if graph[i][j] > max_day:
      max_day = graph[i][j]
  if not_complete:
    break

if not_complete:
  print(-1)
else:
  print(max_day-1)