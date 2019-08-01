for i in range(int(input())):
    a, b = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    answers = []

    for j in range(0, a-b + 1):
        answers.append(sum(numbers[x] for x in range(j, j+b)))
    result = max(answers) - min(answers)
    print("#{0} {1}".format(i + 1,result))
