for i in range(int(input())):
    e, jong, choong = list(map(int, (input().split(' '))))
    a = [False] * jong
    b = list(map(int, (input().split(' '))))
    for j in b:
        a[j] = True
    count = 0
    energy = e
    for p in range(1, len(a)):
        energy -= 1
        if a[p]:
            if p + energy < len(a):
                if energy == 0:
                    count += 1
                    energy = e
                elif True not in (a[x] for x in range(p + 1, p + energy+1)):
                    count += 1
                    energy = e
            # elif energy < len(a) - p:
            #         count += 1
            #         energy = e

        ## 이동 끝
        if energy == 0:
            print('#{0} {1}'.format(i + 1, 0))
            break
        elif p == len(a) - 1:
            print('#{0} {1}'.format(i + 1, count))


    #끝 판단

    # 이동 계산 끝
