N = int(input())
graph = []

for i in range(N):
    graph.append(input())

max_count = 0

for i in range(N):
    count = 1
    for j in range(N-1):
        if graph[i][j] == graph[i][j+1]:
