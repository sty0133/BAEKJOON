import sys
from collections import deque
read = sys.stdin.readline

computer = int(read())
networkLine = int(read())
network = [[] for _ in range(computer + 1)]
haveVirus = [0] * (computer + 1)
haveVirus[1] = 1
cnt = 0

for _ in range(networkLine):
    a , b = map(int, read().split())
    network[a].append(b)
    network[b].append(a)

def virus(x):
    global cnt
    dq = deque()
    dq.append(x)
    while dq:
        v = dq.popleft()
        if len(haveVirus) == computer:
            print(computer)
        for c in network[v]:
            if haveVirus[c] == 0:
                haveVirus[c] = 1
                cnt += 1
                dq.append(c)

virus(1)
print(cnt)