for tc in range(int(input())):
    li_A = []
    li_B = []
    li_C = []
    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        li_A.append(a)
        li_B.append(b)
    P = int(input())
    for _ in range(P):
        li_C.append(int(input()))
    cnt = [0 for _ in range(P)]
    for idx in range(N):
        for j in range(li_A[idx], li_B[idx]+1,1):
            cnt[j-1] += 1

    print("#{0} {1}".format(tc+1, ' '.join(list(map(str, cnt)))))