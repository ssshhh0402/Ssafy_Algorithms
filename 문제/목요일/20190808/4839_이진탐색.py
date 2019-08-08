def binary(a,b):
    left = 1
    count = 0
    mid = (left+a)//2
    while True:
        count += 1
        if mid == b:
            return count
        elif mid > b:
            a = mid
            mid = (left+a)//2
        elif mid < b:
            left = mid
            mid = (left+a) // 2


for i in range(int(input())):
    book_n, t_1, t_2 = list(map(int, input().split(" ")))

    s_1 = binary(book_n, t_1)
    s_2 = binary(book_n, t_2)
    if s_1 < s_2:
        print("#{0} {1}".format(i+1, 'A'))
    elif s_1 > s_2:
        print("#{0} {1}".format(i+1, 'B'))

    else:
        print("#{0} 0".format(i+1))