import sys
read = sys.stdin.readline

t = int(read().rstrip())
arr = []
for i in range(t):
    arr.append(list(map(int , read().rstrip().split())))
arr.sort(key = lambda x : (x[1] , x[0]))
for i in range(t):
    print(arr[i][0] , arr[i][1])