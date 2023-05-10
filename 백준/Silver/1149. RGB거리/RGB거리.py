import sys
read = sys.stdin.readline

n = int(read())
rgb = [[0] for _ in range(n)]

for i in range(n):
    rgb[i] = list(map(int , read().split()))

# R 로 시작하면 다음껀 i -1 이랑 색만 다르면 되니까,
# R 로 시작하면서 두번째 집의 G B 중 G 를 선택했으면 
# 다음집은 R B 의 값을 더해서 두번째 집의 B를 선택했을 경우 똑같이 더해서 최솟값을 구해야 한다?

# https://velog.velcdn.com/images%2Fhope1213%2Fpost%2F7bf8fb5f-1c91-4b99-bf8f-36242dea574f%2Fimage.png
# 이미지 참고

for i in range(1 , len(rgb)):
    rgb[i][0] = min(rgb[i - 1][1] , rgb[i - 1][2]) + rgb[i][0]
    rgb[i][1] = min(rgb[i - 1][0] , rgb[i - 1][2]) + rgb[i][1]
    rgb[i][2] = min(rgb[i - 1][0] , rgb[i - 1][1]) + rgb[i][2]

print(min(rgb[n - 1][0] , rgb[n - 1][1] , rgb[n - 1][2]))