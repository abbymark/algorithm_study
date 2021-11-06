# 입력 예제
# 3
# 1 1 10
# 1 5 1
# 2 2 -1

from collections import deque

n = int(input())

graph = []

for i in range(n):
  graph.append(list(map(int, input().split())))

dx = [1, 0]
dy = [0, 1]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()

    # 현재 위치에서 아래, 오른쪽으로 위치 확인
    for i in range(2):
      if graph[x][y] == 0:
        print('Hing')
        return

      nx = x + graph[x][y] * dx[i]
      ny = y + graph[x][y] * dy[i]

      # 판을 넘어가는 경우
      if nx >= n or ny >= n:
        continue
      
      if nx == n-1 and ny == n-1:
        print('HaruHaru')
        return
      
      queue.append((nx, ny))
  
  print('Hing')
  return

bfs(0, 0)

