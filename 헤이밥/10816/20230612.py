def binarySearch(start, end, findNumber):

    if start > end: # 재귀 함수 종료 조건
        return 0

    middle = (start + end) // 2

    if numbers[middle] == findNumber:  # 종료 조건문
        return dic[numbers[middle]]

    elif numbers[middle] < findNumber:  # 재귀 함수로 계속
        return binarySearch(middle + 1, end, findNumber)

    elif numbers[middle] > findNumber:
        return binarySearch(start, middle - 1, findNumber)


n = int(input())
numbers = sorted(list(map(int, input().split())))  # 정렬은 꼭 해주어야함
m = int(input())
findNumbers = list(map(int, input().split()))

dic = {}

for i in numbers:
    if i not in dic.keys():
        dic[i] = 1
    else:
        dic[i] += 1

for i in findNumbers: # 마지막 index 생각
    print(binarySearch(0, len(numbers) - 1, i), end=" ")
