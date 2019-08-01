for i in range(int(input())):
    count = int(input())
    numbers = list(map(int, input().split(" ")))
    print("{0} {1}".format(i+1, max(numbers) - min(numbers)))