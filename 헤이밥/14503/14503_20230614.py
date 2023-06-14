n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

# 맨처음 방분
cnt = 1
visited[r][c] = 1

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 북:0 동:1 남:2 서:3
while True:

    flag = 0  # 청소 안됨..
    for _ in range(4):  # 반시계 방향
        d = (d + 3) % 4
        nr = r + dr[d]  # 상,하
        nc = c + dc[d]  # 좌,우

        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0: # 범위 안에 들기
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                cnt += 1
                flag = 1  # 청소 함
                r, c = nr, nc  # 이동
                break

    # 청소 못함
    # 후진
    if flag == 0:
        if arr[r - dr[d]][c - dc[d]] == 1:
            print(cnt)
            break
        else:
            r, c = r - dr[d], c - dc[d]
