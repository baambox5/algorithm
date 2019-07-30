import sys
sys.stdin = open('input_4834.txt', 'r')

for test_case in range(1, int(input())+1):
    len_number = int(input())
    input_number = input()
    numbers = [0] * 10
    max_number = 0
    for number in input_number:
        numbers[int(number)] += 1
    for i in range(1, 10):
        if numbers[i] >= numbers[max_number]:
            max_number = i
    print('#{} {} {}'.format(test_case, max_number, numbers[max_number]))
