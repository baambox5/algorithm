import sys
sys.stdin = open('4408.txt', 'r')

for test_case in range(1, int(input()) + 1):
    num_stu = int(input())
    room = [0] * 401
    # 학생 수 만큼 입력 받고, 입력받자마자 처리
    for i in range(num_stu):
        room_1, room_2 = tuple(map(int, input().split()))
        # 홀수일 경우 짝수와의 인덱스 맞추기
        if room_1 % 2:
            room_1 += 1
        if room_2 % 2:
            room_2 += 1
        # 역방향으로 가는 경우
        if room_1 > room_2:
            start = room_2
            end = room_1
        # 정방향으로 가는 경우
        else:
            start = room_1
            end = room_2
        # 해당되는 경로에 숫자 쌓기
        for j in range(start, end + 1):
            room[j] += 1
    # 가장 많이 쌓인 값 찾기
    max_count = 0
    for i in range(1, 401):
        if room[i] > max_count:
            max_count = room[i]
    print('#{} {}'.format(test_case, max_count))


    