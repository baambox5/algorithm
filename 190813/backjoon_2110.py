import sys
sys.stdin = open('2110_input.txt', 'r')

N, M = tuple(map(int, input().split()))
arr = []
for i in range(N):
    arr += [int(input())]
max_dist = 0
min_dist = 10000
for i in range(N - 1):
    for j in range(i + 1, N):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
# for i in range(N - M + 1):
#     for j in range(i + 1, ):
#
print(max_dist)


