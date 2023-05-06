import sys
read = sys.stdin.readline

N = int(read())
meetingTime = []
for i in range(N):
    meetingTime.append(list(map(int, read().split())))
# print(meetingTime)

#시작 시간과 끝나는 시간을 오름차순으로 정렬하여,
#빨리 끝나는거부터 선별할수있다.
meetingTime.sort(key = lambda x:(x[1] , x[0]))
# print(meetingTime)

count = 1
endTime = meetingTime[0][1]
for i in range(1,N):
    if meetingTime[i][0] >= endTime:
        count += 1
        endTime = meetingTime[i][1]
print(count)