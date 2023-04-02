from math import gcd

n, s = map(int, (input().split()))
a = list(map(int, input().split()))

distance = []

for i in range(n):
    if a[i] <= s:
        distance.append(s-a[i])
    else:
        distance.append(a[i]-s)

print(gcd(*distance))
