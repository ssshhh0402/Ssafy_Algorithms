def find(arr_1, arr_2):  # arr_1 = 집, arr_2=  치킨집 조합 # 집을 기준으로 모든 치킨집에 대한 거리 계싼
    result = []
    while arr_2:
        imsi = 0
        pick = arr_2.pop(0)
        for house in arr_1:
            imsi_2 = []
            for idx in pick:
                imsi_2.append(abs(idx[0] - house[0]) + abs(idx[1]- house[1]))
            imsi += min(imsi_2)
        result.append(imsi)
    print(min(result))


N, M = map(int, input().split())
base = [list(map(int, input().split())) for _ in range(N)]
chk = []
hs = []
jh = []
for x in range(N):
    for y in range(N):
        if base[x][y] == 1:
            hs.append((x, y))
        elif base[x][y] == 2:
            chk.append((x, y))
n_chk = len(chk)
for i in range(1 << n_chk):
    imsi = []
    for j in range(n_chk+1):
        if i & (1 << j):
            imsi.append(chk[j])
    if 0 < len(imsi) <= M:
        jh.append(imsi)
find(hs, jh)


