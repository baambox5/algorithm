import sys
sys.stdin = open('5099.txt', 'r')
from collections import deque

for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    list_in = deque()
    list_in += input().split()
    q = deque()
    idx = 0
    for _ in range(N):
        q.append((idx, int(list_in.popleft())))
        idx += 1
    while q:
        m, c = q.popleft()
        c //= 2
        if not c:
            if list_in:
                q.append((idx, int(list_in.popleft())))
                idx += 1
            if not q:
                break
        else:
            q.append((m, c))
    print('#{} {}'.format(test_case, m+1))
