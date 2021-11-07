from collections import deque

n = int(input())
target1, target2 = map(int, input().split())
m = int(input())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [-1] * (n+1)

for i in range(m):
  parent, child = map(int, input().split())
  graph[parent].append(child)
  graph[child].append(parent)


break_while = False
def bfs(start):
  global break_while
  queue = deque()
  queue.append(start)

  visited[start] = True
  distance[start] = 0

  while queue:
    v = queue.popleft()

    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
        distance[i] = distance[v] + 1
      
      if i == target2:
        break_while = True
        print(distance[i])
        break
    
    if break_while:
      break

bfs(target1)
if not break_while:
  print(-1)

# print(visited, count)