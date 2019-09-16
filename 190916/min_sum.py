import sys
sys.stdin = open('min_sum.txt', 'r')


def dfs(x, y, s):
    global min_sum
    if x == N-1 and y == N-1:
        if min_sum > s:
            min_sum = s
        return
    elif s > min_sum:
        return
    else:
        if x != N-1:
            dfs(x + 1, y, s + arr[x + 1][y])
        if y != N-1:
            dfs(x, y + 1, s + arr[x][y + 1])


for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr += [list(map(int, input().split()))]
    min_sum = 1000000
    dfs(0, 0, arr[0][0])
    print('#{} {}'.format(test_case, min_sum))
