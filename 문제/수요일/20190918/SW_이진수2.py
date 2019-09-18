for tc in range(int(input())):
    N = float(input())
    num = 1 / 2
    result = []
    of = 1
    while N:
        if len(result) >= 13:
            of = 0
            break
        else:
            if N >= num:
                result.append(str(1))
                N -= num
            else:
                result.append(str(0))
            num /= 2

    if not of:
        print("#{0} overflow".format(tc+1))
    else:
        print("#{0} {1}".format(tc+1, ''.join(result)))