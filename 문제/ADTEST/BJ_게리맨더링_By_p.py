def DFS(v, group, visit):
#이건 내가 재귀적으로 ㄱ구현하기


N = int(input())
arr = [0] + list(map(int, input().split()))
G = [[]]

for i in range(N):
    tmp = list(amp(int, input().split()))
    tmp.pop(0)
    G.append(tmp)

ans = 1000
for set in range(2, 1 << (N+1)):
    A, B = [], []
    Asum, Bsum = 0, 0
    for i in range(1, N+1):
        if set & (1 << i):
            A.append(i)
            Asum += arr[i]
        else:
            B.append(i)
            Bsum += arr[i]
    if len(A) == 0 or len(B) == 0:
        continue
    if abs(Asum - Bsum) >= ans:
        continue
    visit = [False] * (N+1)
    DFS(A[0], A, visit)
    if len(A) != visit.count(True):
        continue
    DFS(B[0], B, visit)
    if len(B) != visit.count(True):
        continue
    ans = min(ans, abs(Asum - Bsum))
if ans == 1000:
    ans = -1
print(ans)