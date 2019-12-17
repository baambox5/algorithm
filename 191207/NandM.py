import sys
sys.stdin = open('NandM.txt', 'r')


def perm(k, visit):
    if k == M:
        for num in order:
            print(num, end=' ')
        print()
    else:
        for i in range(1, N + 1):
            if visit & (1 << i):
                continue
            order[k] = i
            perm(k + 1, visit | (1 << i))


N, M = map(int, input().split())
order = [0] * M
perm(0, 0)
