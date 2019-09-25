def game(arr,b):
    ans = 0
    if b < 3:
        return 0
    elif 3 in arr:
        return 1
    else:
        for i in range(1,len(arr)-1):
            if arr[i-1] >= 1 and arr[i] >= 1 and arr[i+1] >= 1:
                return 1
    return 0






for tc in range(1, int(input())+1):
    base = list(map(int, input().split(' ')))
    p_a = [0 for _ in range(10)]
    p_b = [0 for _ in range(10)]
    count = 0
    s_b = False
    for i in range(0,12,+2):
        count += 1
        p_a[base[i]] += 1
        if game(p_a,count) == 1:
            s_b = True
            print("#{0} {1}".format(tc, 1))
            break
        p_b[base[i+1]] += 1
        if game(p_b, count) == 1:
            s_b = True
            print("#{0} {1}".format(tc, 2))
            break
    if not s_b:
        print("#{0} 0".format(tc))