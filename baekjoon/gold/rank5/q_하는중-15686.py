from collections import deque
import copy

n, m = map(int, input().split())

graph = []

for i in range(n):
  graph.append(list(map(int, input().split())))

houses = []  # ((house_x, house_y), (chicken_x, chicken_y), distance)
chickens = {}  # (chicken_x, chicken_y): total_distance

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def house_to_chicken_distance(x, y):
  for i in range(n):
    for j in range(n):
      if graph[i][j] == 2:
        houses.append(((x, y), (i, j), abs(i - x) + abs(j - y)))



# 각 집마다 각 치킨집에 대한 거리를 구한다.
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      house_to_chicken_distance(i, j)

# 각 치킨빋은 집들로 부터의 거리합을 갖는다.
for house in houses:
  if house[1] not in chickens:
    chickens[house[1]] = house[2]
  else:
    chickens[house[1]] += house[2]

# 생존 가능 치킨집 수가 현 치킨집보다 작으면 치킨거리의 함이 큰 치킨집부터 없엔다.
if m < len(chickens):
  # dictionary 정렬
  chickens = dict(sorted(chickens.items(), key=lambda item: item[1], reverse=True))

  # 치킨집 제거
  for i in range(len(chickens) - m):
    # breakpoint()
    chicken_loc = next(iter(chickens))
    distance = chickens.pop(next(iter(chickens)))
    graph[chicken_loc[0]][chicken_loc[1]] = 0

# 다시 각 집에서 최소 치킨 거리를 구한다.
houses = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      house_to_chicken_distance(i, j)

# 치킨거리를 구한다.
chicken_dist = {}  # (house_x, house_y), distance
for house in houses:
  if house[0] not in chicken_dist:
    chicken_dist[house[0]] = house[2]
  else:
    if house[2] < chicken_dist[house[0]]:
      chicken_dist[house[0]] = house[2]

print(chicken_dist)

print(sum(chicken_dist.values()))