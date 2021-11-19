n, m = map(int, input().split())

x, y, dir = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 방향 돌리기
def turn_dir(dir):
    dir -= 1
    if dir == -1:
        dir = 3
    return dir

count = 0
break_flag = False
final_break = False
while True:
    # 현재 자리 청소하기
    if graph[x][y] == 0:
        graph[x][y] = -1
        count += 1
    
    while True:
        for i in range(4):
            dir = turn_dir(dir)
            is_in_min_x = x + dx[dir] >= 0
            is_in_max_x = x + dx[dir] < n
            is_in_min_y = y + dy[dir] >= 0
            is_in_max_y = y + dy[dir] < n 
            # 청소할 자리가 남아있으면
            if is_in_max_x and is_in_min_x and is_in_max_y and is_in_min_y and graph[x + dx[dir]][y + dy[dir]] == 0:
                x = x + dx[dir]
                y = y + dy[dir]
                break_flag = True
                break
        if break_flag:
            break_flag = False
            break
        
        is_in_min_x = x - dx[dir] >= 0
        is_in_max_x = x - dx[dir] < n
        is_in_min_y = y - dy[dir] >= 0
        is_in_max_y = y - dy[dir] < n 
        # 후진
        if is_in_max_x and is_in_min_x and is_in_max_y and is_in_min_y and graph[x - dx[dir]][y - dy[dir]] != 1:
            x = x - dx[dir]
            y = y - dy[dir]
        # 후진 못할시 끝
        else:
            final_break = True
            break
    if final_break:
        break

print(count)



"""
8 10
0 0 0
0 1 1 1 0 1 0 0 0 1
0 0 0 0 0 1 0 0 0 1
0 1 0 0 1 0 1 0 0 0
1 1 1 0 1 1 1 0 0 1
1 0 1 1 0 1 0 0 0 1
1 0 0 0 0 1 1 0 0 0
0 0 0 1 1 1 0 1 0 1
0 1 1 1 1 0 1 0 0 0
9

5 5
0 0 0
0 1 0 1 0
0 1 0 1 1
0 0 0 1 0
0 1 1 1 0
1 1 0 1 0
7

11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
"""
