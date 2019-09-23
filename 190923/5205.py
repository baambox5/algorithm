import sys
sys.stdin = open('5205.txt', 'r')


def quick_sort(lo, hi):
    if lo >= hi:
        return
    i, j, pivot = lo, hi, arr[lo]
    while i < j:
        while i <= hi and pivot >= arr[i]:
            i += 1
        while pivot < arr[j]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[lo], arr[j] = arr[j], arr[lo]
    quick_sort(lo, j - 1)
    quick_sort(j + 1, hi)


for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(0, N - 1)
    print('#{} {}'.format(test_case, arr[N // 2]))
