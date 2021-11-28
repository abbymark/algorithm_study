import sys
sys.setrecursionlimit(10**6)
def dfs(x, y):
    
    graph[x][y] = 0
    # print(graph)
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        # print('x, y = ', nx, ny, 'dx, dy = ', dx[i], dy[i])
        if nx >= 0 and ny >= 0 and nx < h and ny < w:
            if graph[nx][ny] == 1:
                dfs(nx, ny)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = []

    for i in range(h):
        graph.append(list(map(int, input().split())))
    
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    count = 0
    # breakpoint()
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                count += 1
                dfs(i, j)
    print(count)


