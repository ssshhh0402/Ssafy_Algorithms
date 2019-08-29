import sys
from collections import deque

for tc in range(int(sys.stdin.readline())):
    num, target = list(map(int, sys.stdin.readline().split()))
    count = 0
    joong = deque(map(int, sys.stdin.readline().split()))
    for i in range(num):
        if joong[i] == max(joong):
            count += 1
            joong.popleft()
        else:
            joong.rotate(-1)
    print(joong)
    # for i in range(num):
    #     if joong[i] == max(joong):
    #         joong.pop(0)
