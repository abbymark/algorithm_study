import copy

n = int(input())

graph = []
for i in range(n):
    graph.append(list(input()))

graph_RG = copy.deepcopy(graph)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x,y, graph):
    stack= []
    stack.append((x,y))

    while stack:
        x, y = stack.pop()
        color = graph[x][y]
        graph[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >=0 and ny >= 0 and nx < n and ny < n:
                if graph[nx][ny] != 0 and graph[nx][ny] == color:
                    stack.append((nx, ny))

count = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            dfs(i, j, graph)
            count += 1
print(count, end=' ')

for i in range(n):
    for j in range(n):
        if graph_RG[i][j] == 'G':
            graph_RG[i][j]='R'

count = 0
for i in range(n):
    for j in range(n):
        if graph_RG[i][j] != 0:
            dfs(i, j, graph_RG)
            count += 1
print(count)


