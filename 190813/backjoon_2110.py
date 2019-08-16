import sys
sys.stdin = open('2110_input.txt', 'r')

N, M = tuple(map(int, input().split()))
arr = []
for i in range(N):
    arr += [int(input())]
max_dist = 0
min_dist = 0
max_dist = (arr[-1] - arr[0]) // (M - 1)
for i in range(N - 1):
    for j in range(i + 1, N):
        diff = arr[i] - arr[j]
        if diff < 0:
            diff = -diff
        if min_dist < diff < max_dist:
            min_dist = diff
            res = diff
print(res)





