import sys
read = sys.stdin.readline

n = int(read())
stack = []

for i in range(n):
    a = read().split()

    if a[0] == "push":
        stack.append(a[1])
    elif a[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()    
    elif a[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif a[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == "size":
        print(len(stack))