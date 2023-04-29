import sys
read = sys.stdin.readline

m , n = map(int, read().rstrip().split())
primenum = []

for i in range(m , n+1):
    count = 0
    if i > 1:
        for j in range(2 , int(i**0.5) + 1):
            if i % j == 0:
                count = 1
                break
        if count == 0:
            primenum.append(i)
primenum = sorted(primenum)
print(*primenum, sep=' \n')