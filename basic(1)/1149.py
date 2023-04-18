import sys

n = int(input())

rgb = []

for i in range(n): # 2번째 집부터
    rgb.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(1, n):
    rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + rgb[i][0] # 빨간색 집을 칠한 경우
    rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2]) + rgb[i][1] # 초록색 집을 칠한 경우
    rgb[i][2] = min(rgb[i-1][0], rgb[i-1][1]) + rgb[i][2] # 파란색 집을 칠한 경우

print(min(rgb[n-1][0], rgb[n-1][1], rgb[n-1][2]))


