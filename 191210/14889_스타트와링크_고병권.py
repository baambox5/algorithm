import sys
sys.stdin = open('start_link.txt', 'r')


def perm(k, s):
    global res
    if k == N // 2:
        sum_value = 0
        for m in range(N // 2 - 1):
            for n in range(m + 1, N // 2):
                sum_value += arr[order[m]][order[n]] + arr[order[n]][order[m]]
        res += [sum_value]
    else:
        for i in range(s, N):
            order[k] = i
            perm(k + 1, i + 1)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
order = [0] * (N // 2)
res = []
min_value = 100000
perm(0, 0)
for i in range(len(res) // 2):
    diff = res[i] - res[-i - 1]
    if diff < 0:
        diff = - diff
    if min_value > diff:
        min_value = diff
print(min_value)
