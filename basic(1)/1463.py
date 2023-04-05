n = int(input())

dp = [0] * (n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1 # +1 : 빼준 것을 더해줌

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1) # 나눠준 것을 1 더해줌
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1) # 나눠준 것을 1 더해줌

print(dp[n])