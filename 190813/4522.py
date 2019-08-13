import sys
sys.stdin = open('4522.txt', 'r')

for test_case in range(1, int(input()) + 1):
    str_in = input()
    for i in range(len(str_in) // 2):
        if str_in[i] != str_in[-i-1] and str_in[i] != '?' and str_in[-i-1] != '?':
            res = 'Not exist'
            break
    else:
        res = 'Exist'
    print('#{} {}'.format(test_case, res))
