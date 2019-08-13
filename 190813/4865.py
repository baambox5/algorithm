import sys
sys.stdin = open('4865.txt', 'r')

for test_case in range(1, int(input()) + 1):
    str_1 = input()
    dict_str = {}
    for str_char_1 in str_1:
        dict_str[str_char_1] = 0
    str_2 = input()
    for str_char_2 in str_2:
        for str_char_1 in dict_str:
            if str_char_1 == str_char_2:
                dict_str[str_char_1] += 1
    max_count = 0
    for key in dict_str:
        if max_count < dict_str[key]:
            max_count = dict_str[key]
    print('#{} {}'.format(test_case, max_count))
