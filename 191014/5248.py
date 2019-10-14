import sys
sys.stdin = open('5248.txt', 'r')


def dfs(n):
    visit[n] = True
    for w in G[n]:
        if not visit[w]:
            dfs(w)


for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    str_in = list(map(int, input().split()))
    G = [[] for _ in range(N + 1)]
    for i in range(M):
        u = str_in[i*2]
        v = str_in[i*2+1]
        G[u].append(v)
        G[v].append(u)
    visit = [False] * (N + 1)
    count = 0
    for i in range(1, N + 1):
        if not visit[i]:
            count += 1
            dfs(i)
    print('#{} {}'.format(test_case, count))
