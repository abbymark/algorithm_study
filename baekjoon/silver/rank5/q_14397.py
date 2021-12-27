n, m = map(int, input().split())

graph = []

for i in range(n):
  if i % 2 != 0:
    graph.append([' '] + list(input()))
  else:
    graph.append(list(input()) + [' '])

# 짝수 단위의 행일경우 적용
dxdy_even = [
  [0, 1],  # 우
  [0, -1],  # 좌
  [-1, 0],  # 상
  [-1, 1],  # 상우
  [1, 0],  # 하
  [1, 1],  # 하우
]

# 홀수 단위의 행일경우 적용
dxdy_odd = [
  [0, 1],  # 우
  [0, -1],  # 좌
  [-1, 0],  # 상
  [-1, -1],  # 상좌
  [1, 0],  # 하
  [1, -1],  # 하좌
]

count = 0

for i in range(n):
  for j in range(m+1):
    # 땅일때만 옆에 물인지 확인
    if graph[i][j] == '#':

      if i % 2 == 0:
        for dx, dy in dxdy_even:
          
          # 바운더리 넘어가면 무시
          if i + dx >= 0 and i + dx < n and j + dy >= 0 and j + dy < m+1:
          
            if graph[i+dx][j+dy] == '.':
              # print(i+dx, j+dy)
              count += 1
      else:
        for dx, dy in dxdy_odd:
          
          # 바운더리 넘어가면 무시
          if i + dx >= 0 and i + dx < n and j + dy >= 0 and j + dy < m+1:
          
            if graph[i+dx][j+dy] == '.':
              # print(i+dx, j+dy)
              count += 1
print(count)