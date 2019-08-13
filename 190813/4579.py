import sys
sys.stdin = open('4579.txt', 'r')

for test_case in range(1, int(input()) + 1):
    str_in = input()
    for i in range(len(str_in) // 2):
        if str_in[i] != str_in[-i-1]:
            if str_in[i] != '*' and str_in[-i-1] != '*':
                res = 'Not exist'
                break
        if str_in[i] == '*' or str_in[-i-1] == '*':
            res = 'Exist'
            break
    else:
        res = 'Exist'
    print('#{} {}'.format(test_case, res))
