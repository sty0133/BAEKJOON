import sys
read = sys.stdin.readline

N = int(read())
a = list(map(int, read().split()))
sums = [a[0]]

#모두 음수일때 최솟값만 출력
#굳이 반복문까지 안가고 모두 음수일때 코드를 끝낼수 있음.
def isAllNegative():
    if max(a) < 0:
        print(max(a))
        exit()

isAllNegative()

for i in a[1:]:
    sums.append(max(sums[-1] + i, i))
print(max(sums))
# print(sums)