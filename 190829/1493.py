import sys
sys.stdin = open('1493.txt', 'r')

for test_case in range(1, int(input()) + 1):
    p, q = map(int, input().split())
    while True:
        i = 1
        first = 1 + (i-1) * i // 2
        end = 1 + (i*i + i-2) // 2
        if first <= p <= end:
            row = i - p + first
        i += 1