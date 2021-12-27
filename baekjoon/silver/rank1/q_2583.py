m, n, k = map(int, input().split())

graph = []
for i in range(m):
    graph.append([0] * n)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

areas = []
def dfs(x, y, count):
    if graph[x][y] == 0:
        graph[x][y] = 1
        count += 1
        area.append(count)
    else:
        return 

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx < m and ny < n:
            dfs(nx,ny, count)
    

recs = []
for i in range(k):
    recs.append(list(map(int, input().split())))


for i in range(m):
    for j in range(n):
        for rec in recs:
            if j >= rec[0] and j < rec[2]-1 and i >= rec[1] and i < rec[3]-1:
                graph[i][j] = -1

for row in graph:
    print(row)

for i in range(m):
    for j in range(n):
        area = []
        dfs(i, j, 0)
        if area:
            areas.append(max(area))
print(areas)