import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

computer = int(read())
networkLine = int(read())
network = [[] for _ in range(computer + 1)]
haveVirus = [0] * (computer + 1)
haveVirus[1] = 1

for _ in range(networkLine):
    a , b = map(int, read().split())
    network[a].append(b)
    network[b].append(a)

def virus(x):
    global cnt

    for nextcomputer in network[x]:
        if haveVirus[nextcomputer] == 0:
            haveVirus[nextcomputer] = 1
            virus(nextcomputer)

virus(1)
print(haveVirus[2:].count(1))