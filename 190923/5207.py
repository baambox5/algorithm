import sys
sys.stdin = open('5207.txt', 'r')


def merge_sort(lo, hi):
    if lo == hi:
        return
    mid = (lo + hi) >> 1
    merge_sort(lo, mid)
    merge_sort(mid + 1, hi)
    i, j, k = lo, mid + 1, lo
    while i <= mid and j <= hi:
        if A[i] < A[j]:
            tmp[k] = A[i]
            i, k = i + 1, k + 1
        else:
            tmp[k] = A[j]
            j, k = j + 1, k + 1
    while i <= mid:
        tmp[k] = A[i]
        i, k = i + 1, k + 1
    while j <= hi:
        tmp[k] = A[j]
        j, k = j + 1, k + 1
    for i in range(lo, hi + 1):
        A[i] = tmp[i]


for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    tmp = [0] * N
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    merge_sort(0, N - 1)
    count = 0
    for num in B:
        le = 1
        ri = 1
        lo = 0
        hi = N - 1
        while True:
            mid = (lo + hi) >> 1
            if A[mid] < num:
                lo = mid + 1
                if le:
                    ri = 1
                    le = 0
                else:
                    break
            elif A[mid] > num:
                hi = mid - 1
                if ri:
                    le = 1
                    ri = 0
                else:
                    break
            else:
                count += 1
                break
            if mid == (lo + hi) >> 1:
                break
    print('#{} {}'.format(test_case, count))
