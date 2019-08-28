import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

# for test_case in range(1, int(input()) + 1):
#     str_in = input()
#     dict_str = {}
#     count = 0
#     temp = ''
#     print('#{}'.format(test_case), end=' ')
#     for i in range(len(str_in)):
#         if str_in[i].isdecimal():
#             count += 1
#             temp += str_in[i]
#         if count == 2:
#             if str_in[i-2] in dict_str:
#                 if temp in dict_str[str_in[i-2]]:
#                     print('ERROR')
#                     break
#                 else:
#                     dict_str[str_in[i-2]] += [temp]
#             else:
#                 dict_str[str_in[i-2]] = [temp]
#             count = 0
#             temp = ''
#     else:
#         if 'S' not in dict_str:
#             res_s = 13
#         else:
#             res_s = 13-len(dict_str['S'])
#         if 'D' not in dict_str:
#             res_d = 13
#         else:
#             res_d = 13-len(dict_str['D'])
#         if 'H' not in dict_str:
#             res_h = 13
#         else:
#             res_h = 13-len(dict_str['H'])
#         if 'C' not in dict_str:
#             res_c = 13
#         else:
#             res_c = 13-len(dict_str['C'])
#         print('{} {} {} {}'.format(res_s, res_d, res_h, res_c))


for test_case in range(1, int(input()) + 1):
    q = deque()
    str_in = input()
    for char in str_in:
        q.append(char)
    visit_s = [0] * 14
    visit_d = [0] * 14
    visit_h = [0] * 14
    visit_c = [0] * 14
    print('#{}'.format(test_case), end=' ')
    error = 1
    while q:
        char = q.popleft()
        temp = q.popleft()
        temp += q.popleft()
        if char == 'S':
            if visit_s[int(temp)]:
                print('ERROR')
                error = 0
                break
            else:
                visit_s[int(temp)] = 1
        elif char == 'D':
            if visit_d[int(temp)]:
                print('ERROR')
                error = 0
                break
            else:
                visit_d[int(temp)] = 1
        elif char == 'H':
            if visit_h[int(temp)]:
                print('ERROR')
                error = 0
                break
            else:
                visit_h[int(temp)] = 1
        else:
            if visit_c[int(temp)]:
                print('ERROR')
                error = 0
                break
            else:
                visit_c[int(temp)] = 1
    if error:
        res_s = 0
        res_d = 0
        res_h = 0
        res_c = 0
        for i in range(1, 14):
            if visit_s[i]:
                res_s += 1
            if visit_d[i]:
                res_d += 1
            if visit_h[i]:
                res_h += 1
            if visit_c[i]:
                res_c += 1
        print('{} {} {} {}'.format(13-res_s, 13-res_d, 13-res_h, 13-res_c))
