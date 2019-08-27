import sys
sys.stdin = open('input.txt', 'r')

for test_case in range(1, 11):
    len_in = int(input())
    stack_list = []
    calc_list = []
    top = -1
    for char in input():
        if char.isdecimal():
            calc_list.append(char)
        elif char == '(':
            stack_list.append(char)
            top += 1
        elif char == '*':
            if stack_list[top] == char:
                calc_list.append(stack_list.pop())
                top -= 1
            stack_list.append(char)
            top += 1
        elif char == '+':
            if stack_list[top] == '*' or stack_list[top] == char:
                calc_list.append(stack_list.pop())
                top -= 1
            stack_list.append(char)
            top += 1
        elif char == ')':
            while stack_list:
                stack = stack_list.pop()
                top -= 1
                if stack == '(':
                    break
                else:
                    calc_list.append(stack)
    for calc in calc_list:
        if calc.isdecimal():
            stack_list.append(int(calc))
        elif calc == '+' or calc == '*':
            b = stack_list.pop()
            a = stack_list.pop()
            if calc == '+':
                stack_list.append(a + b)
            elif calc == '*':
                stack_list.append(a * b)
    print('#{} {}'.format(test_case, stack_list.pop()))
            