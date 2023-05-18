import sys
read = sys.stdin.readline

n = int(read())
arr = set()
cnt = 0

for _ in range(n):
    a = read().rstrip()
    # arr 를 set 으로 받음으로써 중복확인을 안해도 된다. == 시간절약
    # if a in arr:
    #     pass
    if a == "ENTER":
        cnt += len(arr)
        # 왜 틀렸나 했더니 clear 뒤에 () 를 안붙였다. 
        arr.clear()
    else:
        arr.add(a)
cnt += len(arr)
print(cnt)