from collections import deque, Counter
import sys

n = int(input())

A = list(map(int, sys.stdin.readline().rstrip().split()))
F = Counter(A)
ans = [-1 for _ in range(len(A))]
stk = deque()

for i in range(n):
    while stk and F[A[stk[-1]]] < F[A[i]]:
        ans[stk.pop()] = A[i]
    stk.append(i)

print(*ans)