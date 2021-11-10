graph = []
for i in range(19):
  graph.append(list(map(int, input().split())))

graph = list(map(list, zip(*graph)))

dx = [0, 1, 1, 1, 0]
dy = [1, 1, 0, -1, -1]

def search(x, y):
  color = graph[x][y]
  # breakpoint()
  for i in range(5):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 0 or ny < 0 or nx >= 19 or ny >= 19:
      continue
    
    if color == graph[nx][ny]:

      count = 2
      for j in range(2, 6):
        nnx = x + dx[i] * j
        nny = y + dy[i] * j
        
        if j == 5:
          if count == 5:

            back_x = x - dx[i]
            back_y = y - dy[i]
            if not(back_x < 0 or back_y < 0 or back_x >= 19 or back_y >= 19):
              if color == graph[back_x][back_y]:
                break

            if nnx < 0 or nny < 0 or nnx >= 19 or nny >= 19:
              print(color)
              print(y+1, x+1)
              return True
            if color == graph[nnx][nny]:
              break
            print(color)
            print(y+1, x+1)
            return True

        if nnx < 0 or nny < 0 or nnx >= 19 or nny >= 19:
          break

        if color == graph[nnx][nny]:
          count += 1

flag = False
for i in range(19):
  for j in range(19):
    if graph[i][j] == 1 or graph[i][j] == 2:
      flag = search(i, j)
    
    if flag:
      break
  if flag:
    break

if not flag:
  print(0)
  """
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 1 2 0 0 2 2 2 1 0 0 0 0 0 0 0 0 0 0
0 0 1 2 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 2 2 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 2 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
  """