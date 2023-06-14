n = int(input())

list = []

for i in range(n):
    list.append(tuple(map(int, input().split())))

# 두번째 원소로 오름차순 정렬하고, 두번째 원소가 같으면 첫번째 원소로 오름차순 정렬하기
list.sort(key=lambda x: (x[1], x[0]))

for i in list:
    print(*i)