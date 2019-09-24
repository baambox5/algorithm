import sys
sys.stdin = open('5208.txt', 'r')


def backtrack(p, count):
    global min_count
    if p >= N:
        if count < min_count:
            min_count = count
        return
    elif min_count <= count:
        return
    else:
        for i in range(1, station[p] + 1):
            backtrack(p + i, count + 1)


for test_case in range(1, int(input()) + 1):
    station = list(map(int, input().split()))
    N = station[0]
    min_count = N
    backtrack(1, -1)
    print('#{} {}'.format(test_case, min_count))
