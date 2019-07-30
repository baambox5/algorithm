import sys
sys.stdin = open('input_Flatten.txt', 'r')

for test_case in range(1, 11):
    dump_count = int(input())
    arr = list(map(int, input().split()))

    count_list = [0] * 101
    max_count = 0
    min_count = 0
    for i in arr:
        count_list[i] += 1
    for i in range(dump_count):
        for j in range(1, 101):
            if count_list[j]:
                min_count = j
                count_list[j] -= 1
                count_list[j+1] += 1
                break
        for j in range(100, 1, -1):
            if count_list[j]:
                max_count = j
                count_list[j] -= 1
                count_list[j-1] += 1
                break
        if (max_count-min_count) <= 1:
            break
    for j in range(1, 101):
        if count_list[j]:
            min_count = j
            break
    for j in range(100, 1, -1):
        if count_list[j]:
            max_count = j
            break
    print('#{} {}'.format(test_case, max_count - min_count))

    # max_idx = 0
    # min_idx = 0
    # for i in range(dump_count):
    #     for j in range(100):
    #         if arr[max_idx] < arr[j]:
    #             max_idx = j
    #         if arr[min_idx] > arr[j]:
    #             min_idx = j
    #     arr[max_idx] -= 1
    #     arr[min_idx] += 1
    #     if (arr[max_idx]-arr[min_idx]) <= 1:
    #         break
    # for i in range(1, 100):
    #     if arr[max_idx] < arr[i]:
    #         max_idx = i
    #     if arr[min_idx] > arr[i]:
    #         min_idx = i
    #
    # print('#{} {}'.format(test_case, arr[max_idx] - arr[min_idx]))

