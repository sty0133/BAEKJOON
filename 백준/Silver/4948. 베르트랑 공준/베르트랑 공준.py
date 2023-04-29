import sys
read = sys.stdin.readline

aPrimeNum = [False] + [True] * (123456 * 2)
aPrimeNum[1] = False

for i in range(2 , len(aPrimeNum)):
    if aPrimeNum[i] == True:
        for j in range(2 * i , len(aPrimeNum) , i):
            aPrimeNum[j] = False

while True:
    n = int(read())
    if n == 0:
        break
    else:
        primenum = []
        for i in range(n + 1 , (n*2) + 1):
            if aPrimeNum[i] == True:
                primenum.append(1)

    print(len(primenum))