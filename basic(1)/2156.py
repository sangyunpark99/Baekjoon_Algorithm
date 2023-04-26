import sys

n = int(input())

dp = [0] * 10000
array = [0] * 10000
for i in range(n):
    array[i] = (int(sys.stdin.readline().rstrip()))

dp[0] = array[0]
dp[1] = array[0] + array[1]
dp[2] = max(array[0] + array[1], array[1] + array[2], array[0] + array[2])

for i in range(3, n):
    dp[i] = max(array[i] + dp[i - 2], array[i] + array[i - 1] + dp[i - 3], dp[i - 1])

print(max(dp))
