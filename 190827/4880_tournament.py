import sys
sys.stdin = open('4880.txt', 'r')


def tournament(n, a):
    pivot = n // 2
    if n == 2:
        if (arr[a[0]] == '1' and arr[a[1]] == '2') or (arr[a[0]] == '2' and arr[a[1]] == '3') or (arr[a[0]] == '3' and arr[a[1]] == '1'):
            return a[1]
        else:
            return a[0]
    elif n == 1:
        return a[0]
    else:
        winner = []
        for i in range(0, pivot, 2):
            if (arr[a[i]] == '1' and arr[a[i+1]] == '2') or (arr[a[i]] == '2' and arr[a[i+1]] == '3') or (arr[a[i]] == '3' and arr[a[i+1]] == '1'):
                winner.append(a[i + 1])
            else:
                winner.append(a[i])
        if pivot % 2:
            winner.append(a[pivot-1])
        idx_a = tournament(len(winner), winner)
        winner = []
        if n == 3:
            pivot += 1
        for i in range(pivot, n - 1, 2):
            if (arr[a[i]] == '1' and arr[a[i+1]] == '2') or (arr[a[i]] == '2' and arr[a[i+1]] == '3') or (arr[a[i]] == '3' and arr[a[i+1]] == '1'):
                winner.append(a[i+1])
            else:
                winner.append(a[i])
        if (n - pivot) % 2:
            winner.append(a[n-1])
        idx_b = tournament(len(winner), winner)
        if (arr[idx_a] == '1' and arr[idx_b] == '2') or (arr[idx_a] == '2' and arr[idx_b] == '3') or (arr[idx_a] == '3' and arr[idx_b] == '1'):
            return idx_b
        else:
            return idx_a


for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = input().split()
    order = [i for i in range(N)]
    idx = tournament(N, order)
    print('#{} {}'.format(test_case, idx + 1))

