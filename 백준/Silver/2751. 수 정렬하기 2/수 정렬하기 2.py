import sys
read = sys.stdin.readline

n = int(read())
arr = []
for i in range(n):
    arr.append(int(read()))
# print(arr)
arr.sort(key = lambda x : x)
print(*arr, sep = '\n')