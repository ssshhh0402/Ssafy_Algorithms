import sys
from collections import deque

def find(a, b):
    global result
    stck = deque()
    stck.append((a,b))
    while stck:
        n = stck.popleft()
        if n[0] == N:
            result.append(n[1])
        else:
            for i in range(n[0], len(list_T)):
                if i + list_T[i] <= N:
                    stck.append((i + list_T[i], n[1] + list_P[i]))
                else:
                    result.append(n[1])



list_T = []
list_P = []
result = []
N = int(sys.stdin.readline())
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    list_T.append(a)
    list_P.append(b)
for i in range(len(list_T)):
    if i + list_T[i] <= N:
        find(i + list_T[i], list_P[i])
if len(result) == 0:
    print(0)
else:
    print(max(result))