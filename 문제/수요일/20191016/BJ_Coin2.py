
n,k = map(int,input().split())
coins = [0 for _ in range(n)]
for idx in range(n):
    coins[idx] = int(input())
coins.sort()
dp = [0 for _ in range(k+1)]
dp[0] = 1
for i in coins:
    for j in range(1, k+1):
        if j - i >= 0:
            dp[j] += dp[j-i]
print(dp[k])