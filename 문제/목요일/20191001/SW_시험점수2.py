def find(a,b):
    global score
    score[a] = 1
    for i in range(b+1,L):
        find(a+base[i],i)


for tc in range(1, int(input())+1):
    N = int(input())
    base = list(map(int, input().split()))
    score = [0]*((100*N)+1)
    score[0] = 1
    L = len(base)
    for i in range(L):
        find(base[i],i)

    print("#{0} {1}".format(tc, sum(score)))