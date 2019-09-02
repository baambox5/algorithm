import sys
sys.stdin = open('14889.txt', 'r')


def backtrack(k, s):
    if k == N // 2:
        sum_start = 0
        for i in range(N // 2):
            for j in range(i + 1, N // 2):
                sum_start += arr[start[i]][start[j]] + arr[start[j]][start[i]]
        temp.append(sum_start)
    else:
        for i in range(s, N):
            start[k] = i
            backtrack(k + 1, i + 1)


N = int(input())
arr = []
start = [0] * (N // 2)
min_value = 100
for _ in range(N):
    arr.append(list(map(int, input().split())))
temp = []
backtrack(0, 0)
sum_start = 0
sum_link = 0
for k in range(len(temp) // 2):
    diff = temp[k] - temp[-k-1]
    if diff < 0:
        diff = -diff
    if min_value > diff:
        min_value = diff
print(min_value)