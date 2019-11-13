import sys
sys.stdin = open('make_number.txt', 'r')


def perm(k, sum_value, plus, minus, multi, divide):
    global min_value, max_value
    if k == N:
        if sum_value < min_value:
            min_value = sum_value
        if sum_value > max_value:
            max_value = sum_value
        return
    else:
        if plus:
            perm(k + 1, sum_value + numbers[k], plus - 1, minus, multi, divide)
        if minus:
            perm(k + 1, sum_value - numbers[k], plus, minus - 1, multi, divide)
        if multi:
            perm(k + 1, sum_value * numbers[k], plus, minus, multi - 1, divide)
        if divide:
            perm(k + 1, int(sum_value / numbers[k]), plus, minus, multi, divide - 1)


for test_case in range(1, int(input()) + 1):
    N = int(input())
    max_value = -1000000
    min_value = 1000000
    operator = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    perm(1, numbers[0], operator[0], operator[1], operator[2], operator[3])
    print('#{} {}'.format(test_case, max_value - min_value))
