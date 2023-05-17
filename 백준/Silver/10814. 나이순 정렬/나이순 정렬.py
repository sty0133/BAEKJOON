import sys
read = sys.stdin.readline

cases = int(read())
arr = [[] for _ in range(cases)]

for i in range(cases):
    age , name = map(str, read().rstrip().split())
    age = int(age)
    arr[i].extend([age , name])

arr.sort(key= lambda x : x[0])

for i in range(cases):
    print(arr[i][0] , arr[i][1])