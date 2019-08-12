import sys
sys.stdin = open('GNS_test_input.txt', 'r')

gns = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
for test_case in range(1, int(input()) + 1):
    test_number, len_arr = input().split()
    str_arr = input().split()
    count = [0] * 10
    for i in range(int(len_arr)):
        for j in range(10):
            if gns[j] == str_arr[i]:
                count[j] += 1
                break
    print('{}'.format(test_number))
    for i in range(10):
        for _ in range(count[i]):
            print('{} '.format(gns[i]), end='')
        print()



