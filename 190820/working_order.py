import sys
sys.stdin = open('working_order.txt', 'r')

# for test_case in range(1, 11):
#     V, E = tuple(map(int, input().split()))
#     G = [[] for _ in range(V + 1)]
#     condition = [0] * (V + 1)
#     visit = [0] * (V + 1)
#     arr = list(map(int, input().split()))
#     stack_list = []
#     for i in range(len(arr)):
#         if i % 2:
#             condition[arr[i]] += 1
#         else:
#             G[arr[i]].append(arr[i + 1])
#     print('#{}'.format(test_case), end=' ')
#     for i in range(1, V + 1):
#         if not condition[i] and not visit[i]:
#             stack_list.append(i)
#             visit[i] = 1
#             print('{}'.format(i), end=' ')
#             for j in G[i]:
#                 condition[j] -= 1
#             while stack_list:
#                 for w in G[i]:
#                     if not condition[w] and not visit[w]:
#                         visit[w] = 1
#                         stack_list.append(i)
#                         print('{}'.format(w), end=' ')
#                         i = w
#                         for j in G[w]:
#                             condition[j] -= 1
#                         break
#                 else:
#                     i = stack_list.pop()
#     print()


def dfs(v):
    visit[v] = 1
    print('{}'.format(v), end=' ')
    for w in G[v]:
        condition[w] -= 1
        if not condition[w] and not visit[w]:
            dfs(w)


for test_case in range(1, 11):
    V, E = tuple(map(int, input().split()))
    G = [[] for _ in range(V + 1)]
    condition = [0] * (V + 1)
    visit = [0] * (V + 1)
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        if i % 2:
            condition[arr[i]] += 1
        else:
            G[arr[i]].append(arr[i + 1])
    print('#{}'.format(test_case), end=' ')
    for i in range(1, V + 1):
        if not condition[i] and not visit[i]:
            dfs(i)
    print()







