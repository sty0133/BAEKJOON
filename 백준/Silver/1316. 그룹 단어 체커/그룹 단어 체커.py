import sys
read = sys.stdin.readline

n = int(read().rstrip())
cnt = n
word = [0] * n

for i in range(n):
    seq = []
    word[i] = read().rstrip()
    A = list(word[i])
    for j in range(len(A)-1):
        if A[j] == A[j+1]:
            seq.append(A[j])
        elif A[j] != A[j+1]:
            if A[j+1] in seq:
                cnt -= 1
                break
            else:
                seq.append(A[j])

print(cnt)