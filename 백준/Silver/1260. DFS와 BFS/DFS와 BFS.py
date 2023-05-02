import sys
from collections import deque
sys.setrecursionlimit(10**6)

read = sys.stdin.readline

n , m , v = map(int, read().split())
graph = [[]for _ in range(n + 1)]
visited_dfs = [0] * (n + 1)
visited_bfs = [0] * (n + 1)
cnt_dfs = []
cnt_bfs = []
visited_bfs[v] = 1
visited_dfs[v] = 1
cnt_bfs.append(v)
cnt_dfs.append(v)


for _ in range(m):
    a ,b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

for node in graph:
    node.sort()
# print(graph)

def dfs(x):
    global cnt_dfs
    for next_dfs in graph[x]:
        if visited_dfs[next_dfs] == 0:
            visited_dfs[next_dfs] = 1
            cnt_dfs.append(next_dfs)
            dfs(next_dfs)

def bfs(u):
    global cnt_bfs
    dq = deque()
    dq.append(u)
    while dq:
        c = dq.popleft()
        for next_bfs in graph[c]:
            if visited_bfs[next_bfs] == 0:
                visited_bfs[next_bfs] = 1
                cnt_bfs.append(next_bfs)
                dq.append(next_bfs)

dfs(v)
print(*cnt_dfs,sep=' ')
bfs(v)
print(*cnt_bfs,sep=' ')
