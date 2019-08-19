import sys
sys.stdin = open('palindrome2.txt', 'r')

for test_case in range(1, 11):
    input()
    arr = []
    M = 0
    # 입력 받기
    for i in range(100):
        arr += [input()]
    for i in range(100):
        # 가로줄 체크, j는 처음에 회문의 최대 길이 100이라고 가정하고 거기서부터 회문의 길이를 1씩 줄여나가며(가정) 체크
        for j in range(100, M, -1):
            # 위에서 가정한 길이가 j인 회문을 현재의 가로줄 안의 열의 초기 위치를 1씩 바꿔가며 체크(ex- (0~j)->(1~j+1)->...->(100-j~100)
            for k in range(101 - j):
                # 회문인지 체크(길이 j인 회문이 회문이 맞는지 체크)
                e = j + k - 1
                for l in range(j // 2):
                    if arr[i][k+l] != arr[i][e-l]:
                        break
                else:
                    M = j
                    break
            if M >= j:
                break
        # 세로줄 체크
        for j in range(100, M, -1):
            for k in range(101 - j):
                e = j + k - 1
                for l in range(j // 2):
                    if arr[k+l][i] != arr[e-l][i]:
                        break
                else:
                    M = j
                    break
            if M >= j:
                break
    print('#{} {}'.format(test_case, M))
