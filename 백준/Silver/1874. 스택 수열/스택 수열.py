import sys
read = sys.stdin.readline

n = int(read())
poped = []
stack = []
start = 1
can = 0

for i in range(n):
    a = int(read())
    # targetStack.append(a)
    # targetStack.append(a)
    # for j in range(1 , n + 1):
    #     if 
    #     stack.append(j)
    #     print("+")
    # for j in range(1 , a+1):
    #     if not stack and not poped:
    #         stack.append(j)
    #         print("+")
    #         if stack[-1] == a:
    #             stack.pop(a)
    #             poped.append(a)
    #             print("-")
    #     elif a in stack:
    #         stack.pop(a)
    #         print("-")
# for i in targetStack:
#     for j in range(1 , i + 1):
#         if stack[-1] != targetStack[i]:
#             stack[j] = 
#             print("+")
#         else:
#             stack.pop(stack[-1])
#             print("-")
    while start <= a:
        stack.append(start)
        poped.append("+")
        start += 1
    
    if stack[-1] == a:
        stack.pop()
        poped.append("-")
    else:
        print("NO")
        can = 1
        break
if can == 0:
    for i in poped:
        print(i)

          


# print(targetStack , stack)

# for i in targetStack:
#     if not stack == i:
#         for j in range(stack[-1] , i + 1):
