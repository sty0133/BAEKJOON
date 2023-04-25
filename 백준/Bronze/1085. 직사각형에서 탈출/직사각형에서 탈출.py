import sys
read = sys.stdin.readline

x , y , w , h = map(int, read().rstrip().split())

## 1트
# if w - x < h - y:
#     if w - x > x:
#         if x < y:
#             print(x)
#     else:
#         print(w - x)
# elif w - x > h - y:
#     if h - y > y:
#         if x > y:
#             print(y)
#     else:
#         print(h - y)

## 2트
# if w - x < x or h - y < y:
#     if w - x <= h - y:
#         print(w - x)
#     elif h - y <= w - x:
#         print(h - y)
# else:
#     if y < x:
#         print(y)
#     else:
#         print(x)

## 3트
print(min(x, y, w-x, h-y))