arr = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11]

# 핵심로직
# 중간 인덱스 값 찾기
# 무조건 정렬하고 찾아야함


def binarySearch(arr, targetNum):

    start = 0
    end = len(arr) - 1 # 인덱스는 0부터 시

    while start <= end: # start와 end가 같을때까지?
        midIndex = len(arr) // 2  # // 연산자로 소수점이 나올 확률 제거
        midValue = arr[midIndex]

        if midValue == targetNum:
            return midIndex
        elif midValue < targetNum:
            start = midIndex + 1
        else:
            end = midIndex - 1

    return -1  # 찾지 못하느 경우


print(binarySearch(arr, 7))
