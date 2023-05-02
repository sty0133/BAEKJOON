import sys
from collections import deque
read = sys.stdin.readline

a , b = map(int,read().split())

def find(x):
    queue = deque()
    queue.append([x,1])

    while queue:
        x, count = queue.popleft()
        if x == b:
            return count
        
        for next_x in [2*x, 10*x+1]:
            if 0 <= next_x <= b:
                queue.append([next_x, count+1])

    return -1

print(find(a))