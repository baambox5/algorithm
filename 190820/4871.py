import sys
sys.stdin = open('4871.txt', 'r')

# for test_case in range(1, int(input()) + 1):
#     V, E = tuple(map(int, input().split()))
#     G = [[] for _ in range(V + 1)]
#     visit = [0] * (V + 1)
#     stack_list = []
#     res = 0
#     for _ in range(E):
#         s, e = tuple(map(int, input().split()))
#         G[s].append(e)
#     start, end = tuple(map(int, input().split()))
#     stack_list.append(start)
#     visit[start] = 1
#     while stack_list:
#         for i in G[start]:
#             if not visit[i]:
#                 visit[i] = 1
#                 stack_list.append(start)
#                 start = i
#                 if i == end:
#                     res = 1
#                     stack_list = []
#                 break
#         else:
#             start = stack_list.pop()
#     print('#{} {}'.format(test_case, res))


def dfs(s, e):
    visit[s] = 1
    if s == e:
        return 1
    for w in G[s]:
        if not visit[w]:
            if dfs(w, e):
                return 1
    else:
        return 0


for test_case in range(1, int(input()) + 1):
    V, E = tuple(map(int, input().split()))
    G = [[] for _ in range(V + 1)]
    visit = [0] * (V + 1)
    for _ in range(E):
        st, en = tuple(map(int, input().split()))
        G[st].append(en)
    start, end = tuple(map(int, input().split()))
    res = dfs(start, end)
    print('#{} {}'.format(test_case, res))
