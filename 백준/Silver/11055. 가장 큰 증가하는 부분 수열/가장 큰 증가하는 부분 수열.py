import sys
read = sys.stdin.readline

n = int(read())
a = list(map(int , read().split()))

dp = a[:]
dp[0] = a[0]

# 인덱스의 개수가 n보다 크면 조기종료
if len(a) > n:
    exit()
# 문제 자체가 이해가안되서 인터넷 참고.
# 1. 수열에서 자신보다 앞 쪽에 있는 값 중에서 자신보다 작은 값의 인덱스를 찾는다.
# 2. 해당 인덱스의 dp값중 가장 큰 값과 자신의 값을 더해 dp를 다시 채운다.
else:
    for i in range(1, n):
        for j in range(i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j] + a[i])

print(max(dp))