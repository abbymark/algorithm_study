from collections import deque
import copy

n, m = map(int, input().split())

graph = []
for i in range(n):
  line = list(map(int, input()))
  new_line = [-1 if j == 1 else 0 for j in line]
  graph.append(new_line)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

path_distance = []

def bfs(x, y):
  if n == 1 and m == 1 and graph[0][0] == 0:
    path_distance.append(1)
    return

  queue = deque()
  queue.append((x, y, 1))
  graph[x][y] = 1
  block_visited[x][y] = 1

  while(queue):
    x, y, block_avail = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      block = block_avail

      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue

      if block == 1 and graph[nx][ny] == -1:
        # 돌파력이 1이고 벽이면 돌파 사용
        block = 0
        block_visited[nx][ny] = graph[x][y] + 1
      elif graph[nx][ny] != 0 and block == 1:
        # 돌파력이 1이고 지나간곳이면 넘김
        continue
      elif block_visited[nx][ny] != 0 and block == 0:
        continue
      elif block == 1:
        # 돌파를 쓰지 않았을때는 그냥맵, 돌파맵 둘다 업데이트 해준다.
        graph[nx][ny] = graph[x][y] + 1
        block_visited[nx][ny] = block_visited[x][y] + 1
      elif block == 0:
        block_visited[nx][ny] = block_visited[x][y] + 1

      if nx == n-1 and ny == m-1 and block == 1:
        path_distance.append(graph[nx][ny])
      elif nx == n-1 and ny == m-1 and block == 0:
        path_distance.append(block_visited[nx][ny])

      # breakpoint()
      queue.append((nx, ny, block))

# for i in range(n):
#   for j in range(m):
#     temp = copy.deepcopy(graph)
#     temp[i][j] = 0

block_visited = copy.deepcopy(graph)

bfs(0, 0)

if len(path_distance) == 0:
  print(-1)
else:
  print(min(path_distance))

"""
6 4
0000
1110
0000
0001
0111
0000

5 4
0001
1101
0001
0111
0010
"""