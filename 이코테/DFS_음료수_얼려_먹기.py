# 예시 입력
# 4 5
# 00110
# 00011
# 11111
# 00000

from pprint import pprint
from typing import List

# N, M을 공백으로 구분하여 입력받기
N, M = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for _ in range(N):
  graph.append(list(input()))


# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x:int, y: int):
  # 주어진 범위를 벗어나는 경우에는 즉시 종료
  if x < 0 or x >= N or y < 0 or y >= M:
    return False
  
  # 현재 노드를 아직 방문하지 않았다면
  if graph[x][y] == '0':
    # 해당 노드 방문 처리
    graph[x][y] = '1'

    # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y+1)
    dfs(x, y-1)
    return True
  return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(N):
  for j in range(M):
    # 현재 위치에서 DFS 수행
    if dfs(i,j):
      result += 1

print(result)  # 정답 출력