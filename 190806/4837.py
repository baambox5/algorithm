import sys
sys.stdin = open('4837.txt', 'r')

# 1~12의 숫자를 리스트로 저장
A = list(range(1, 13))
# test case만큼 반복
for test_case in range(1, int(input()) + 1):
    # 입력 받기
    N, K = tuple(map(int, input().split()))
    count = 0
    # 모든 부분집합
    for subset in range(1 << 12):
        B = []
        # 각각의 부분집합을 저장
        for i in range(12):
            if subset & (1 << i):
                B += [A[i]]
        # 만약 부분집합이 입력값 N만큼의 요소를 가지고 있으면 더하는 과정을 시작함.
        if len(B) == N:
            sum_value = 0
            for j in B:
                sum_value += j
            # 만약 더한 값이 입력값 K라면 count를 하나 증가시킴
            if sum_value == K:
                count += 1
    # count 출력
    print('#{} {}'.format(test_case, count))