import copy

n, m = map(int, input().split())

graph_ori = [[[], 0] for i in range(n+1)]

for i in range(m):
  a, b = map(int, input().split())

  graph_ori[b][0].append(a)

counts = []

def dfs(n):
  stack = []
  stack.append(n)
  # breakpoint()
  count  = 0
  while stack:
    x = stack.pop()
    if graph[x][1] == 1:
      continue
    graph[x][1] = 1
    count += 1
    for node in graph[x][0]:
      if graph[node][1] != 1:
        stack.append(node)
  
  counts.append((n, count))

for i in range(m):
  graph = copy.deepcopy(graph_ori)
  dfs(i)

counts = sorted(counts, key=lambda x: (-x[1], x[0]))


max_count = counts[0][1]
for count in counts:
  if count[1] == max_count:
    print(count[0], end= ' ')
  else:
    break