import sys
sys.stdin = open('2806.txt', 'r')


def perm(k, visit):
    if k == N:
        return 1
    else:
        res = 0
        for i in range(N):
            if visit & (1 << i): continue
            for j in range(k):
                if i == order[j] - (k - j) or i == order[j] + (k - j):
                    break
            else:
                order[k] = i
                res += perm(k+1, visit | (1 << i))
        else:
            if res != None:
                return res
            else:
                return 0

            
for test_case in range(1, int(input()) + 1):
    N = int(input())
    count = 0
    order = [0] * N
    count = perm(0, 0)
    print('#{} {}'.format(test_case, count))