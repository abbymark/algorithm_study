from typing import List
import collections

def findItinerary(tickets: List[List[str]]) -> List[str]:
    adj = {src: [] for src, dst in tickets}

    tickets.sort()
    for src, dst in tickets:
        adj[src].append(dst)

    result = ['JFK']
    def dfs(src):
        if len(result) == len(tickets) + 1:
            return True
        if src not in adj:
            return False
        
        temp = list(adj[src])
        for i, v in enumerate(temp):
            adj[src].pop(i)
            result.append(v)

            if dfs(v): return True

            adj[src].insert(i, v)
            result.pop()
        return False

    dfs("JFK")

    return result


def findItinerary(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)

    for a, b in sorted(tickets):
        graph[a].append(b)

    route = []
    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)
    
    dfs('JFK')
    print(route)
    return route[::-1]
    
print(findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
print(findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))