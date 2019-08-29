from collections import deque

for tc in range(int(input())):
    N, M = map(int, input().split())
    base = list(map(int, input().split()))
    hwadeok = deque()
    result = []
    base_2 = []
    idx_m = 0
    idx_v = 0
    for k, v in enumerate(base):
        base_2.append([k, v, 0])
    while base_2:
        if len(hwadeok) != N:
            while len(hwadeok) != N:
                a = base_2.pop(0)
                hwadeok.append(a)
        else:
            hwadeok.rotate(-1)
            for idx in range(N):
                hwadeok[idx][2] += 1
                if hwadeok[idx][2] == N:
                    hwadeok[idx][2] = 0
                    hwadeok[idx][1] = hwadeok[idx][1] // 2
            if hwadeok[0][1] == 0:
                result.append(hwadeok.popleft())
                hwadeok.appendleft(base_2.pop(0))
    while len(hwadeok) != 1:
        hwadeok.rotate(-1)
        for idx in range(len(hwadeok)):
            hwadeok[idx][2] += 1
            if hwadeok[idx][2] == N:
                hwadeok[idx][2] = 0
                hwadeok[idx][1] = hwadeok[idx][1] // 2
            if hwadeok[0][1] == 0:
                result.append(hwadeok.popleft())
                break

    print('#{0} {1}'.format(tc + 1, hwadeok[0][0]))
