from collections import deque

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * n for _ in range(n)]  # 방문했는지 여부(전체적인 그림)


def bfs(x):  # 한 노드에 관해
    check = [0 for _ in range(n)]  # 방문여부 0,1,2
    queue = deque()
    queue.append(x)  # 첫시작

    while queue:
        num = queue.popleft()
        for i in range(n): # 자신의 노드와 연결된 모든 노드를 찾아 queue에 추가
            if check[i] == 0 and graph[num][i] == 1:  # 아직 방문하지 않고, 두개가 인접행렬이라면(둘다 연결되어있는 경우)
                check[i] = 1 # 0 -> 1 | 1 -> 2 | 2 -> 0 무한반복된다. 그래서 check 확인해야함
                queue.append(i)
                visited[x][i] = 1


for i in range(n): # 각 노드마다 확인
    bfs(i)

for i in visited:
    print(*i)
