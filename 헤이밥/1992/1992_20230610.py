n = int(input())
arr = [list(map(int, input())) for _ in range(n)]


def division(x, y, n):
    if n == 1:
        print(arr[x][y], end="")
        return

    value = arr[x][y]

    for row in range(x, x + n):
        for col in range(y, y + n):
            if value != arr[row][col]:  # 분할 시작
                n //= 2
                print("(", end="")
                division(x, y, n)
                division(x, y + n, n)
                division(x + n, y, n)
                division(x + n, y + n, n)
                print(")", end="")
                return

    print(value, end="")


division(0, 0, n)
