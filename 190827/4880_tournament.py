import sys
sys.stdin = open('4880.txt', 'r')


def tournament(s, e):
    if s == e:
        return s
    else:
        idx_a = tournament(s, (s+e) // 2)
        idx_b = tournament(((s+e) // 2) + 1, e)
        if (arr[idx_a] == '1' and arr[idx_b] == '2') or (arr[idx_a] == '2' and arr[idx_b] == '3') or (arr[idx_a] == '3' and arr[idx_b] == '1'):
            return idx_b
        else:
            return idx_a


for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = input().split()
    idx = tournament(0, N-1)
    print('#{} {}'.format(test_case, idx + 1))

