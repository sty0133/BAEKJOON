import sys
read = sys.stdin.readline

a1 , a0 = map(int, read().split())
c = int(read())
n0 = int(read())

# O(g(n)) , O(n) 즉 g(n) = n , f(n) ≤ c × n
# 0 ≤ |ai| ≤ 100  == ai 는 양수 또는 음수도 가능
# https://img1.daumcdn.net/thumb/R1280x0/?fname=http://t1.daumcdn.net/brunch/service/user/85kA/image/kjtsKAogvgamFTrn49EQZXbYblY.png
# 시간 복잡도에는 f(n) 이 음수일 경우의 수가 없는듯 하다.
# 그러니 f(x)가 음수일때를 예외처리를 할려면 c가 a1보다 크거나 같아야 한다.
if a1 * n0 + a0 <= c * n0 and c >= a1:
    print(1)
else:
    print(0)