n = int(input())

list = []
for i in range(n):
    list.append(tuple(map(int, input().split())))

list.sort(key=lambda x: (x[1], x[0]))

for i in list:
    print(*i)
