for i in range(10):
    base = []
    max_num = 0
    number = int(input())
    for j in range(100):
        imsi= list(map(int, input().split()))
        base.append(imsi)
    num = len(base)
    # 정리 끝
    for q in range(100):
        imsi_max = sum(base[x][q] for x in range(num))
        if imsi_max > max_num:
            max_num = imsi_max
        imsi_max2 = sum(base[q][x] for x in range(num))
        if imsi_max2 > max_num:
            max_num = imsi_max2
    # x합 y합
    im_max = sum(base[x][x] for x in range(num))
    im_max2 = sum(base[num-x-1][x] for x in range(num))
    #대각선 아이들
    print('#{0} {1}'.format(number, max([max_num, im_max, im_max2])))
