import sys
read = sys.stdin.readline

N = int(read().rstrip())
N_num = list(map(int, read().split()))
N_num.sort()
M = int(read().rstrip())
M_num = list(map(int, read().split()))

for num in M_num:
    first, last = 0, N - 1
    find = False
    while first <= last:
        mid = (first + last) // 2
        if num == N_num[mid]:
            find = True
            print("1")
            break
        elif num > N_num[mid]:
            first = mid + 1
        else:
            last = mid -1

    if not find:
        print("0") 