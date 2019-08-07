for i in range(int(input())):
    nums = int(input())
    numbers = list(map(int, input()))
    count = [0] * 10
    max_n = 0
    max_i = 0
    for j in numbers:
        count[j] += 1
    for n, idx in enumerate(count):
        if idx >= max_i:
            max_n = n
            max_i = idx

    print("#{0} {1} {2}".format(i+1, max_n, max_i))