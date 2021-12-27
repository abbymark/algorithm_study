from collections import deque

n = int(input())
stones = list(map(int, input().split()))
a, b = map(int, input().split())

count = 0
def bfs(x):
  global count
  queue = deque()
  queue.append(x)

  while queue:
    x = queue.popleft()
    count += 1


    jump_len = stones[x]

    x_pos = x
    x_neg = x

    if count > n:
      return

    while True:
      if x_pos + jump_len >= n:
        break
      queue.append(x_pos + jump_len)
      x_pos += jump_len

      if x_pos == b - 1:
        return True
    
    while True:
      if x_neg - jump_len < 0:
        break
      queue.append(x_neg - jump_len)
      x_neg -= jump_len

      if x_neg == b - 1:
        return True


if bfs(a-1):
  print(count)
else:
  print(-1)