import sys
import math

n = int(sys.stdin.readline().rstrip())

dp = [m for m in range(n+1)]

for i in range(1, n + 1): # n
    for j in range(1, int(math.sqrt(i))+1):
        if i < j * j:
            break
        if dp[i] > dp[i-j*j]+1:
            dp[i] = dp[i-j*j]+1

print(dp[n])  # 결과 출력
