#############################깊이우선탐색#######################################
def backtrack(k, sum):              #k = 트리의 깊이(depth), 문항번호, s : 지금까지 정수 합
        global count
        if visit[k][sum]:
            return
        visit[k][sum] = 1
        if k == N:
            count += 1
            return
        else:
            backtrack(k + 1, sum)
            backtrack(k+1, sum + scores[k])


for tc in range(1, int(input())+1):
    N = int(input())
    scores = list(map(int,input().split()))
    visit = [[0] * (N * 100 + 1) for _ in range(N + 1)]
    count = 0
    backtrack(0, 0)
    print("#{0} {1}".format(tc, count))
###################################################################################
import collections
scores = [1] * 10
N = len(scores)
visit = [[0] * (N * 100 + 1) for _ in range(N + 1)]
cnt = 0
visit[0] = 1
for s in scores:
    for i in range(10000, -1, -1):
        if visit[i]:
            visit[i+s] = 1