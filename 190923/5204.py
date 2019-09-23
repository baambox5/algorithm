import sys
sys.stdin = open('5204.txt', 'r')


def merge_sort(lo, hi):
    global count
    if lo == hi:
        return
    mid = (lo + hi - 1) // 2
    merge_sort(lo, mid)
    merge_sort(mid + 1, hi)
    i, j, k = lo, mid + 1, lo
    while i <= mid and j <= hi:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            i, k = i + 1, k + 1
        else:
            tmp[k] = arr[j]
            j, k = j + 1, k + 1
    while i <= mid:
        tmp[k] = arr[i]
        i, k = i + 1, k + 1
    while j <= hi:
        tmp[k] = arr[j]
        j, k = j + 1, k + 1
    if arr[mid] > arr[hi]:
        count += 1
    for i in range(lo, hi + 1):
        arr[i] = tmp[i]


for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    count = 0
    tmp = [0] * N
    merge_sort(0, N - 1)
    print('#{} {} {}'.format(test_case, arr[N // 2], count))
