import sys
read = sys.stdin.readline

n = int(read().rstrip())
arr = list(map(int , read().rstrip().split()))
setarr = sorted(list(set(arr)))
result = {}

# print(setarr)
# 시간초과
# for i in range(len(setarr)):
#     cnt = 0
#     for j in range(len(setarr)):
#         if setarr[i] > setarr[j]:
#             cnt += 1
#     # print(cnt)
#     if cnt > 0:
#         for k in range(n):
#             if setarr[i] == arr[k]:
#                 result[k] = cnt

for i in range(len(setarr)):
    result[setarr[i]] = i
for i in arr:        
    print(result[i], end = " ")