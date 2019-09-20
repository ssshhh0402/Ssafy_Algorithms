



for tc in range(1, int(input())+1):
    base_a = []
    base_b = []
    base = list(map(int, input().split()))
    for i in range(0,len(base),+2):
        base_a.append(base[i])
        base_b.append(base[i+1])
        if check(base_a):
            print("#{0} 1".format(tc))
        elif check(base_b):
            print("#{0} 2".format(tc))
        else:
            print("#{0} 0")

