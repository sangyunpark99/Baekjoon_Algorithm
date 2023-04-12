n = int(input())

dp = [[0, 0]for _ in range(91)]

dp[1][0] = 0
dp[1][1] = 1
dp[2][0] = 1
dp[2][1] = 0
dp[3][1] = 1
dp[3][0] = 1

for i in range(4, 91):
    dp[i][0] += dp[i-1][0] # 0으로 끝난경우 0이 옴
    dp[i][1] += dp[i-1][0] # 0으로 끝난경우 1이 옴
    dp[i][0] += dp[i-1][1] # 1로 끝난경우 0만 올 수 있음

print(sum(dp[n]))

