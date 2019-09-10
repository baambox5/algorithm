import sys
sys.stdin = open('bank.txt', 'r')

tet = {0: (1, 2), 1: (0, 2), 2: (0, 1)}

for test_case in range(1, int(input()) + 1):
    binary = []
    for num in input():
        binary += [int(num)]
    len_binary = len(binary)
    tetra = []
    tet_num = 0
    for num in input():
        tetra += [int(num)]
    len_tetra = len(tetra)
    res = 0
    for i in range(len_binary):
        binary[i] ^= 1
        bi_num = 0
        for j in range(len_binary):
            bi_num += binary[j] * 2**(len_binary - 1 - j)
        for j in range(len_tetra):
            for k in range(2):
                tet_num = 0
                for s in range(len_tetra):
                    if s == j:
                        tet_num += tet[tetra[j]][k] * 3**(len_tetra - 1 - j)
                    else:
                        tet_num += tetra[s] * 3**(len_tetra - 1 - s)
                if tet_num == bi_num:
                    res = bi_num
                    break
            if res:
                break
        if res:
            break
        binary[i] ^= 1
    print('#{} {}'.format(test_case, res))
