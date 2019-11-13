# def find(a,b):
#     global result, count
#     for k in range(2 * N, 0, -1):
#         cnt = 0
#         for home in homes:
#             dist = abs(home[0]-a) + abs(home[1] - b)
#             if dist < k:
#                 cnt += 1
#         byong = k ** 2 + (k-1) ** 2
#         income = M * cnt
#         ed = income - byong
#         if ed >= 0:
#             count = max(count, cnt)
#             return
#######========================거리로 계산==========================================
def find(a,b):
    global result, count
    for k in range(2 * N, 0, -1):
        cnt = 0


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    base = [list(map(int,input().split())) for _ in range(N)]
    homes = []
    count = -0xfffffff
    for i in range(N):
        for j in range(N):
            if base[i][j] == 1:
                homes.append((i,j))
    for i in range(N):
        for j in range(N):
            find(i,j)
    print("#{0} {1}".format(tc, count))