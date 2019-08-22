import sys
sys.stdin = open('11724.txt', 'r')
input = sys.stdin.readline
sys.setrecursionlimit(2**16)


def dfs(s):
    if not visit[s]:
        visit[s] = 1
        for w in G[s]:
            dfs(w)
        else:
            return 1
    else:
        return 0


for _ in range(1, 3):
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    visit = [0] * (N + 1)
    count = 0
    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    for i in range(1, N + 1):
        count += dfs(i)
    print(count)


# for _ in range(1, 3):
#     N, M = map(int, input().split())
#     G = [[] for _ in range(N + 1)]
#     visit = [0] * (N + 1)
#     count = 0
#     stack_list = []
#     for _ in range(M):
#         u, v = map(int, input().split())
#         G[u].append(v)
#         G[v].append(u)
#     for i in range(1, N + 1):
#         if not visit[i]:
#             count += 1
#             stack_list.append(i)
#             visit[i] = 1
#             while stack_list:
#                 for w in G[i]:
#                     if not visit[w]:
#                         visit[w] = 1
#                         stack_list.append(i)
#                         i = w
#                         break
#                 else:
#                     i = stack_list.pop()
#     print(count)
