
for i in range(10):
    result = 0
    max_n = int(input())

    numbers = list(map(int, input().split()))
    # for j in range(2, len(numbers)-2):
    #     if numbers[j] > max([numbers[j-1], numbers[j-2], numbers[j+1], numbers[j+2]]):
    #         result += numbers[j] - max([numbers[j-1], numbers[j-2], numbers[j+1], numbers[j+2]])
    for j in range(2, len(numbers)-2):
        lar = 0
        for p in range(j-2, j+3):
            if p == j:
                continue
            elif numbers[p] > lar:
                lar = numbers[p]
        if numbers[j] > lar:
            result += numbers[j] - lar
    print("#{0} {1}".format(i+1, result))
