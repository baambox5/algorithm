import sys
sys.stdin = open('sangwon_birth.txt', 'r')
from collections import deque

for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    count = 0
    visit = [False] * (N + 1)
    Q = deque()
    visit[1] = True
    Q.append((1, 0))
    while Q:
        u, k = Q.popleft()
        if k >= 2:
            break
        for w in G[u]:
            if not visit[w]:
                visit[w] = True
                Q.append((w, k + 1))
                count += 1
    print('#{} {}'.format(test_case, count))
