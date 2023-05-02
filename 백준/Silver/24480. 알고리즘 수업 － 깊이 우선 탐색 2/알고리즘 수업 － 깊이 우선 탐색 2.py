import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

n , m , start = map(int,read().split())
graph = [[] for _ in range(n+1)]
isVisited = [0] * (n+1)
count = 0

for _ in range(m):
    a , b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)
    # print(graph)
for node in graph:
    node.sort(reverse=True)
# print(graph)

def dfs(s):
    global count
    count += 1
    isVisited[s] = count

    for next in graph[s]:
        if isVisited[next] == 0:
            dfs(next)

dfs(start)
print(*isVisited[1:], sep='\n')