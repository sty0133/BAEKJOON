import sys
read = sys.stdin.readline

n = int(read())
a = [int(x) for x in read().split()]
# print(a)
dp = [0] * n
dp_reverse = [0] * n

# 앞에서부터 가장 긴 수열을 찾는다
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
# print(max(dp))

# 뒤에서부터 가장 긴 수열을 찾는다
for i in range(n - 1 , -1 , -1):
    for j in range(n - 1, i , -1):
        if a[i] > a[j] and dp_reverse[i] < dp_reverse[j]:
            dp_reverse[i] = dp_reverse[j]
    dp_reverse[i] += 1

for i in range(n):
    dp[i] = dp[i] + dp_reverse[i]

# 앞에서부터 의 해당숫자까지의 길이와 뒤에서부터 해당숫자까지의 길이를 구했으니,
# 해당숫자가 겹치게 되기때문에 빼줘야한다.
print(max(dp) - 1)