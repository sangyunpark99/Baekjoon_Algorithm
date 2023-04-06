ans = [0]*1001

ans[1] = 1
ans[2] = 2

n = int(input())

for i in range(3, n+1):
    ans[i] = ans[i-1] + ans[i-2]

print(ans[n]%10007)