def change(a,b,c):
    global base
    imsi = []
    idx = 9 + (ord(c) - ord('A'))
    while idx // 2 != 0:
        imsi.append(idx % 2)
        idx //= 2
    imsi.append(idx)
    imsi = list(reversed(imsi))
    for i in range(len(imsi)):
        base[a].insert(b, str(imsi[i]))
        b +=1




for tc in range(int(input())):
    N, M = list(map(int, input().split()))
    base = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(M-1, -1, -1):
            if base[i][j] != 0:
                if not base[i][j].isdigit():
                    a = base[i][j]
                    base[i].pop(j)
                    change(i,j,a)
    print(base)