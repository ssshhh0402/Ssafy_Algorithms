for i in range(10):
    base = []
    max_num = 0
    number = int(input())
    im_max = im_max2 = 0
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
        im_max += base[q][q]
        im_max2 += base[q][99-q]
    # x합 y합
    # im_max = sum(base[x][x] for x in range(num))
    # im_max2 = sum(base[num-x-1][x] for x in range(num))
    #대각선 아이들
    print('#{0} {1}'.format(number, max([max_num, im_max, im_max2])))




#---------------------------강사님 코드------------------------------
# import sys
# sys.stdin = open('input.txt', 'r')
#
# for tc in range(1, 11):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(100)]
#
#     Max = 0 #최대값 을 저장할 아이
#
#     for i in range(100):
#         S = 0 #합을 더하기 위한 아이
#         for j in range(100):
#             S += arr[i][j]
#             Max = max(Max, S)
#
#     for j in range(100):
#         S = 0
#         for j in range(100):
#             S += arr[i][j]
#         Max = max(Max, S)
#
#
#     S = 0
#     for p in range(100):
#         S += arr[p][p]
#     Max = max(Max, S)
#
#     for q in range(100):
#         S += arr[q][99-q]
#     Max = max(Max, S)
#
#     print(Max)