import copy
from collections import deque

n = int(input())

graph_ori = []
for i in range(n):
    graph_ori.append(list(map(int, input().split())))

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(x, y, height):
    graph[x][y] = 0
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                if graph[nx][ny] > height:
                    queue.append((nx, ny))
                    graph[nx][ny] = 0


max_count = 0
for i in range(0, 101):
    graph = copy.deepcopy(graph_ori)
    count = 0
    for j in range(n):
        for k in range(n):
            if graph[j][k] > i:
                # print('i, j, k', i, j, k)
                count += 1
                bfs(j, k, i)

    if count > max_count:
        max_count = count
    # elif count < max_count: 이거 쓰면 틀림...
    #     # print(i)
    #     break
print(max_count)

"""
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7
"""