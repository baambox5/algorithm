import sys
sys.stdin = open('2597.txt', 'r')

len_ruler = int(input())
arr = []
for _ in range(3):
    a, b = map(int, input().split())
    arr += [a]
    arr += [b]
for i in range(3):
    if arr[2*i] == arr[2*i+1]:
            continue
    mid = (arr[2*i] + arr[2*i+1]) / 2
    if mid >= len_ruler / 2:
        for j in range(6):
            if arr[j] > mid:
                arr[j] = 2 * mid - arr[j]
        len_ruler = mid
    else:
        for j in range(6):
            if arr[j] < mid:
                arr[j] = 2 * mid - arr[j]
        for j in range(6):
            arr[j] -= mid
        len_ruler -= mid
print(len_ruler)
