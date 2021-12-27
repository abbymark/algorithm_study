n, m = list(map(int, input().split()))

grid = []
for i in range(n):
    row = input()
    grid.append(list(row))

count = 0
def recursion(pos, prev):
    global count
    x, y = pos

    if y >= n or x >= m or grid[y][x] == '0' or grid[y][x] != prev:
        count += 1
        return

    if grid[y][x] == '-':
        grid[y][x] = '0'
        recursion([x+1, y], prev)

    if grid[y][x] == '|':
        grid[y][x] = '0'
        recursion([x, y+1], prev)
    
    if x+1 < m and grid[y][x+1] != '0':
        recursion([y, x+1], grid[y][x+1])
    if y+1 < n and grid[y+1][x] != '0':
        recursion([y+1, x], grid[y+1][x])

prev = grid[0][0]

recursion([0,0], prev)
print(count)



