import sys
sys.stdin = open('5209.txt', 'r')


def backtrack(k, s, visit):
    global min_sum
    if k == N:
        if s < min_sum:
            min_sum = s
    elif min_sum <= s:
        return
    else:
        for i in range(N):
            if not visit & (1 << i):
                backtrack(k + 1, s + arr[k][i], visit | (1 << i))


for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr += [list(map(int, input().split()))]
    min_sum = 1000000
    backtrack(0, 0, 0)
    print('#{} {}'.format(test_case, min_sum))
