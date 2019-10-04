# # num = list(input())
# # N = len(num)
# # for i in range(N-1):
# #     for j in range(i+1, N):
# #         num[i], num[j] = num[j], num[i]
# #         for i in range(N-1):
# #             for j in range(i+1, N):
# #                 num[i], num[j] = num[j], num[i]
# #                 print(num)
# #                 num[i], num[j] = num[i],num[j]
#
# num = list(input())
# N = len(num)
# cnt = int(input())
# max_num = 0
# visited = [[0] * 1000000 for _ in range(N+1)]
#
#
# def backtrack(k):
#     global max_num
#     val = int(''.join(map(str, num)))
#     if k == cnt:
#         max_num = max(max_num, int(''.join(map(str, num))))
#     if visited[val][k]:
#         return
#     visited[val][k] = 1
#     for i in range(N - 1):
#         for j in range(i+1, N):
#             num[i], num[j] = num[j], num[i]
#             backtrack(k+1)
#             num[i], num[j] = num[j], num[i]
#
#
# backtrack(0)
# print(max_num)
from collections import deque
d = [1, 10, 100, 1000, 10000, 100000]


def swap(val, i, j):
    a = (val // d[i]) % 10
    b = (val // d[j]) % 10
    return val - a * d[i] + a * d[j] - b * d[j] + b * d[i]


num = 32888
N = len(num)
cnt = 10
visit = [[0]*100000 for _ in range(11)]
MAX = 0
Q = deque()
Q.append((num, 0))
while Q:
    val, k = Q.popleft()
    if k == cnt:
        MAX = max(MAX, val)
    else:
        for i in range(N - 1):
            for j in range(i+1, N):
                t = swap(val, i, j)
                if visit[k][t]:
                    continue
                else:
                    Q.append(t,k+1)