import sys
sys.stdin = open('4843.txt', 'r')

for test_case in range(1, int(input()) + 1):
    len_num = int(input())
    numbers = list(map(int, input().split()))
    for i in range(1, len_num):
        for j in range(i, len_num):
            if numbers[i-1] > numbers[j]:
                numbers[i-1], numbers[j] = numbers[j], numbers[i-1]
    res = ''
    for i in range(5):
        res += ' ' + str(numbers[-i-1])
        res += ' ' + str(numbers[i])
    print('#{}{}'.format(test_case, res))
