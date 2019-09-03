import sys
sys.stdin = open('14501.txt', 'r')


def backtrack(k, s, value):
    global max_value
    if s > N:
        if max_value < value - arr[order[k-1]][1]:
            max_value = value - arr[order[k-1]][1]
        return
    elif s == N:
        if max_value < value:
            max_value = value
    else:
        for i in range(s, N):
            order[k] = i
            backtrack(k + 1, i + arr[i][0], value + arr[i][1])


N = int(input())
arr = []
max_value = 0
for _ in range(N):
    Ti, Pi = map(int, input().split())
    arr.append((Ti, Pi))
order = [0] * N
backtrack(0, 0, 0)
print(max_value)