
for i in range(int(input())):  #Testcase
    col1 = [[False] * 10 for _ in range(10)]
    col2 = [[False] * 10 for _ in range(10)]
    count = 0
    for j in range(int(input())): #색칠 영역 갯수
        imsi = list(map(int, input().split(" ")))   #영역 입력
        if imsi[-1] == 1:
            for x in range(imsi[0], imsi[2]+1):
                for y in range(imsi[1], imsi[3]+1):
                    col1[x][y] = True
        elif imsi[-1] == 2:
            for x in range (imsi[0], imsi[2]+1):
                for y in range(imsi[1], imsi[3]+1):
                    col2[x][y] = True

    for x in range(10):
        for y in range(10):
            if col1[x][y] and col2[x][y]:
                count += 1

    print("#{0} {1}".format(i+1, count))
#이거 공통부분 구하면 될거같은데;
