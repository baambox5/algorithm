import sys
sys.stdin = open('color_paper.txt', 'r')

N = int(input())
arr = []
paper_number = 0
count = [0] * 101
for i in range(101):
    arr.append([0] * 101)
for i in range(N):
    paper_in = list(map(int, input().split()))
    paper_number += 1
    for j in range(paper_in[2]):
        for k in range(paper_in[3]):
            arr[paper_in[0]+j][paper_in[1]+k] = paper_number
for i in range(101):
    for j in range(101):
        count[arr[i][j]] += 1
for i in range(1, N + 1):
    print(count[i])