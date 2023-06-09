# 1차 문제 풀기 : 2023/06/09(금)
# 시간 : 1초 - 2천만
# 데이터 범위 : -천만 ~ 천만 이으로 O(n)으로 풀 수 없다.

# 시간복잡도가 nlog(n)이 될 수 있는 알고리즘을 생각해야 한다.
# 숫자 탐색 문제
# 탐색? 이진 탐색 log(n).
# 정렬 무조건 해주고 해야함

n = int(input())
numbers = sorted(list(map(int, input().split())))
m = int(input())
findNums = list(map(int, input().split()))


def bs(arr, start, end, targetNum):
    if start > end:  # 재귀함수 종료조건
        return 0

    mid = (start + end) // 2
    midValue = arr[mid]

    if midValue == targetNum:
        return cnt.get(targetNum)
    elif midValue > targetNum:
        return bs(arr, start, mid-1, targetNum)
    else:
        return bs(arr, mid+1,  end, targetNum)


cnt = {}

for i in numbers:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in findNums:
    print(bs(numbers, 0, len(numbers) - 1, i), end=' ')
