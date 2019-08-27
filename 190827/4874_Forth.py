import sys
sys.stdin = open('4874.txt', 'r')

for test_case in range(1, int(input()) + 1):
    stack_list = []
    str_in = input().split()
    print('#{}'.format(test_case), end=' ')
    for string in str_in:
        if string.isdecimal():
            stack_list.append(string)
        elif string == '*' or string == '/' or string == '+' or string == '-':
            if len(stack_list) <= 1:
                print('error')
                break
            b = int(stack_list.pop())
            a = int(stack_list.pop())
            if string == '*':
                stack_list.append(a * b)
            elif string == '/':
                stack_list.append(a // b)
            elif string == '+':
                stack_list.append(a + b)
            elif string == '-':
                stack_list.append(a - b)
        elif string == '.':
            res = stack_list.pop()
            if stack_list:
                print('error')
                break
            else:
                print(res)
