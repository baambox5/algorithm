import sys
sys.stdin = open('ladder.txt', 'r')

for _ in range(1, 11):
    test_case = input()
    arr = [[] for _ in range(100)]
    position_y = 0
    # 방향 변수 (0: 내려가는 방향, 1: 오른쪽, -1: 왼쪽)
    direction = 0
    # 입력 받기
    for i in range(100):
        arr[i] = input().split()
    # 첫번째 줄에서 시작할 1들 찾기
    for j in range(100):
        if arr[0][j] == '1':
            # 초기 위치 설정
            position_y = j
            # 위에서부터 아래로 계속해서 내려간다. 단, 옆으로 이동할 때만 제외하고
            for i in range(1, 100):
                # 옆으로 이동하기 위한 반복문 (가능한 크게 잡았다.)
                for _ in range(100):
                    # 위치가 경계선일때 처리
                    if position_y == 0:
                        # 만약 오른쪽이 1이고, 지금까지 내려가고 있었다면 방향을 바꿔준다.
                        if arr[i][position_y + 1] == '1' and direction == 0:
                            direction = 1
                            position_y += 1
                        # 만약 오른쪽에서 인덱스 0으로 다가갈 경우, 그 이상 가면 안되므로 처리
                        if direction == -1:
                            direction = 0
                    elif position_y == 99:
                        if arr[i][position_y - 1] == '1' and direction == 0:
                            direction = -1
                            position_y -= 1
                        if direction == 1:
                            direction = 0
                    # 위치가 경계가 아닌 경우
                    else:
                        if arr[i][position_y + 1] == '1' and direction == 0:
                            direction = 1
                        elif arr[i][position_y - 1] == '1' and direction == 0:
                            direction = -1
                        # 방향에 따라 y축 이동
                        if direction == 1:
                            if arr[i][position_y + 1] == '1':
                                position_y += 1
                            # 만약 더 이상 1이 없으면 방향 바꿔준다.
                            else:
                                direction = 0
                        elif direction == -1:
                            if arr[i][position_y - 1] == '1':
                                position_y -= 1
                            else:
                                direction = 0
                    # 현재 줄에서 방향이 아래로 갈 경우 줄을 바꿔준다.
                    if not direction:
                        break
            # 줄의 끝까지 간 경우
            else:
                if arr[99][position_y] == '2':
                    res = j
                    break  
    print('#{} {}'.format(test_case, res))


