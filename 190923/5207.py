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
