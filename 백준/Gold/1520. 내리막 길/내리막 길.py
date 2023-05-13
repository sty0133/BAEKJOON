import sys
read = sys.stdin.readline
#이 문제는 DFS를 사용해야 한다.
sys.setrecursionlimit(10**6)

n , m = map(int, read().split())
mountain = [list(map(int, read().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
moveRange = [[1 , 0] , [0 , 1] , [-1 , 0] , [0 , -1]]
# print(mountain)


#   https://seongonion.tistory.com/109
#   https://fre2-dom.tistory.com/251
#   https://studyandwrite.tistory.com/387 를 참고함.
def dfs(x , y):
    if x == n - 1 and y == m - 1:
        return 1
    
    if visited[x][y] != -1:
        return visited[x][y]

    visited[x][y] = 0
    
    for move in moveRange:
        nx , ny = move[0] + x , move[1] + y

        if 0 <= nx < n and 0 <= ny < m:
            if mountain[x][y] > mountain[nx][ny]:
                visited[x][y] += dfs(nx , ny)

    return visited[x][y]

print(dfs(0,0))