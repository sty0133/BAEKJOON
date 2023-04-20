import sys
read = sys.stdin.readline

a , b = map(int, read().split())

if b - 45 < 0:
    if a - 1 < 0:
        a = a + 23
    else:
        a = a - 1
    b = b + 15
elif b - 45 >= 0:
    b = b - 45

print(a , b)