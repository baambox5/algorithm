import sys
sys.stdin = open('1260.txt', 'r')
from collections import deque


def dfs(s):
    visit[s] = 1
    print(s, end=' ')
    for w in G[s]:
        if not visit[w]:
            dfs(w)

for _ in range(1, 4):
    N, M, start = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    visit = [0] * (N + 1)
    for _ in range(M):
        n, m = map(int, input().split())
        tmp = m
        for i in range(len(G[n])):
            if tmp < G[n][i]:
                G[n][i], tmp = tmp, G[n][i]
        else:
            G[n].append(tmp)
        tmp = n
        for i in range(len(G[m])):
            if tmp < G[m][i]:
                G[m][i], tmp = tmp, G[m][i]
        else:
            G[m].append(tmp)
    dfs(start)
    print()
    visit = [0] * (N + 1)
    Q = deque()
    visit[start] = 1
    print(start, end=' ')
    Q.append(start)
    while Q:
        v = Q.popleft()
        for w in G[v]:
            if not visit[w]:
                visit[w] = 1
                print(w, end=' ')
                Q.append(w)
    print()



