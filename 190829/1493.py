import sys
sys.stdin = open('1493.txt', 'r')

arr = [0]
i = 1
while True:
    first = 1 + (i-1) * i // 2
    arr.append(first)
    if first > 10000:
        break
    i += 1
for test_case in range(1, int(input()) + 1):
    p, q = map(int, input().split())
    row_p = 0
    row_q = 0
    i = 1
    first_p = 0
    first_q = 0
    while True:        
        if arr[i] > p and not row_p:
            first_p = arr[i-1]
            row_p = i-1 - p + first_p
        if arr[i] > q and not row_q:
            first_q = arr[i-1]
            row_q = i-1 - q + first_q
        if row_p and row_q:
            break
        i += 1
    row = row_p + row_q
    column = 2 + p + q - first_p - first_q
    idx = row + column - 1
    res = column + (idx-1) * idx // 2
    print('#{} {}'.format(test_case, res))