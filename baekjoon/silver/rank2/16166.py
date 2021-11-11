from collections import deque
import copy

n = int(input())

graph_ori = []

for i in range(n):
  graph_ori.append(list(set(list(map(int, input().split()))[1:])))

goal = int(input())

ans = []

def bfs(x, y):
  if goal in graph[x]:
    ans.append(0)
    return

  queue = deque()
  queue.append((x, y, 0))

  while queue:
    x, y, count = queue.popleft()
    # breakpoint()
    if graph[x][y] == -1:
      continue
    
    for j in range(len(graph[x])):
      for i in range(len(graph)):
        if i == x:
          continue
        if graph[x][j] in graph[i]:

          # 도착역이 해당 호선에 있을경우
          if goal in graph[i]:
            ans.append(count+1)
            return
        
          queue.append((i, graph[i].index(graph[x][j]), count+1))
          
      # 지나간곳 처리
      graph[x][j] = -1

for i in range(len(graph_ori)):
  for j in range(len(graph_ori[i])):
    if graph_ori[i][j] == 0:
      graph = copy.deepcopy(graph_ori)
      bfs(i, j)

if len(ans) == 0:
  print(-1)
else:
  print(min(ans))

"""
5
7 12 1 2 3 1 12 8
2 12 13
7 13 0 9 4 99 99 13
6 13 8 10 7 99 13
2 13 22
22
1

3
1 0
2 0 3
2 3 8
8
1
"""