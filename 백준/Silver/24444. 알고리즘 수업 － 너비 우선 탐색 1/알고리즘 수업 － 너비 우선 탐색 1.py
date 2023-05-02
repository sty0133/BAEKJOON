import sys
from collections import deque
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

n, m, r = map(int, read().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
count = 1

for _ in range(m):
    a , b = map(int,read().split())
    graph[a].append(b)
    graph[b].append(a)
    
for node in graph:
    node.sort()

def bfs(v):
    global count
    q = deque([r])
    visited[r] = 1
    while q:
        v = q.popleft()
        for g in graph[v]:
            if visited[g] == 0:
                count += 1
                visited[g] = count
                q.append(g)
bfs(r)
print(*visited[1:] , sep='\n')