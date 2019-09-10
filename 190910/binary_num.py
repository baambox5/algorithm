import sys
sys.stdin = open('binary_num.txt', 'r')

hex_char = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
def hextobi(c):
    if c.isdecimal():
        num = int(c)
    else:
        num = hex_char[c]
    if num == 0:
        res = '0000'
    elif num < 2:
        res = '000'
    elif num < 4:
        res = '00'
    elif num < 8:
        res = '0'
    else:
        res = ''
    temp = ''
    while num > 0:
        temp += str(num % 2)
        num //= 2
    for i in range(len(temp) - 1, -1, -1):
        res += temp[i]
    return res


for test_case in range(1, int(input()) + 1):
    N, str_in = input().split()
    print('#{}'.format(test_case), end=' ')
    for char in str_in:
        print(hextobi(char), end='')
    print()
