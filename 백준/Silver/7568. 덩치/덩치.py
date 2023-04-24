import sys
read = sys.stdin.readline

n = int(read().rstrip())
data = []
rank = []

for i in range(n):
    a,b = map(int, read().rstrip().split())
    data.append((a,b))

for i in range(n):
    count = 0
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            count += 1
    rank.append(count + 1)

for i in rank:
    print(i, end=" ")