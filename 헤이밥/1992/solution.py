def quad_tree(x, y, n):
    if n == 1: # 크기가 1인경우
        print(arr[x][y],end="")
        return

    num = arr[x][y]

    # 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래
    for row in range(x, x+n):
        for col in range(y, y+n):
            if num != arr[row][col]: # 같지 않다면
                print("(",end="")
                n //= 2 # 구역 나누기
                quad_tree(x,y,n)
                quad_tree(x,y+n,n)
                quad_tree(x+n,y,n)
                quad_tree(x+n,y+n,n)
                print(")",end="")
                return
    print(arr[x][y],end="")
    return

n = int(input())
arr = [list(map(int,input())) for _ in range(n)]

quad_tree(0,0,n)