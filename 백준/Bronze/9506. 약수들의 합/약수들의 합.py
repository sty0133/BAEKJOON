import sys
read = sys.stdin.readline

while True:
    measure = []
    n = int(read())

    if n == -1:
        exit()
    else:
        for a in range(1, n):
            if n % a == 0:
                measure.append(a)
        # print(measure)
        if sum(measure) == n:
            # https://blockdmask.tistory.com/468 참고함
            print(n, "=", " + ".join(str(i) for i in measure), sep=" ")
        else:
            print(n, "is NOT perfect.")