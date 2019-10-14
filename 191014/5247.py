import sys
sys.stdin = open('5247.txt', 'r')
from collections import deque

for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    if M > N:
        min_count = M - N
    else:
        min_count = N - M
    Q = deque()
    visit = [0] * 1000001
    Q.append((N, 0))
    visit[N] = 1
    while Q:
        p, k = Q.popleft()
        if p == M:
            min_count = k
            break
        if 1000001 > p > 1 and not visit[p-1]:
            visit[p-1] = 1
            Q.append((p-1, k + 1))
        if 999999 > p > 0 and not visit[p+1]:
            visit[p+1] = 1
            Q.append((p+1, k + 1))
        if 500001 > p > 0 and not visit[p*2]:
            visit[p*2] = 1
            Q.append((p*2, k + 1))
        if 1000011 > p > 10 and not visit[p-10]:
            visit[p-10] = 1
            Q.append((p-10, k + 1))
    print('#{} {}'.format(test_case, min_count))
