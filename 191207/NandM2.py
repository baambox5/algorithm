import sys
sys.stdin = open('NandM2.txt', 'r')


def perm(k, s):
    if k == M:
        for num in order:
            print(num, end=' ')
        print()
    else:
        for i in range(s, N + 1):
            order[k] = i
            perm(k + 1, i + 1)


N, M = map(int, input().split())
order = [0] * M
perm(0, 1)
