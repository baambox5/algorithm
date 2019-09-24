import sys
sys.stdin = open('3980.txt', 'r')


def perm(k, s, visit):
    global max_sum
    if k == 11:
        if s > max_sum:
            max_sum = s
        return
    else:
        for i in range(11):
            if not visit & (1 << i) and arr[k][i]:
                perm(k + 1, s + arr[k][i], visit | (1 << i))


for C in range(int(input())):
    arr = []
    for _ in range(11):
        arr += [list(map(int, input().split()))]
    max_sum = 0
    perm(0, 0, 0)
    print(max_sum)
