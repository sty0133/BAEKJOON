import sys
read = sys.stdin.readline

k = int(read().rstrip())
nums = []
# for i in range(k):
#     nums[i] = int(read().rstrip())
#     if nums[0] == 0:
#         continue
#     else:
#         if nums[i] == 0:
#             nums.remove(nums[i-1])
#             nums.remove(nums[i])

# for a in range(len(nums)):
#     sum += nums[a]
# print(a)
# def isZero(zero):
#     if nums[i] == 0:
#         nums.pop()
#         nums.pop()
        
# for i in range(k):
#     nums[i] = int(read().rstrip())
# for i in range(len(nums)):
#     sum += nums[i]
# print(sum)

#     if nums[i] == 0:
#         nums.remove(nums[i])
#         nums.remove(nums[i-1])
#         break
# print(nums)

for i in range(k):
    num = int(read().strip())
    if num == 0:
        nums.pop()
    else:
        nums.append(num)
print(sum(nums))