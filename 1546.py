import sys
read = sys.stdin.readline

N = int(read())
score = [int(i) for i in input().split()]
average = 0
M = max(score)

for j in range(N):
    score[j] = score[j] / M * 100
    average += score[j]

print(average / N)