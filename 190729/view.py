def my_max(a, b):
    if a > b:
        return a
    else:
        return b

# 총 10개 받는다고 해서 10번 반복으로 고정
for input_case in range(1, 11):
    # 테스트 개수 입력받기
    len_horizon = int(input())
    count = 0
    # 입력 받은 테스트 리스트로 바꿈
    arr = list(map(int, input().split()))
    # 조건에 맞는지 반복문 돌리면서 계산
    for i in range(2, len_horizon-2):
        # 왼쪽, 오른쪽 변수 하나씩 지정해서 한번 체크할때마다 초기화
        left = 0
        right = 0
        # 해당되는 위치가 조건이 다 맞는 경우(제일 높음)
        if arr[i] > arr[i-2] and arr[i] > arr[i-1] and arr[i] > arr[i+2] and arr[i] > arr[i+1]:
            #  직접 정의한 큰 값 찾는 함수 불러서 그 중 가장 큰 값을 찾는다.
            left = my_max(arr[i-1], arr[i-2])
            right = my_max(arr[i+1], arr[i+2])
            # 왼쪽, 오른쪽 중에 큰 값과 비교한 결과를 계속해서 넣어준다.
            count += arr[i] - my_max(left, right)
    # 출력
    print('#{} {}'.format(input_case, count))
