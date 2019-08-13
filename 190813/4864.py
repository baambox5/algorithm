import sys
sys.stdin = open('4864.txt', 'r')

for test_case in range(1, int(input()) + 1):
    str_1 = input()
    str_2 = input()
    N = len(str_1)
    M = len(str_2)
    res = 0
    for i in range(M - N + 1):
        for j in range(N):
            if str_1[j] != str_2[i + j]:
                break
        else:
            res = 1
            break
    print('#{} {}'.format(test_case, res))
