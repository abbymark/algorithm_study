import sys
sys.setrecursionlimit(10**6)

n, r, c = map(int, input().split())

graph = []
for i in range(2**n):
    graph.append([-1] * (2**n))

count = 0
def recursion(h_start, h_end, w_start, w_end):
    # breakpoint()
    global count
    # 길이가 1일때 처리
    if  h_end - h_start == 1 and w_end - w_start == 1:
        graph[h_start][w_start] = count
        count += 1
        graph[h_start][w_end] = count
        count += 1
        graph[h_end][w_start] = count
        count += 1
        graph[h_end][w_end] = count
        count += 1
        # print(graph)
        return

    recursion(h_start, (h_start+h_end)//2, w_start, (w_start+w_end)//2)
    recursion(h_start, (h_start+h_end)//2, (w_start+w_end)//2 +1, w_end)
    recursion((h_start+h_end)//2+1, h_end, w_start, (w_start+w_end)//2)
    recursion((h_start+h_end)//2+1, h_end, (w_start+w_end)//2+1, w_end)

recursion(0, len(graph)-1, 0, len(graph)-1)
# for row in graph:
#     print(row)
print(graph[r][c])