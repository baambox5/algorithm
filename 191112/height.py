import sys
sys.stdin = open('height.txt', 'r')


def dfs(k, arr):
    global people_count
    for j in arr[k]:
        if not visit[j]:
            people_count += 1
            visit[j] = 1
            dfs(j, arr)


for test_case in range(1, int(input()) + 1):
    N = int(input())
    M = int(input())
    up = [[] * (N + 1) for _ in range(N + 1)]
    down = [[] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        up[a].append(b)
        down[b].append(a)
    count = 0
    for i in range(1, N + 1):
        visit = [0] * (N + 1)
        people_count = 1
        dfs(i, up)
        dfs(i, down)
        if people_count == N:
            count += 1
    print('#{} {}'.format(test_case, count))
