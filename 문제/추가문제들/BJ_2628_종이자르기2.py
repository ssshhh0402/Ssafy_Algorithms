# 저 애들 정렬하고
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

order_h.sort()
order_w.sort()
