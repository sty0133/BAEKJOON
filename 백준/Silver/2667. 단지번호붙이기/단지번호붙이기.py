import sys
from collections import deque
read = sys.stdin.readline


n = int(read())
nmap = [list(map(int, read().rstrip())) for _ in range(n)]
visited = [ [False]*n for _ in range(n) ]
site = []

# def house(x):
#     dq = deque()
#     dq.append(0)
#     while dq:
#         c = dq.popleft()
#         for next in nmap[c]:
#             for next_in in next:
#                 if next_in == 1:
#                     home.append([next_in,c])
#         dq.append(c + 1)
# print(nmap)

def search(a , b):
    count = 1
    dq = deque()
    dq.append([a , b])
    visited[a][b] = True
    while dq:
        x , y = dq.popleft()

        #4방향
        for dx,dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < n:
                if nmap[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    dq.append([nx,ny])
                    count += 1
        
    return count

for i in range(n):
    for j in range(n):
        if nmap[i][j] == 1 and not visited[i][j]:
            temp = search(i,j)
            site.append(temp)

print(len(site), *sorted(site), sep = '\n')