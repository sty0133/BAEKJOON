import sys
read = sys.stdin.readline

m = int(read().rstrip())
n = int(read().rstrip())
primenum = []

for i in range(m,n+1):
    count = 0
    if i > 1:
        # primenum.append(i)
        for j in range(2,i):
            if i % j == 0:
                count = 1
                break
        if count == 0:
            primenum.append(i)
# print(primenum)
if len(primenum) == 0:
    print(-1)
else:
    print(sum(primenum))
    print(min(primenum))

