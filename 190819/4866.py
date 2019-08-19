import sys
sys.stdin = open('4866.txt', 'r')


def push(item):
    s.append(item)


def pop():
    if len(s) == 0:
        return
    else:
        return s.pop(-1)


def is_empty():
    return True if len(s) else False


for test_case in range(1, int(input()) + 1):
    global s
    s = []
    str_in = input()
    res = 1
    for char in str_in:
        if char == '(' or char == '{':
            push(char)
        else:
            if (char == ')' and pop() != '(') or (char == '}' and pop() != '{'):
                res = 0
                break
    else:
        if is_empty():
            res = 0
    print('#{} {}'.format(test_case, res))
