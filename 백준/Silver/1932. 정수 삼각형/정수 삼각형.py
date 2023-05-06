import sys
read = sys.stdin.readline

n = int(read())
triangle = []

for i in range(n):
    triangle.append(list(map(int, read().split())))

for i in range(1,n):
  for j in range(len(triangle[i])): 
    if j==0:
      triangle[i][j]=triangle[i][j]+triangle[i-1][j]
    elif j==len(triangle[i])-1: 
      triangle[i][j]=triangle[i][j]+triangle[i-1][j-1]
    else:
      triangle[i][j]=max(triangle[i-1][j-1],triangle[i-1][j])+triangle[i][j]
print(max(triangle[n-1]))