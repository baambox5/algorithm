import sys
sys.stdin = open('5102.txt', 'r')
from collections import deque

for test_case in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    group = [[] for _ in range(V + 1)]
    visit = [0] * (V + 1)
    dist = [0] * (V + 1)
    for _ in range(E):
        u, v = map(int, input().split())
        group[u].append(v)
        group[v].append(u)
    S, G = map(int, input().split())
    q = deque()
    q.append(S)
    visit[S] = 1
    flag = 1
    while q:
        s = q.popleft()
        if s == G:
            print('#{} {}'.format(test_case, dist[s]))
            flag = 0
            break
        for w in group[s]:
            if not visit[w]:
                visit[w] = 1
                dist[w] = dist[s] + 1
                q.append(w)
    if flag:
        print('#{} {}'.format(test_case, 0))
