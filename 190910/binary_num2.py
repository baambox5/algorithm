import sys, math
sys.stdin = open('binary_num2.txt', 'r')


def binary(k, num):
    global res
    if k == 14:
        res = 'overflow'
        return
    elif math.isclose(num, 0.0):
        return
    else:
        if num >= 1 * 2**(-k):
            res += '1'
            num -= 1 * 2**(-k)
        else:
            res += '0'
        binary(k + 1, num)


for test_case in range(1, int(input()) + 1):
    num_in = float(input())
    res = ''
    binary(1, num_in)
    print('#{} {}'.format(test_case, res))
