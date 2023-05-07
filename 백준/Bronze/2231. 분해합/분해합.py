import sys
read = sys.stdin.readline

N = int(read())
M = 0

for i in range(N , -1 , -1):
    M_list = []
    M = N - i
    for j in str(M):
        M_list.append(j)
    M_list = list(map(int, M_list))
    if M + sum(M_list) == N:
        print(M)
        exit()
    elif i == 0 and M + sum(M_list) != N:
        print(0)