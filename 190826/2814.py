import sys
sys.stdin = open('2814.txt', 'r')
# from collections import deque
#
# for test_case in range(1, int(input()) + 1):
#     N, M = map(int, input().split())
#     G = [[] for _ in range(N + 1)]
#     for _ in range(M):
#         u, v = map(int, input().split())
#         G[u].append(v)
#         G[v].append(u)
#     max_count = 1
#     for start in range(1, N + 1):
#         visit = [0] * (N + 1)
#         D = [0] * (N + 1)
#         D[start] = 1
#         visit[start] = 1
#         Q = deque()
#         Q.append(start)
#         while Q:
#             x = Q.popleft()
#             for w in G[x]:
#                 if not visit[w]:
#                     visit[w] = 1
#                     D[w] = D[x] + 1
#                     Q.append(w)
#         for count in D:
#             if count > max_count:
#                 max_count = count
#     print('#{} {}'.format(test_case, max_count))


def dfs(s):
    for w in G[s]:
        if not visit[w]:
            D[w] = D[s] + 1
            visit[w] = 1
            dfs(w)


for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    max_count = 1

    for start in range(1, N + 1):
        visit = [0] * (N + 1)
        D = [0] * (N + 1)
        D[start] = 1
        visit[start] = 1
        dfs(start)
        for count in D:
            if count > max_count:
                max_count = count
    print('#{} {}'.format(test_case, max_count))
