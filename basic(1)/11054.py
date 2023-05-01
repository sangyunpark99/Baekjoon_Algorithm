n = int(input())

a = list(map(int, input().split()))

dp1 = [0] * n
dp2 = [0] * n

for i in range(n): # 왼쪽기준 정렬
    for j in range(i):
        if a[i] > a[j]:
            dp1[i] = max(dp1[i], dp1[j])
    dp1[i] += 1 # 자기자신 더해주기

for i in range(n-1,-1,-1): # 오른쪽 기준 정렬
    for j in range(i,n):
        if a[i] > a[j]:
            dp2[i] = max(dp2[i], dp2[j])
    dp2[i] += 1 # 자기 자신 더해주기

for i in range(n):
    dp1[i] = dp1[i] + dp2[i]-1 # 자기자신 중복 제거

print(max(dp1))

