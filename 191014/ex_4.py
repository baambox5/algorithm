# BFS 간선 완화
from collections import deque

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))
D = [0xffffff] * (V + 1)
def BFS(s):
    Q = deque()
    D[s] = 0
    Q.append(s)
    while Q:
        u = Q.popleft()
        for v, w in G[u]:
            if D[v] > D[u] + w:
                D[v] = D[u] + w
                Q.append(v)

BFS(1)


# dijkstra
def dijkstra(s):
    D = [0xffffff] * (V + 1)
    D[s] = 0
    cnt = V
    visit = [False] * (V + 1)
    while cnt:
        u, MIN = 0, 0xffffff
        for i in range(1, V + 1):
            if not visit[i] and MIN > D[i]:
                u, MIN = i, D[i]
        visit[u] = True
        for v, w in G[u]:
            if D[v] > D[u] + w:
                D[v] = D[u] + w
        cnt -= 1
