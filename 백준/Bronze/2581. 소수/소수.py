import sys
read = sys.stdin.readline

m = int(read())
n = int(read())


def prime_num(min,max):

    temp = []


    for i in range(min, max+1):
        check = True
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    check = False

            if check == True:
                temp.append(i)

    return temp


result = prime_num(m,n)

if len(result) == 0:
    print(-1)
    exit(0)

else:
    p_sum = sum(result)
    p_min = min(result)
    print("{}\n{}".format(p_sum,p_min))