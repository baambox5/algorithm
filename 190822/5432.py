import sys
sys.stdin = open('5432.txt', 'r')

# 쇠막대기 자르기
for test_case in range(1, int(input()) + 1):
    str_in = input()
    blanket = 0
    res = 0
    for i in range(len(str_in)):
        if str_in[i] == '(':
            blanket += 1
        elif str_in[i] == ')' and str_in[i-1] == '(':
            blanket -= 1
            res += blanket
        else:
            blanket -= 1
            res += 1
    print('#{} {}'.format(test_case, res))
