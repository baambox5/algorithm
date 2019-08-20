import sys
sys.stdin = open('4873.txt', 'r')


def same_char(chars):
    new_chars = ''
    i = 0
    count = 0
    while i < len(chars):
        if i == len(chars) - 1:
            new_chars += chars[i]
        else:
            if chars[i] == chars[i + 1]:
                i += 1
                count = 1
            else:
                new_chars += chars[i]
        i += 1
    if count:
        return same_char(new_chars)
    else:
        return len(chars)


for test_case in range(1, int(input()) + 1):
    str_in = input()
    res = same_char(str_in)
    print('#{} {}'.format(test_case, res))
