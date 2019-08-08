A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for idx in range(int(input())):
    tong = []
    count = 0
    ran, sum_n = list(map(int, input().split(" ")))
    for i in range(1 << len(A)):
        imsi = []
        for j in range(len(A)):
            if i & (1 << j):
                imsi.append(A[j])
        tong.append(imsi)
    for item in tong:
        if len(item) == ran and sum(item) == sum_n:
            count += 1

    print("#{0} {1}".format(idx+1, count))

