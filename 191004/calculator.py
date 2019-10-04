import sys
sys.stdin = open('calculator.txt', 'r')


def divide(n):
    count = 0
    while n > 0:
        if num[n % 10] == '0':
            return 0
        n //= 10
        count += 1
    return count


def calc(k, q):
    global min_count
    if q <= 1:
        if min_count > k:
            min_count = k
        return
    elif min_count <= k:
        return
    else:
        for i in range(q, 1, -1):
            if q % i:
                continue
            temp = divide(i)
            if temp:
                calc(k + temp + 1, q // i)


for test_case in range(1, int(input()) + 1):
    num = input().split()
    X = int(input())
    min_count = 1000000
    if X == 1:
        if num[1] == '1':
            min_count = 2
    else:
        calc(0, X)
    if min_count != 1000000:
        print('#{} {}'.format(test_case, min_count))
    else:
        print('#{} {}'.format(test_case, -1))
