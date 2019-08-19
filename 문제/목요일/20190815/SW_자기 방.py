# for i in range(int(input())):
#     base = []
#     result = {}
#     num = int(input())
#     # 이거 끝까지 다 확인해 봐야하나?
#     for j in range(num):
#         base.append(list(map(int, input().split())))
#     for p in range(num):
#         for ans in range(base[p][0], base[p][1]+1):
#                 if ans not in result.keys():
#                     result[ans] = 1
#                 else:
#                     result[ans] += 1
#
#     print("#{0} {1}".format(i+1, max(result.values())))
# for i in range(int(input())):
#     base = []
#     count = 1
#     result={}
#     # 이거 끝까지 다 확인해 봐야하나?
#     for j in range(int(input())):
#         base.append(list(map(int, input().split())))
#     n = len(base)
#
#     for p in range(n-1):
#         for q in range(p+1, n):
#             if base[q][0] in range(base[p][0], base[p][1]) or base[q][1] in range(base[p][0], base[p][1]):
#                 count += 1
#                 break
#
#                                                                                                                 #정렬해서 넣어보자
#     print("#{0} {1}".format(i+1, count))
# for i in range(int(input())):
#     base = {}
#     count = 1
#     for j in range(int(input())):
#         (a, b) = list(map(int, input().split()))
#         base[a] = b
#     n = len(base)
#     k_order = list(sorted(base.keys()))
#     for p in range(n-1):
#         for q in range(p+1, n):
#             if k_order[q] in range(k_order[p], base[k_order[p]]) or base[k_order[q]] in range(k_order[p], base[k_order[p]]):
#                 count += 1
#                 break
#     print("#{0} {1}".format(i+1, count))


for i in range(int(input())):
    base = []
    result = {}
    num = int(input())
    # 이거 끝까지 다 확인해 봐야하나?
    for j in range(num):
        base.append(list(map(int, input().split())))
    for p in range(num):
        if base[p][0] < base[p][1]:
            for ans in range(2 * ((base[p][0]) // 2), 2*((base[p][1] + 1) // 2) + 1):
                if ans not in result.keys():
                    result[2 * (ans//2)] = 1
                else:
                    result[2 * (ans//2)] += 1
        else:
            for ans in range(2 * (base[p][1] // 2), 2 * (base[p][0] // 2) - 1, -1):
                if ans not in result.keys():
                    result[2 * (ans //2)] = 1
                else:
                    result[2 * (ans // 2)] += 1

            print('#{0} {1}'.format(i + 1, max(result.values())))