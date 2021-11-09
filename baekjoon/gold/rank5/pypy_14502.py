from collections import deque
import copy

n, m = map(int, input().split())

graph = []

safe_area = []

for i in range(n):
  graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
  queue = deque()
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 2:
        queue.append((i, j))
  
  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue

      if temp[nx][ny] != 0:
        continue

      temp[nx][ny] = 2

      queue.append((nx, ny))
  
  count = 0
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        count += 1
  safe_area.append(count)
  return


for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      graph[i][j] = 1

      for k in range(n):
        for l in range(m):
          if graph[k][l] == 0:
            graph[k][l] = 1

            for o in range(n):
              for p in range(m):
                if graph[o][p] == 0:
                  graph[o][p] = 1
                  temp = copy.deepcopy(graph)
                  bfs()
                  graph[o][p] = 0
            graph[k][l] = 0
      graph[i][j] = 0

print(max(safe_area))