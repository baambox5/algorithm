import sys
sys.stdin = open('2007.txt', 'r')

for test_case in range(1, int(input()) + 1):
    str_in = input()
    words = ''
    words += str_in[0]
    flag = 1
    for i in range(1, 10):
        if str_in[0] == str_in[i]:
            for j in range(1, len(words)):
                if words[j] != str_in[i + j]:
                    break
            else:
                flag = 0
                continue
            words += str_in[i]
        else:
            if flag:
                words += str_in[i]
    print('#{} {}'.format(test_case, len(words)))
