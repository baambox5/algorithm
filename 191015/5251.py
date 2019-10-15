import sys
sys.stdin = open('5251.txt', 'r')


from queue import PriorityQueue

for test_case in range(1, int(input()) + 1):
    N, E = map(int, input().split())
    G = [[] * (N + 1) for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        G[s].append((e, w))
    D = [0xffff] * (N + 1)
    D[0] = 0
    Q = PriorityQueue()
    Q.put((0, 0))
    while not Q.empty():
        w, u = Q.get()
        if w > D[u]: continue
        for v, weight in G[u]:
            if D[v] > D[u] + weight:
                D[v] = D[u] + weight
                Q.put((D[v], v))
    print('#{} {}'.format(test_case, D[N]))


# BFS
# from collections import deque
#
# for test_case in range(1, int(input()) + 1):
#     N, E = map(int, input().split())
#     G = [[] * N for _ in range(N + 1)]
#     for _ in range(E):
#         s, e, w = map(int, input().split())
#         G[s].append((e, w))
#     min_weight = 0xfffff
#     Q = deque()
#     D = [0xfffff] * (N + 1)
#     D[0] = 0
#     Q.append(0)
#     while Q:
#         u = Q.popleft()
#         for v, weight in G[u]:
#             if D[v] > D[u] + weight:
#                 D[v] = D[u] + weight
#                 Q.append(v)
#     print('#{} {}'.format(test_case, D[N]))
