import sys
sys.stdin = open('mono_increase.txt', 'r')


def perm(k, s, multi):
    global max_value
    if k == 2:
        if mono(multi) and max_value < multi:
            max_value = multi
    else:
        for i in range(s, N):
            perm(k + 1, i + 1, multi * arr[i])


def mono(value):
    num = value % 10
    while value > 0:
        value //= 10
        if num >= value % 10:
            num = value % 10
        else:
            return 0
    return 1


for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_value = 0
    perm(0, 0, 1)
    if max_value:
        print('#{} {}'.format(test_case, max_value))
    else:
        print('#{} {}'.format(test_case, -1))
