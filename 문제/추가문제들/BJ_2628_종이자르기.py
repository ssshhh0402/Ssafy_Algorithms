def ct(a, b):
    global chk
    if chk[a][b]:
        return 0
    elif a+1 in order_w:
        chk[a][b] = 1
        if b+1 in order_h:
            return 1
        else:
            return 1 + ct(a, b+1)
    elif b+1 in order_h:
        chk[a][b] = 1
        if a + 1 in order_w:
            return 1
        else:
            return 1 + ct(a+1, b)
    else:
        chk[a][b] = 1
        return 1 + ct(a+1, b) + ct(a, b+1)


N, M = list(map(int, input().split()))
chk = [[0 for _ in range(N)] for _ in range(N)]
count = 0
order_h = []
order_w = []
result = []
for _ in range(int(input())):
    o_1, o_2 = map(int, input().split())
    if o_1 == 0:
        order_w.append(o_2)
    else:
        order_h.append(o_2)

for i in range(M):
    for j in range(N):
        if not chk[i][j]:
            result.append(ct(i, j))
print(result)

