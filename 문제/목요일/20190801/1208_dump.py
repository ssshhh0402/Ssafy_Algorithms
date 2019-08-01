for i in range(10):
    width = 100
    count = int(input())
    first = 0
    boxes = list(map(int, input().split()))
    check = {}
    for j in range(len(boxes)):
        check[j] = boxes[j]
    while max(check.values()) != min(check.values()):
        ma = False
        mi = False
        max_n = max(check.values())
        min_n = min(check.values())
        for idx, num in check.items():
            if num == max_n and not ma:
                check[idx] = num - 1
                ma = True
            elif num == min_n and not mi:
                check[idx] = num + 1
                mi = True
        first += 1
        if count == first:
            break
    print('#{0} {1}'.format(i+1, max(check.values()) - min(check.values())))

