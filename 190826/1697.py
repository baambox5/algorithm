import sys
sys.stdin = open('1697.txt', 'r')
from collections import deque

N, K = map(int, input().split())
min_value = 17
if N > K:
    min_value = N - K
elif N == K:
    min_value = 0
else:
    visit = [0] * 100001
    D = [0] * 100001
    Q = deque()
    visit[N] = 1
    Q.append(N)
    while Q:
        position = Q.popleft()
        if position == K:
            break
        if K+2 > position > 0 and not visit[position-1]:
            Q.append(position - 1)
            visit[position - 1] = 1
            D[position - 1] = D[position] + 1
        if K > position and not visit[position+1]:
            Q.append(position + 1)
            visit[position + 1] = 1
            D[position + 1] = D[position] + 1
        if K+2 > 2*position and not visit[2*position]:
            Q.append(2 * position)
            visit[2 * position] = 1
            D[2 * position] = D[position] + 1
    min_value = D[position]
print(min_value)