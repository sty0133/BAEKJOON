import sys
read = sys.stdin.readline

m = 2
n = int(read().rstrip())

while m <= n:
    if n %  m== 0:
        print(m)
        n = n / m
    else:
        m = m + 1