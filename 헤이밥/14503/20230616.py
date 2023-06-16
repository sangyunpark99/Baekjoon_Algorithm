n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

# 로봇이 방문 - 맨처음엔 청소되지 않은 곳에 떨어짐
cnt = 1
graph[r][c] = 2
# 북, 동, 남, 서
rd = [-1, 0, 1, 0]
rc = [0, 1, 0, -1]

while True:
    flag = 0  # 주위에 빈칸이 있는가
    for i in range(4):  # 빈칸이 있는지 확인
        d = (d + 3) % 4  # 반시계 방향으로 확인
        nr = r + rd[d]
        nc = c + rc[d]

        # 청소되지 않은 곳을 발견하고 청소한 후 break 해줘야 함
        if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 0:  # 맴 크기를 넘지 않고, 청소가 되어있지 않은 경우
            cnt += 1
            flag = 1  # 청소할 곳이 있고 청소했다!
            graph[nr][nc] = 2
            r = nr
            c = nc
            break # break 조건 잘 확인하기

    if flag == 0:  # 청소할 곳이 없는데?
        if graph[r - rd[d]][c - rc[d]] == 1:  # 후진했는데 벽이야 끝내
            print(cnt)
            break
        else:  # 후진했는데 벽이 아닌걸? 이동해!
            r = r - rd[d]
            c = c - rc[d]
