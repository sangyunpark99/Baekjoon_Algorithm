a = int(input())

nums = list(map(int, input().split()))

dp = [0] * a

for i in range(a):
    for j in range(i): # 다음것 확인하기
        if nums[i] > nums[j] and dp[i] < dp[j]: # 수열인 경우
            dp[i] = dp[j]
    dp[i] += 1 #자기 자신 +1

print(max(dp))