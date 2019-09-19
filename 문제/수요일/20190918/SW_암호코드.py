def getVal(a):
    t = ord(a)
    if t > ord('9'):
        val = (t - ord('A')) + 10
    else:
        val = t - ord('0')
    return val


def find():
    global pwd
    ret = 0
    for i in range(N):
        for j in range(M-1, -1, -1):
            if base[i][j] != '0' and base[i-1][j]=='0':
                pwd = []
                val = getVal(base[i][j])
                stck_v = []
                stck_c = []
                imsi = []
                while val // 2 != 0:
                    a = val % 2
                    imsi.append(a)
                    val //= 2
                imsi.append(val)
                imsi = list(reversed(imsi))
                for q in range(len(imsi)-1, -1, -1):
                    if not stck_v and not stck_c:
                        stck_v.append(imsi[q])
                        stck_c.append(1)
                    else:
                        if imsi[q] == stck_v[-1]:
                            stck_c[-1] += 1
                        else:
                            stck_v.append(imsi[q])
                            stck_c.append(1)
                MIN = min(stck_c)
                pwd.append(P[(stck_c[3]//MIN, stck_c[2]//MIN,stck_c[1]//MIN,stck_c[0]//MIN)])
                a = pwd[0] + pwd[2] + pwd[4] + pwd[6]
                b = pwd[1] + pwd[3] + pwd[5] + pwd[7]
                if ((b * 3 + a) % 10) ==0:
                    ret += (a+b)
    return ret


for tc in range(int(input())):
    P = {(3,2,1,1):0, (2,2,2,1):1, (2,1,2,2):2, (1,4,1,1):3,(1,1,3,2):4,(1,2,3,1):5,(1,1,1,4):6, (1,3,1,2):7
         ,(1,2,1,3):8,(3,1,1,2):9}
    N, M = list(map(int, input().split()))
    base = [input() for _ in range(N)]
    print("#{0} {1}".format(tc+1, find()))
