import sys
def find(a, b):
    global result
    if a == N:
        result.append(b)
    else:
        for idx in range(a, len(list_T)):
            if a + list_T[idx] <= N:
                find(list_T[idx], b + list_P[idx])


list_T = []
list_P = []
result = []
N = int(sys.stdin.readline())
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    list_T.append(a)
    list_P.append(b)
for i in range(len(list_T)):
    find(i, 0)
print(result)