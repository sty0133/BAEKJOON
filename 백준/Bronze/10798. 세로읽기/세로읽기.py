import sys
read = sys.stdin.readline
a = [list(map(str , read().rstrip())) for _ in range(5)]
# print(len(a))
# print(a)
for i in range(15):
    for j in range(15):
        try:
            print(a[j][i], end='')
        except:
            pass