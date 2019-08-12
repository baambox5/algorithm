cnt = 0
def printHello(i, n):
    global cnt
    if i == n:
        cnt += 1
        return
    printHello(i + 1, n)
    printHello(i + 1, n)
    # n이 종료 조건
    # 함수를 처음 한 번 호출하면 2개의 자기자신이 호출된다.
    # 그 다음이 되면 2개의 자기자신은 각각 2개를 또 호출한다.
    # 이런 과정을 종료조건인 n번 만큼 반복하게 된다면 결과적으로 2의 n승 만큼의 종료조건을 만나게 된다.

printHello(0, 3)
print(cnt)