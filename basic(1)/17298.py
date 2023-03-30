from collections import deque

n = int(input())
seq = list(map(int, input().split()))

ans = [-1] * n
stack = deque()

# index, value 둘 다 알아아 한다.
for i in range(n):
    while stack and (stack[-1][0] < seq[i]):
        value, idx = stack.pop()
        ans[idx] = seq[i]
    stack.append((seq[i], i))

print(*ans)