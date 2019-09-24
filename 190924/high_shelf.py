import sys
sys.stdin = open('high_shelf.txt', 'r')


def perm(k, s, visit, x):
    global min_height
    if k == i:
        if B <= s < min_height:
            min_height = s
        return
    elif min_height <= s:
        return
    else:
        for j in range(x, N):
            if not visit & (1 << j):
                perm(k + 1, s + H[j], visit | (1 << j), j)


for test_case in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    min_height = 1000000
    for i in range(1, N + 1):
        perm(0, 0, 0, 0)
    print('#{} {}'.format(test_case, min_height - B))
