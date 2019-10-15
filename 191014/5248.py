import sys
sys.stdin = open('5248.txt', 'r')


# def dfs(n):
#     visit[n] = True
#     for w in G[n]:
#         if not visit[w]:
#             dfs(w)
#
#
# for test_case in range(1, int(input()) + 1):
#     N, M = map(int, input().split())
#     str_in = list(map(int, input().split()))
#     G = [[] for _ in range(N + 1)]
#     for i in range(M):
#         u = str_in[i*2]
#         v = str_in[i*2+1]
#         G[u].append(v)
#         G[v].append(u)
#     visit = [False] * (N + 1)
#     count = 0
#     for i in range(1, N + 1):
#         if not visit[i]:
#             count += 1
#             dfs(i)
#     print('#{} {}'.format(test_case, count))


def find_set(x):
    if x != G[x]:
        G[x] = find_set(G[x])
    return G[x]


for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    G = [x for x in range(N + 1)]
    count = N
    str_in = list(map(int, input().split()))
    for i in range(M):
        u = str_in[2*i]
        v = str_in[2*i+1]
        a = find_set(u); b = find_set(v)
        if a == b: continue
        G[b] = a
        count -= 1
    print('#{} {}'.format(test_case, count))
