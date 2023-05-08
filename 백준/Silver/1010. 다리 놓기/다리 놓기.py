import sys
read = sys.stdin.readline

T = int(read())

# N = 1 일때 답은 M
# N == M 일때 답은 1

for _ in range(T):
    N , M = map(int, read().split())
    dp = [[1 for i in range(M+1)] for j in range(N+1)]
    for i in range(1 , N + 1):
        for j in range(1 , M + 1):
            if i == 1:
                dp[i][j] = j
            if i == j:
                dp[i][j] = 1
            else:
                if j > i:
                    # 핵심이였음
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
    print(dp[N][M])