from collections import deque

m, n, h = map(int, input().split())

graph = []

for i in range(h):
  temp = []

  for j in range(n):
    temp.append(list(map(int, input().split())))
  
  graph.append(temp)


dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
  queue = deque()

  for i in range(h):
    for j in range(n):
      for k in range(m):
        if graph[i][j][k] == 1:
          queue.append((i, j, k))
  
  while queue:
    x, y, z = queue.popleft()

    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]

      if nx < 0 or ny < 0 or nz < 0 or nx >= h or ny >= n or nz >= m:
        continue

      if graph[nx][ny][nz] == 0:
        graph[nx][ny][nz] = graph[x][y][z] + 1
        queue.append((nx, ny, nz))
  
bfs()
is_complete = True
max_day = 0
for i in range(h):
  for j in range(n):
    for k in range(m):
      if graph[i][j][k] == 0:
        is_complete = False
      if graph[i][j][k] > max_day:
        max_day = graph[i][j][k]

if not is_complete:
  print(-1)
else:
  print(max_day - 1)
