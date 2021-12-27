n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(input()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

near_wolf = False

for i in range(n):
  for j in range(m):
    if graph[i][j] == 'S':
      for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
          continue
        
        if graph[nx][ny] == 'W':
          near_wolf = True
          break
    if near_wolf:
      break
  if near_wolf:
    break

if near_wolf:
  print(0)
else:
  print(1)
  for i in range(n):
    for j in range(m):
      if graph[i][j] == '.':
        print('D', end='')
      else:
        print(graph[i][j], end='')
    print()
