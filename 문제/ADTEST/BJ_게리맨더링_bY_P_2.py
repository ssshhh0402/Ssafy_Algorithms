#k:결정할 구역 번호, A,B = 그룹 리스트, sumA = A합, sumB = B합
def backtrack(k, A, B, sumA):
    if k == N+1:
        global ans
        diff = abs(sumA * 2 - total)
        if len(B) == 0 or diff >= ans:
            return
        visit = [False] * (N + 1)
        if (DFS(A[0], A, visit) != len(A)):
            return
        visit = [False] *(N+1)
        if (DFS(B[0],B,visit) != len(B)):
            return
        ans = diff
    else:
        A.append(k)
        backtrack(k+1, A,B, sumA + arr[k])
        A.pop()
        B.append(k)
        backtrack(k+1, A,B, sumA)
        B.pop()

A, B = [], []
total = sum(arr)
A.append(1)
backtrack(2, A, B, arr[1])
