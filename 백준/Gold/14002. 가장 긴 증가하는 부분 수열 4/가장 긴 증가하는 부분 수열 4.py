import sys
read = sys.stdin.readline

n = int(read())
a = [int(x) for x in read().split()]
dp = [0] * n
nums = []

for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
    
print(max(dp))
h = max(dp)
for i in range(n - 1 , -1 , -1):
    if dp[i] == h:
        nums.append(a[i])
        h -= 1
nums.reverse()

print(*nums)