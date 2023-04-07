ans = [0]*1001

n = int(input())

ans[1] = 1
ans[2] = 3

for i in range(3, 1001):
    ans[i] = ans[i-1] + 2*ans[i-2]

print(ans[n] % 10007)