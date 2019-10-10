import sys
sys.stdin = open('1799.txt', 'r')


# def perm(k, count):
#     global max_count
#     if k == N:
#         if max_count < count:
#             max_count = count
#         return
#     else:
#         for i in range(N):
#             if arr[k][i] == '1':
#                 y = 1
#                 for j in range(k):
#                     for x in range(N):
#                         if order[j][x] and (i == x + k - j or i == x - k + j):
#                             y = 0
#                             break
#                     if not y:
#                         break
#                 if y:
#                     order[k][i] = 1
#                     count += 1
#                     perm(k + 1, count)
#         else:
#             perm(k + 1, count)
#
#
# N = int(input())
# arr = [0] * N
# for i in range(N):
#     arr[i] = input().split()
# max_count = 0
# for m in range(N):
#     order = [[0] * N for _ in range(N)]
#     perm(m, 0)
# print(max_count)


N = int(input())
arr = [0] * N
for i in range(N):
    arr[i] = input().split()
max_count = 0
visit_1 = [[0] * N for _ in range(N)]
visit_2 = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not i % 2:
            if j % 2:

            else:
        else:
            if not j % 2:

            else:
print(max_count)