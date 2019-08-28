import sys
sys.stdin = open('1759.txt', 'r')


def perm(k, n, visit, count_v, count_c):
    if k == n:
        if count_v >= 1 and count_c >=2:
            for i in range(n):
                print(arr[order[i]], end='')
            else:
                print()
        return
    else:
        for i in range(C):
            if visit & (1 << i): continue
            if k and ord(arr[order[k-1]]) > ord(arr[i]): continue
            order[k] = i
            if arr[i] == 'a' or arr[i] == 'e' or arr[i] == 'i' or arr[i] == 'o' or arr[i] == 'u':
                count_v += 1
                perm(k+1, n, visit | (1 << i), count_v, count_c)
                count_v -= 1
            else:
                count_c += 1
                perm(k+1, n, visit | (1 << i), count_v, count_c)
                count_c -= 1


def qsort(a, low, high):
    if low < high:
        pivot = partition(a, low, high)
        qsort(a, low, pivot - 1)
        qsort(a, pivot + 1, high)


def partition(a, pivot, high):
    i = pivot + 1
    j = high
    while True:
        while i < high and ord(a[i]) < ord(a[pivot]):
            i += 1
        while j > pivot and ord(a[j]) > ord(a[pivot]):
            j -= 1
        if i >= j:
            break
        a[i], a[j] = a[j], a[i]
        j -= 1
        i += 1
    a[pivot], a[j] = a[j], a[pivot]
    return j


L, C = map(int, input().split())
arr = input().split()
order = [0] * C
qsort(arr, 0, C - 1)
perm(0, L, 0, 0, 0)
