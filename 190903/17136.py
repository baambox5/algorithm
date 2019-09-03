import sys
sys.stdin = open('17136.txt', 'r')

arr = []
for _ in range(10):
    arr.append(input().split())
print(arr)