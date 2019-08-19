# for i in range(10):
#     base = []
#     num = int(input())
#     count = 0
#     for j in range(8):
#         base.append(list(input()))
#     for p in range(8 - num):
#         for q in range(8 - num):
#             word_1 = ''.join(base[p][x] for x in range(q, q + num))
#             word_2 = ''.join(base[p][x] for x in range())

for i in range(10):
    N = 8
    M = int(input())
    #N = base 길이, M = 회문 길이
    base = []
    for j in range(N):
        base.append(list(input()))
    count = 0             #차라리 가로축 쫙 확인하고 세로 축 쫙 확인하고 그런식으로 ㄱ
    for p in range(N):
        for q in range(N-M+1):
            word_1 = ''.join(base[p][y] for y in range(q, q+M))
            word_2 = ''.join(base[p][y_2] for y_2 in range(q+M-1, q-1, -1))
            if word_1 == word_2:
                count += 1
            word_1 = ''.join(base[x][p] for x in range(q, q+M))
            word_2 = ''.join(base[x_2][p] for x_2 in range(q+M-1, q-1, -1))
            if word_1 == word_2:
                count += 1

    print("#{0} {1}".format(i+1, count))
