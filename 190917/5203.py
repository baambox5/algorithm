import sys
sys.stdin = open('5203.txt', 'r')

d_1 = [-2, -1, 2]
d_2 = [-1, 1, 1]
for test_case in range(1, int(input()) + 1):
    p_1 = [0] * 10
    p_2 = [0] * 10
    res = 0
    res_1, res_2 = 0, 0
    arr = [0] * 12
    i = 0
    for num in input().split():
        arr[i] = int(num)
        i += 1
    for i in range(0, 12, 2):
        p_1[arr[i]] += 1
        p_2[arr[i + 1]] += 1
        if i > 3:
            if p_1[arr[i]] == 3:
                res_1 = 1
            if p_2[arr[i + 1]] == 3:
                res_2 = 1
            for j in range(3):
                if 0 <= arr[i] + d_1[j] <= 9 and 0 <= arr[i] + d_2[j] <= 9:
                    if p_1[arr[i]+d_1[j]] and p_1[arr[i]+d_2[j]]:
                        res_1 = 1
                if 0 <= arr[i+1] + d_1[j] <= 9 and 0 <= arr[i+1] + d_2[j] <= 9:
                    if p_2[arr[i+1]+d_1[j]] and p_2[arr[i+1]+d_2[j]]:
                        res_2 = 1
            if res_1 and res_2:
                res = 0
                break
            elif res_1:
                res = 1
                break
            elif res_2:
                res = 2
                break
    else:
        res = 0
    print('#{} {}'.format(test_case, res))
