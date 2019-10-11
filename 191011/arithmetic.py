import sys
sys.stdin = open('arithmetic.txt', 'r')


def calc(n):
    if not arr[n][0]:
        return value[n]
    else:
        a = calc(arr[n][0])
        operator = char[n]
        b = calc(arr[n][1])
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return a / b


for test_case in range(1, 11):
    N = int(input())
    arr = [[0] * 2 for _ in range(N + 1)]
    value = [0] * (N + 1)
    char = [0] * (N + 1)
    for _ in range(N):
        str_in = input().split()
        i = int(str_in[0])
        if str_in[1].isdecimal():
            value[i] = int(str_in[1])
        else:
            char[i] = str_in[1]
            arr[i][0] = int(str_in[2])
            arr[i][1] = int(str_in[3])
    res = calc(1)
    print('#{} {}'.format(test_case, int(res)))
