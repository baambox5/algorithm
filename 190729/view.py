def my_max(a, b):
    if a > b:
        return a
    else:
        return b

for input_case in range(1, 11):
    len_horizon = int(input())
    count = 0
    arr = list(map(int, input().split()))
    for i in range(2, len_horizon-2):
        left = 0
        right = 0
        if arr[i] > arr[i-2] and arr[i] > arr[i-1] and arr[i] > arr[i+2] and arr[i] > arr[i+1]:
            left = my_max(arr[i-1], arr[i-2])
            right = my_max(arr[i+1], arr[i+2])
            count += arr[i] - my_max(left, right)

    print('#{} {}'.format(input_case, count))
