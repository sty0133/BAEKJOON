import sys
read = sys.stdin.readline


def is_VPS(parenthesis):
    global stack
    check = True

    for i in range(len(parenthesis)):
        if parenthesis[i] == '(':
            stack.append('(')

        elif parenthesis[i] == ')':
            if len(stack) == 0:
                check = False
                break
            else:
                stack.pop()

    if len(stack) != 0:
        check = False

    return check


T = int(read())

for _ in range(T):
    stack = []
    string = read().rstrip()

    if is_VPS(string) == True:
        print("YES")
    else:
        print("NO")

