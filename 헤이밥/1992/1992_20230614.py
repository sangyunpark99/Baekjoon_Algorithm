def quad(x, y, n):
    if n == 1: # 하나만 존재하는 경우
        print(matrix[x][y], end="")
        return

    num = matrix[x][y] # 기준이 되는 수

    for row in range(x, x + n):
        for column in range(y, y + n):
            if matrix[row][column] != num:
                n //= 2  # 반토막
                print('(', end="")
                quad(x, y, n) # 왼쪽 위
                quad(x, y + n, n) # 오른쪽 위
                quad(x + n, y, n) # 왼쪽 아래
                quad(x + n, y + n, n) # 오른쪽 아래
                print(')', end="")
                return  # 진행 방지

    # 전부다 같은 경우
    print(matrix[x][y], end="")


n = int(input())
matrix = []

for i in range(n):
    matrix.append(list(input()))

quad(0, 0, n)
