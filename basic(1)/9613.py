from itertools import combinations
from math import gcd
import sys

n = int(input())

for _ in range(n):
    ans = 0
    m = list(map(int, sys.stdin.readline().split()))
    m.pop(0)
    for a, b in combinations(m, 2):
        ans += gcd(a, b)
    print(ans)