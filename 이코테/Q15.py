from collections import deque

CITYS, ROADS, DISTANCE, START = map(int, input().split())

graph = [[] for _ in range(CITYS + 1)]

for i in range(ROADS):
  city1, city2 = map(int, input().split())
  graph[city1].append(city2)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (CITYS + 1)
distance[START] = 0  # 출발 도시까지의 거리는 0으로 설정

# 너비우선 탐색(BFS) 수행
def bfs(city: int):
  queue = deque()
  queue.append(city)

  while queue:
    current_city = queue.popleft()

    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[current_city]:
      # 아직 방문하지 않은 도시라면
      if distance[next_node] == -1:
        # 최단 거리 갱신
        distance[next_node] = distance[current_city] + 1
        queue.append(next_node)

bfs(START)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, CITYS + 1):
  if distance[i] == DISTANCE:
    print(i)
    check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
  print(-1)


