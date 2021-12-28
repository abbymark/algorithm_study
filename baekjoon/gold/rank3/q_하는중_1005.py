import collections
import heapq

T = int(input())

for i in range(T):

    # 건물의 갯수, 건설순서 규칙의 갯수
    N, K = map(int, input().split())

    # 건물 건설에 걸리는 시간
    D = list(map(int, input().split()))

    # 건설순서
    graph = collections.defaultdict(list)
    start_node = 0
    for j in range(K):
        X, Y = map(int, input().split())
        if j == 0:
            start_node = X
        graph[X].append((D[Y-1], Y))
    
    # 목표 건물
    W =int(input())

    max_heap = [(-D[start_node-1], start_node)]

    times = collections.defaultdict(int)

    while max_heap:
        # breakpoint()
        time, node = heapq.heappop(max_heap)
        time = -time
        if node not in times:
            times[node] = time

            for v, w in graph[node]:
                alt = time + v
                heapq.heappush(max_heap, (-alt, w))
        
        if node == W:
            break
    
    print(max(times.values()))


