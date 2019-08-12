import sys
sys.stdin = open('input.txt', 'r')

for test_case in range(1, int(input()) + 1):
    res = 0
    in_str = input()
    for i in range(len(in_str) // 2):
        if in_str[i] != in_str[-i-1]:
            break
    else:
        res = 1
    print('#{} {}'.format(test_case, res))