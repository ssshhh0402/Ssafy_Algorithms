import sys
from collections import deque
# imsi_1 = 무조건 왼쪽
# imsi_2 = 무조건 오른쪽
min_N = 0
N, M = list(map(int, input().split()))
base = deque(x for x in range(1, N+1))
want = list(map(int, input().split()))

# rotate 사용 해야 할 것 같은데...
# 개무식하게 하면 로테이트 길이 비교해서 그 방향으로 계속 돌리기
# 방향 정할 땐 0인지 아닌지로 판단하면 될듯 찾으면 0으로 만들고 그 이후 숫자
# 빼면 want에서도 -1 하기
for i in range(len(want)-1):
    if want[i] < want[i+1]:
        imsi_1 = len([base[x] for x in range(want[i],want[i+1]+1) if base[x] != 0])
        imsi_2 = len([base[x] for x in range(0, want[i]+1) if base[x] != 0]) + len([base[x] for x in range(N-1, base[i+1]-1,-1)])
    else:
        imsi_1 = len([base[x] for x in range(want[i],want[i+1]-1,-1) if base[x] != 0])
        imsi_2 = len([base[x] for x in range(want[i], N) if base[x] != 0]) + len([base[x] for x in range(want[i+1]+1) if base[x] != 0])
    imsi_min = imsi_1 if imsi_1 < imsi_2 else imsi_2
    min_N += imsi_min
    base[want[i]] = 0
    for j in range(want[i]+1, len(base)):
        if base[j] - 1 == 0:
            base[j] = M
        else:
            base[j] -= 1
print(min_N)

