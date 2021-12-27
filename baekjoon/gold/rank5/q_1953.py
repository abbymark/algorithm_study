from collections import deque

n = int(input())

graph = [[] for i in range(n+1)]

blue = []
white = []

for i in range(n):
  person_info = list(map(int, input().split()))
  # breakpoint()
  if person_info[0] == 0:
    continue
  for j in range(person_info[0]):
    graph[i+1].append(person_info[j + 1])

def bfs(node, hates):
  if node == 0:
    return
  
  
  # 이미 팀에 속해있으면 넘긴다.
  if node in blue or node in white:
    return

  queue = deque()
  queue.extend(hates)
  
  if len(blue) == 0:
    blue.append(node)
  elif len(white) == 0:
    white.append(node)
  else:
    blue.append(node)
  # breakpoint()
  while queue:
    node = queue.popleft()

    if node in blue or node in white:
      continue
    
    is_hate_exist= False
    for hate in graph[node]:
      if hate in blue:
        white.append(node)
        queue.extend(graph[node])
        is_hate_exist =True
        break
      elif hate in white:
        blue.append(node)
        queue.extend(graph[node])
        is_hate_exist = True
        break
    
    if is_hate_exist:
      continue

    blue.append(node)
    queue.extend(graph[node])


for i in range(len(graph)):
  bfs(i, graph[i])

print(len(blue))
for node in sorted(blue):
  print(node, end=' ')

print()

print(len(white))
for node in sorted(white):
  print(node, end=' ')