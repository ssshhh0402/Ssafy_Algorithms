for i in range(int(input())):
    n = int(input())
    answer = []
    numbers = list(map(int, input().split()))

    for q in range(n):
        imsi_m = q
        for j in range(q+1,n):
            if numbers[imsi_m] > numbers[j]:
                imsi_m = j
        numbers[q], numbers[imsi_m] = numbers[imsi_m], numbers[q]

    for p in range(n//2):
        answer.append(numbers[-p-1])
        answer.append(numbers[p])
    print("#{0} ".format(i+1), end="")
    for item in range(10):
        print(answer[item], end=" ")
    print("")