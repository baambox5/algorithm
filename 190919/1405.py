import sys
sys.stdin = open('1405.txt', 'r')


def dfs(k, x, y, percent):
    global res
    if arr[x][y]:
        res -= percent
        return
    elif k == N:
        return
    else:
        if R:
            arr[x][y] = 1
            dfs(k + 1, x, y + 1, percent * R)
            arr[x][y] = 0
        if L:
            arr[x][y] = 1
            dfs(k + 1, x, y - 1, percent * L)
            arr[x][y] = 0
        if D:
            arr[x][y] = 1
            dfs(k + 1, x + 1, y, percent * D)
            arr[x][y] = 0
        if U:
            arr[x][y] = 1
            dfs(k + 1, x - 1, y, percent * U)
            arr[x][y] = 0


for test_case in range(1, int(input()) + 1):
     = int(input())
    N, R, L, D, U = map(int, input().split())
    R /= 100
    L /= 100
    D /= 100
    U /= 100
    res = 1
    arr = [[0] * 29 for _ in range(29)]
    dfs(0, 14, 14, 1)
    print('%.10f' % res)
