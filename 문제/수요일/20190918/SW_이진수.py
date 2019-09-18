for tc in range(int(input())):
    result = []
    a, base = list(input().split())
    for i in range(int(a)):
        imsi_base = []
        if base[i].isdigit():
            imsi = int(base[i])
            while imsi // 2:
                imsi_base.append(imsi % 2)
                imsi //= 2
            imsi_base.append(imsi)
        else:
            imsi = 10 + (ord(base[i]) - ord('A'))
            while imsi // 2:
                imsi_base.append(imsi % 2)
                imsi //= 2
            imsi_base.append(imsi)
        if len(imsi_base) != 4:
            while len(imsi_base) != 4:
                imsi_base.append(0)
        for i in range(len(imsi_base)-1, -1, -1):
            result.append(str(imsi_base[i]))
    print("#{0} {1}".format(tc+1, ''.join(result)))