import random
# base = [[9,20, 2, 18, 11], [19, 1, 25, 3, 21], [8, 24, 10, 17, 7], [15, 4, 16, 5, 6], [12, 13, 22, 23, 14]]
# answer = []
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
# for i in range(5):
#     imsi = []
#     for j in range(5):
#         imsi.append(random.randint(0,100))
#     base.append(imsi)
#
# for a in range(5):
#     for b in range(5):
#         for x in range(4):
#             for y in range(4):
#                 # 다 조건문으로 떄려 받아야하나? 너무 더러운데
#                 print(a, b, x, y)
#                 if a + dx[x] >= 0 & b + dy[y] >= 0:
#                     answer.append(abs(base[a][b] - base[a+dx[x]][b+dy[y]]))
#     ##3 이거 중간에 0.4 갔을떄 수정해야 한다. 조건문에 a + dx[x] 값이 맥스 값 넘지 않도록 해야할듯
# print(sum(answer))
#                 # if base[a + dx[x]][b + dy[y]]:
#                 #     answer.append(abs(base[a][b] - base[a-dx[x]][b-dy[y]]))

# print(1 << 8)
# a = 0b1010
# print(a << 1)
# print(1 << 8)
# print(type(1 << 8))
# n = 5
# if n & 1 :
#     print('홀수')
# else:
#     print('짝수')

# arr = 'algorithm'
# arr = list(arr)
# for i in range(len(arr) // 2):
#     arr[i],arr[len(arr)-i-1] = arr[len(arr)-i-1] , arr[i]
#
# print(''.join(arr))
# for i in range(int(input())):
#     number = list(input())
#     answer = [0] * len(number)
#     for j in range(len(number)):
#        answer[j] = number[len(number) -1 -j]
#
#     if number == answer:
#         print('{0} 1'.format(i+1))
#     else:
#         print('{0} 0'.format(i+1))
p = 'CATTCCCTGCGCCGC'
t = 'ATTTGTGCATGTTTGAGCTTTTACGTACGAGAAACTGAACTGTACCTACGACATTCCCTGCGCCGCCACCCCCTTTTTGAA'
n,m = len(p), len(t)
for i in range(m-n):
    for j in range(m):
        if t[i+j] != p[j]:
            break
    else:
        print(True)
