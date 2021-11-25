# n = int(input())

# graph = []

# for i in range(n):
#     graph.append(list(input()))

# # visited = [False] * len(graph)

# max_friend = 0

# def dfs(node, depth):
#     count = 0
    
#     # 갔던곳 체크
#     visited[node] = True
    
#     # 깊이 체크
#     if depth == 2:
#         return 0


#     for i, YN in enumerate(graph[node]):
#         if YN == 'Y' and visited[i] == False:
#             count += 1
#             count += dfs(i, depth + 1)
    
#     return count

# for i in range(len(graph)):
#     visited = [False] * len(graph)
#     count = dfs(i, 0)
#     if count > max_friend:
#         max_friend = count

# print(max_friend)


"""
6
NYYNYN
YNYNNN
YYNYNN
NNYNNN
YNNNNY
NNNNYN    
5

"""

n = int(input())

graph = []

for i in range(n):
    graph.append(list(input()))

max_friend = 0
for i in range(len(graph)):
    count = 0
    near_friend = []
    second_friend = []
    for j in range(len(graph[i])):
        if graph[i][j] == 'Y':
            count += 1
            near_friend.append(j)

    for j in near_friend:
        for k in range(len(graph[j])):
            if graph[j][k] == 'Y' and k != i and k not in near_friend and k not in second_friend:
                count += 1
                second_friend.append(k)

    if count > max_friend:
        max_friend = count

print(max_friend)
