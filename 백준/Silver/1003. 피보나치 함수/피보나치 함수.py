import sys
read = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(read())

# def fibonacci(x):
#     global case_1
#     global case_0

#     if x == 0:
#         # print(0)
#         case_0.append(0)
#     elif x == 1:
#         # print(1)
#         case_1.append(1)
#     else:
#         fibonacci(x - 1)  
#         fibonacci(x - 2)
    
for i in range(T):
    # case_0 = []
    # case_1 = []
    # fibonacci(int(read()))
    # print(case_0.count(0) , case_1.count(1) , sep=" ")
    n  = int(read())
    zero , one = 1 , 0
    for j in range(n):
        zero , one = one , zero + one
    print(zero , one , sep=" ")