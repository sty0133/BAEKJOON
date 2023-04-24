import sys
read = sys.stdin.readline

while (True):
    # a = list(read().rstrip())
    # pelin = list(reversed(a))
    # blank = [0] * len(a)
    # if len(a) == 1:
    #     if a[0] == "0":
    #         break
    #     else:
    #         print("YES")
    # else:
    #     for i in range(len(a)):
    #         if a[i] == pelin[i]:
    #             blank.append(1)
    #         else:
    #             blank.append(0)

    #     if len(a) == blank.count(1):
    #         print("yes")
    #     else:
    #         print("no")
        a = read().rstrip()
        if a == "0":
                break
        print('yes' if a == a[::-1] else 'no')