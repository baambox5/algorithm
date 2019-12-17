import sys
sys.stdin = open('dice_yut.txt', 'r')


def perm(k, axis1, axis2, axis3, axis4, sum_value, s):
    global max_sum
    if k == 10:
        if max_sum < sum_value:
            max_sum = sum_value
        return
    else:
        for i in range(s, 10):
            r, idx = axis1
            dice_in[i]
            perm(k + 1, ())


arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0]
arr1 = [13, 16, 19]
arr2 = [22, 24]
arr3 = [28, 27, 26]
arr4 = [25, 30, 35]
max_sum = 0
dice_in = list(map(int, input().split()))
perm(0, (0, 0), (0, 0), (0, 0), (0, 0), 0, 0)
