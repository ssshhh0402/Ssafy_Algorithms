for tc in range(int(input())):
    cad = list(input())
    joong = False
    count_S = [0 for _ in range(13)]
    count_D = [0 for _ in range(13)]
    count_H = [0 for _ in range(13)]
    count_C = [0 for _ in range(13)]
    while cad:
        moo = cad.pop(0)
        n = int(cad.pop(0) + cad.pop(0)) -1
        if moo == 'S':
            if count_S[n] != 0:
                joong = True
                break
            else:
                count_S[n] += 1
        elif moo == 'D':
            if count_D[n] != 0:
                joong = True
                break
            else:
                count_D[n] += 1
        elif moo == 'H':
            if count_H[n] != 0:
                joong = True
                break
            else:
                count_H[n] += 1
        elif moo == 'C':
            if count_C[n] != 0:
                joong = True
                break
            else:
                count_C[n] += 1
    if joong:
        print('#{0} ERROR'.format(tc+1))
    else:
        print('#{0} {1} {2} {3} {4}'.format(tc+1, count_S.count(0), count_D.count(0), count_H.count(0), count_C.count(0)))
