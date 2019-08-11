import sys
sys.stdin = open('card_number.txt', 'r')

N = int(input())
N_number = input().split()
M = int(input())
M_number = input().split()

res = ''
k = 0
for i in range(M):
    for j in range(k, N):
        if M_number[i] == N_number[j]:
            N_number[j], N_number[k] = N_number[k], N_number[j]
            k += 1            
            res += '1' if i == M-1 else '1 '
            break
    else:
        res += '0' if i == M-1 else '0 '
print(res)


# for i in M_number:
#     res += '1 ' if i in N_number else '0 '
# print(res)
    