# def find(a):        #a = 횟수
#     global num_max
#     string = int(''.join(base))
#     if a == N:
#         num_max = max(num_max,string)
#         return
#     if visited[string]:
#         return
#     visited[string] = 1
#     for i in range(L):
#         for j in range(L):
#             if i != j:
#                 base[i], base[j] = base[j], base[i]
#                 find(a+1)
#                 base[i], base[j] = base[j], base[i]
#
# for tc in range(1, int(input())+1):
#     base, N = map(int,input().split())
#     base = list(str(base))
#     L = len(base)
#     num_max = 0
#     visited = [0 for _ in range(999999+1)]
#     for i in range(L):
#         for j in range(L):
#             if i != j:
#                 base[i], base[j] = base[j], base[i]
#
#    find(1)
#                 base[i], base[j] = base[j], base[i]
#
#     print("#{0} {1}".format(tc,num_max))
def find(a):        #a = 횟수
    global num_max
    string = int(''.join(base))
    if a == N:
        num_max = max(num_max,string)
        return
    if visited[a][string]:
        return
    visited[a][string] = 1
    for i in range(L):
        for j in range(i+1, L):
            base[i], base[j] = base[j], base[i]
            find(a+1)
            base[i], base[j] = base[j], base[i]


for tc in range(1, int(input())+1):
    base, N = map(int,input().split())
    base = list(str(base))
    L = len(base)
    num_max = 0
    visited = [[0 for _ in range(N+1)] for _ in range(999999+1)]
    for i in range(L):
        for j in range(i+1, L):
            base[i], base[j] = base[j], base[i]
            find(1)
            base[i], base[j] = base[j], base[i]

    print("#{0} {1}".format(tc,num_max))