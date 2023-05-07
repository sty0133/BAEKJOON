import sys
read = sys.stdin.readline

n = int(read())
a = 666
cnt = 0

while True:
    if "666" in str(a):
        cnt += 1
        if cnt == n:
            print(a)
            exit()
    a += 1