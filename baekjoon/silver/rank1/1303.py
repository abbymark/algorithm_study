m, n = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(input()))

dx = [0 ,0 ,1 ,-1]
dy = [-1, 1, 0, 0]

white_count = []
blue_count = []

def dfs(x, y, color):
  if graph[x][y] != color:
    return

  count = 0
  stack = []
  stack.append((x,y))

  # visited 표시
  graph[x][y] = 0

  # count 늘리기
  count += 1
  while stack:
    x, y = stack.pop()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx >= n or ny >= m or nx < 0 or ny < 0:
        continue

      if graph[nx][ny] == color:
        count += 1
        graph[nx][ny] = 0
        stack.append((nx, ny))

  if color == 'W':
    white_count.append(count)
  else:
    blue_count.append(count)

for i in range(n):
  for j in range(m):
    dfs(i, j, 'B')
    dfs(i, j, 'W')

print(sum(i*i for i in white_count), end=' ')
print(sum(i*i for i in blue_count))



