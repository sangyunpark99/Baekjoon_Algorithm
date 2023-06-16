from collections import deque

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

ans = [[0] * n for i in range(n)]


def bfs(m):
    queue = deque()
    queue.append(m)
    check = [0 for _ in range(n)]

    while queue:
        num = queue.popleft()
        for i in range(n):
            if matrix[num][i] == 1 and check[i] == 0:  # 연결이 되어 있다면
                queue.append(i)
                check[i] = 1
                ans[m][i] = 1  # 이 부분이 핵심


for i in range(n):
    bfs(i)

for i in ans:
    print(*i)
