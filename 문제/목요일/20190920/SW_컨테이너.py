for tc in range(int(input())):
    N,M = map(int, input().split())
    result = 0
    hwa = sorted(list(map(int,input().split())))
    truck = sorted(list(map(int, input().split())))
    carried = [0 for _ in range(N)]
    t_start = [0 for _ in range(M)]
    for i in range(len(truck)-1, -1, -1):
        for j in range(len(hwa)-1, -1, -1):
            if truck[i] >= hwa[j] and not carried[j] and not t_start[i]:
                carried[j] = 1
                t_start[i] = 1
                result += hwa[j]
    print("#{0} {1}".format(tc+1, result))