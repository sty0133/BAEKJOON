import sys
read = sys.stdin.readline

n , k = map(int, read().split())
coin = [int(read()) for x in range(n)]
dp = [0 for _ in range(k + 1)]
dp[0] = 1

# https://pacific-ocean.tistory.com/200 참고함
# 전에 풀었던 긴 부분수열이랑 비슷한 느낌
for i in coin:
    for j in range(1, k + 1):
        if j >= i:
            dp[j] += dp[j - i]
print(dp[k])