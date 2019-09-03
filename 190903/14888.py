import sys
sys.stdin = open('14888.txt', 'r')
from sys import *
setrecursionlimit(10 ** 6)

def perm(k, visit, res):
    global max_value, min_value
    if k == N-1:        
        if res > max_value:
            max_value = res
        if res < min_value:
            min_value = res
    else:
        for i in range(N - 1):
            if not visit & (1 << i):
                temp = res
                if operator[i] == '+':
                    temp += arr[k+1]
                elif operator[i] == '-':
                    temp -= arr[k+1]
                elif operator[i] == '*':
                    temp *= arr[k+1]
                elif operator[i] == '/':
                    if temp < 0:
                        temp = -temp
                        temp //= arr[k+1]
                        temp = -temp
                    else:
                        temp //= arr[k+1]
                perm(k + 1, visit | (1 << i), temp)


N = int(input())
arr = list(map(int, input().split()))
d_count = input().split()
operator = []
operator += ['+'] * int(d_count[0])
operator += ['-'] * int(d_count[1])
operator += ['*'] * int(d_count[2])
operator += ['/'] * int(d_count[3])
max_value = -1000000000
min_value = 1000000000
perm(0, 0, arr[0])
print(max_value)
print(min_value)