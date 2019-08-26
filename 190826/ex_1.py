str_in = '2+3*4/5'

stack_list = []
for char in str_in:
    if char.isdigit():
        print(char, end='')
    elif char == '(' or char == '*' or char == '/' or char == '+' or char == '-':
        stack_list.append(char)
    elif char == ')':
        while stack_list:
            pop_char = stack_list.pop()
            if pop_char == '(':
                break
            else:
                print(pop_char, end='')
else:
    while stack_list:
        print(stack_list.pop(), end='')
