import sys
from collections import deque

read = sys.stdin.readline
n , m , r = map(int, read().split())
graph = [[]for _ in range(n + 1)]
visited = [0] * (n + 1)
count = 1

for _ in range(m):
    a , b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

for node in graph:
    node.sort(reverse=True)
# print(graph)

def bfs(x):
    global count
    dq = deque()
    dq.append(x)
    visited[x] = 1
    while dq:
        v = dq.popleft()
        for next in graph[v]:
            if visited[next] == 0:
                count += 1
                visited[next] = count
                dq.append(next)

bfs(r)
print(*visited[1:] , sep='\n')
