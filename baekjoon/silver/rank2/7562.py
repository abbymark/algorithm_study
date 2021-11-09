from collections import deque

tests = int(input())

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(start, end):
  queue = deque()
  queue.append(start)

  graph[start[0]][start[1]] = 0

  if start[0] == end[0] and start[1] == end[1]:
    print(0)
    return

  while queue:
    x, y = queue.popleft()

    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= side_length or ny >= side_length:
        continue
      
      if graph[nx][ny] != -1:
        continue

      graph[nx][ny] = graph[x][y] + 1

      if nx == end[0] and ny == end[1]:
        print(graph[nx][ny])
        return
      
      queue.append((nx, ny))




for i in range(tests):
  side_length = int(input())

  graph = [[-1 for k in range(side_length)] for j in range(side_length)]

  start = tuple(map(int, input().split()))
  end = tuple(map(int, input().split()))

  bfs(start, end)
