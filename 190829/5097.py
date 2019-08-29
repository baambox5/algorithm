import sys
sys.stdin = open('5097.txt', 'r')
from collections import deque

for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = deque()
    arr += input().split()
    for _ in range(M):
        value = arr.popleft()
        arr.append(value)
    else:
        print('#{} {}'.format(test_case, arr[0]))
