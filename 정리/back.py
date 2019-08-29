# arr = 'ABC',
# N = len(arr)
# bits = [0] * N
#
#
# def subset(k, n):
#     global N, K, ans
#     if k == n:
#         for j in range(N):
#             cnt = S = 0
#             for i in range(n):
#                 if bits[i]:
#                     cnt, S = cnt + 1, S + (i + 1)
#             if cnt == N and S == K:
#                 ans += 1
#     else:
#         bits[k] = 1; subset(k + 1, n)
#         bits[k] = 0; subset(k + 1, n)
#
#
# for tc in range(int(input())):
#     N, K = map(int, input().split())
#     ans = 0
#     subset(0, 12)
#     print('#{0} {1}'.format(tc+1, ans))
#
# arr = 'ABC'
# N = len(arr)
# order = [0] * N
#
# def perm(k, n, used):
#     if k == n:          #하나의 순열 생성
#         for i in range(n):
#             print(arr[order[i]], end=" ")
#         return
#     for i in range(n):
#         if used & (1 << i):
#             continue
#         order[k] = i
#         perm(k+1, n, used | (1 << i))
#
# perm(0, N, 0) # 0: 선택한 수, N: 전체 원소수, 0: 선택한 원소수











# def subset(k, n, cnt, cur_sum):                                     #cnt = 현재 선택한 원소수, cur_sum : 원소들 합
#     global ans, N, K
#     if cnt > N or cur_sum > K: return
#     if k == n:
#         if cnt == N and cur_sum == K: ans += 1
#         return
#
#     subset(k+1, n, cnt + 1, cur_sum +k)
#     subset(k+1, n, cnt, cur_sum)
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
#     ans = 0
#     subset(1, 13, 0, 0)
#     print('#{0} {1}'.format(tc, ans))

arr = [6, 4, 2, 5, 1, 0, 11, 2, 2, 8, 7]

def getMin(low, high):
    if low == high:
        print(arr[low])
    else:
        mid = (low+high) >> 1
        return min(getMin(low, mid), getMin(mid+1, high))

print(getMin(0, len(arr)-1))