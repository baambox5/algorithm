import sys
sys.stdin = open('secret_code_scan.txt', 'r')

code = {(2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2, (4, 1, 1): 3, (1, 3, 2): 4, (2, 3, 1): 5,
        (1, 1, 4): 6, (3, 1, 2): 7, (2, 1, 3): 8, (1, 1, 2): 9}
hex_char = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def hextobi(char):
    if char.isdecimal():
        num = int(char)
    else:
        num = hex_char[char]
    if num == 0:
        res = '0000'
    elif num < 2:
        res = '000'
    elif num < 4:
        res = '00'
    elif num < 8:
        res = '0'
    else:
        res = ''
    temp = ''
    while num > 0:
        temp += str(num % 2)
        num //= 2
    for i in range(len(temp) - 1, -1, -1):
        res += temp[i]
    return res


for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    str_in = ''
    column_idx = 0
    visit = [0] * M
    bi_list = []
    n = 0
    res = 0
    for _ in range(N):
        bi_code = ''
        str_in = input()
        for i in range(M):
            if str_in[i] != '0' and not visit[i]:
                column_idx = i
                break
        if column_idx:
            zero_count = 0
            for i in range(column_idx - 1, M):
                if zero_count >= 3:
                    continue
                if str_in[i] == '0' and visit[i]:
                    visit[i] = 0
                else:
                    if str_in[i] == '0':
                        zero_count += 1
                    else:
                        zero_count = 0
                        visit[i] = 1
                    bi_code += hextobi(str_in[i])
            else:
                column_idx = 0
                n += 1
                bi_list += [bi_code]
    for i in range(len(bi_list)):
        res_code = [0] * 8
        count = 7
        count_1, count_2, count_3 = 0, 0, 0
        for j in range(len(bi_list[i]) - 1, -1, -1):
            if bi_list[i][j] != '0':
                column_idx = j
                break
        j = column_idx
        min_count = 0
        while j > 0:
            if count == -1:
                break
            if not count_2 and bi_list[i][j] == '1':
                count_1 += 1
            elif count_1 and not count_3 and bi_list[i][j] == '0':
                count_2 += 1
            elif count_2 and bi_list[i][j] == '1':
                count_3 += 1
            elif count_3 and bi_list[i][j] == '0':
                if not min_count:
                    min_count = count_1
                    if min_count > count_2:
                        min_count = count_2
                    if min_count > count_3:
                        min_count = count_3
                count_1, count_2, count_3 = count_1 // min_count, count_2 // min_count, count_3 // min_count
                if (count_3, count_2, count_1) in code:
                    res_code[count] = code[(count_3, count_2, count_1)]
                    j -= (7 - count_1 - count_2 - count_3) * min_count
                else:
                    j += count_3 * min_count
                count_1, count_2, count_3 = 0, 0, 0
                count -= 1
                continue
            j -= 1
        odd = res_code[0] + res_code[2] + res_code[4] + res_code[6]
        even = res_code[1] + res_code[3] + res_code[5] + res_code[7]
        if not (odd*3 + even) % 10:
            res += odd + even
    print('#{} {}'.format(test_case, res))






