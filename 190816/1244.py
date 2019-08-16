import sys
sys.stdin = open('1244.txt', 'r')

# 입력받기
num_switch = int(input())
switch = list(map(int, input().split()))
num_stu = int(input())
# 학생수만큼 반복하면서 학생의 성별과 숫자를 받아서 조건에 따라 저장된 리스트(switch)를 바꿈
for _ in range(num_stu):
    sex, number = tuple(map(int, input().split()))
    # 남자일 경우(학생이 받은 스위치의 숫자가 인덱스보다 1커서 for문 안의 index를 1만큼 조정)
    if sex == 1:
        for i in range(1, num_switch // number + 1):
            switch[number*i-1] ^= 1
    # 여자일 경우
    else:
        # 학생이 받은 스위치의 숫자가 인덱스보다 1 크므로 조정
        fe_number = number - 1
        # 받은 스위치 숫자는 무조건 바꿔야되지만, for문 안의 조건식에서 두번 적용되도록 구성했기 때문에, 미리 빼서 한번만 적용되도록 함.
        switch[fe_number] ^= 1
        # 제일 길게 바꾸는 경우라도 전체 길이의 반만 반복하면 된다.
        for i in range(1, num_switch // 2):
            # 리스트(switch)의 범위를 벗어날경우 반복문 빠져나감
            if fe_number-i < 0 or fe_number+i == num_switch:
                break
            # 좌우가 같을 경우 리스트(switch)를 바꿈
            if switch[fe_number-i] == switch[fe_number+i]:
                switch[fe_number-i] ^= 1
                switch[fe_number+i] ^= 1
            # 같지 않게 되었을 경우 이 이상 반복할 이유가 없으므로 반복문 종료
            else:
                break
# 리스트를 문자열로 바꿈
count = 0
for i in switch:
    count += 1
    if count > 20:
        count -= 20
        print(end='\n')
    print('1 ', end='') if i else print('0 ', end='')
