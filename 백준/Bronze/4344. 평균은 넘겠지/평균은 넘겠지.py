import sys
read = sys.stdin.readline

t = int(read().rstrip())

for _ in range(t):
    arr = list(map(int, read().rstrip().split()))
    # print(arr)
    average = sum(arr[1:]) // arr[0]
    # print(average)
    count = 0
    for j in range(arr[0]):
        if arr[j + 1] > average:
            count += 1
    # print(count)
    print("{:.3f}%".format(count / arr[0] * 100))