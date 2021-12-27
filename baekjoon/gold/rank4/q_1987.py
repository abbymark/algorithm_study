from collections import deque
import copy

r, c = map(int, input().split())

graph = []

for i in range(r):
    graph.append(list(input()))

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(x, y):
    memory = ''
    queue = set()
    memory += graph[x][y]
    queue.add((x, y, memory))
    max_count = 1

    while queue:
        x, y, memory = queue.pop()
        
        for i in range(4):
            memory_store = memory[:]
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and ny >= 0 and nx < r and ny < c:
                if graph[nx][ny] != 0 and graph[nx][ny] not in memory_store:
                    memory_store += graph[nx][ny]
                    queue.add((nx, ny, memory_store))
                    if len(memory_store) > max_count:
                        max_count = len(memory_store)
    print(max_count)

bfs(0, 0)
'''
10 10
ASWERHGCFH
QWERHDLKDG
ZKFOWOHKRK
SALTPWOKSS
BMDLKLKDKF
ALSKEMFLFQ
GMHMBPTIYU
DMNKJZKQLF
HKFKGLKEOL
OTOJKNKRMW

3 4
ABCD
BCDA
CDEF

2 2
AB
CA

20 20
POIUYTREWQBWKALSLDLG
LKJHGFDSAMASFBMBOSOZ
NMBVCXZAKPAISJLBMROW
CEVTBFNIMLASNCVKNDKX
VPQLBKENMSAHBBLFOWPQ
ZLSKJJBNBEASZNFDGHHN
GPBMDLQDALAASBBXCEGA
APQIKBMROIBANPOBLMKS
ASKSKVJRPORHNOXZKSPN
LSNVOEOOOKAKANLGKOAX
AKVMBOTOWPQOJBSMSPEP
BLLBKWPEPBKNMROSALLP
BNQLDNBMKOVMEMELSLMA
RLEPQQPVKJRNBITNBSAS
ZXMCOITRPWKLPGKHNGMS
QOBKRPPPZSLEMPNKSPPR
OQJDNZNANDWKQKVJEOGJ
QUYVOIUYWERLKJHASDFV
ZCVWRETPOIUHJKLVBMAS
QWERZCVUIAFDKHSDFHSA
'''