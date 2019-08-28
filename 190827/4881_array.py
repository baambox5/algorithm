import sys
sys.stdin = open('4881.txt', 'r')
from itertools import permutations  # 모든 경우를 찾으므로 좀 느릴 수 있다.


# def find():
#     min_value = 100
#     for p in permutations(range(N)):
#         s = 0
#         for i in range(N):
#             s += m[i][p[i]]
#         if min_value > s:
#             min_value = s
#     return min_value
#
#
# for test_case in range(1, int(input()) + 1):
#     N = int(input())
#     m = [list(map(int, input().split())) for x in range(N)]
#     print('#{} {}'.format(test_case, find()))


# ----------------------------------------------------------------------
# def find(n, s):
#     global minV
#     if n == N:
#         if minV > s:
#             minV = s
#         return
#     elif minV <= s:
#         return
#     else:
#         for i in range(N):
#             if u[i] == 0:
#                 u[i] = 1
#                 find(n+1, s+m[n][i])
#                 u[i] = 0
#         return
#
#
# for test_case in range(1, int(input()) + 1):
#     N = int(input())
#     m = [list(map(int, input().split())) for x in range(N)]
#     minV = 100
#     u = [0 for i in range(N)]
#     find(0, 0)
#     print('#{} {}'.format(test_case, minV))


# -----------------------------------------------------------------------
def perm(k, sum_value, visit):
    global low_sum
    if k == N:
        if sum_value < low_sum:
            low_sum = sum_value
        return
    elif low_sum <= sum_value:
        return
    else:
        for i in range(N):
            # 이미 앞에 선택한 적이 있는 열인지 확인해서 선택한 적이 있으면 넘김
            if visit & (1 << i): continue
            # 각 행 별로 최대값은 선택 안할 것이라 가정하고 넘김
            if max_num[k] == i: continue
            perm(k + 1, sum_value+arr[k][i], visit | (1 << i))
        return


for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = []
    max_num = [0] * N
    # 입력 받기
    for _ in range(N):
        arr += [list(map(int, input().split()))]
    low_sum = 100
    # 각 행마다 최대값 찾기
    for i in range(N):
        max_value = 0
        for j in range(N):
            if arr[i][j] > max_value:
                max_value = arr[i][j]
                x, y = i, j
        else:
            max_num[x] = y
    perm(0, 0, 0)
    print('#{} {}'.format(test_case, low_sum))
