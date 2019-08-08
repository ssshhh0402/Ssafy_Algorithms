for i in range(int(input())):
    gs = int(input())
    numbers = list(map(int, input().split(" ")))
    nasa_am = []
    nasa_soo = []
    result = []
    for k, v in enumerate(numbers):
        if k % 2 == 0:
            nasa_soo.append(v)
        else:
            nasa_am.append(v)

    while len(result) != gs*2:
        if len(result) == 0:
            for a, b in enumerate(nasa_soo):
                if b not in nasa_am:
                    result.append(nasa_soo[a])
                    result.append(nasa_am[a])
        else:
            for c, d in enumerate(nasa_soo):
                if d == result[-1]:
                    result.append(nasa_soo[c])
                    result.append(nasa_am[c])

    print("#{0}".format(i + 1), end=" ")
    for items in result:
        print(items, end=" ")
    print("")

#받고
#홀수 위치, 짝수 위치 파악해서
#홀수 위치가 짝수 위치에 없으면 맨 앞에
#나머지는 추가