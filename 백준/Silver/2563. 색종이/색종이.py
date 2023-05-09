import sys
read = sys.stdin.readline

# 겹치는게 문제가 아니다 일단 주어진 숫자만큼 숫자 1을 부여하고,
# 종이에 1의 총 개수를 구하면 되는 문제이다.

n = int(read())
# 100 x 100 사이즈를 dp로 만든다.
paper = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

answer = 0
for i in paper:
    answer += i.count(1)
print(answer)