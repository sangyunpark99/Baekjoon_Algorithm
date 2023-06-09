def bs(l, target, start, end): # 재귀적으로 호출
    if start > end: # 찾지 못한 경우
        return 0

    mid = (start + end) // 2
    if l[mid] == target:
        return cnt.get(target) # key에서 찾은 값 return
    elif l[mid] > target:
        return bs(l, target, start, mid-1)
    else:
        return bs(l, target, mid+1, end)

n = int(input())
numbers = sorted(list(map(int, input().split())))
m = int(input())
findNums = list(map(int, input().split()))
answer = []

cnt = {}

for i in numbers: # 각 갯수가 몇게 있는지
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

print(cnt)

for i in findNums:
    print(bs(numbers, i, 0, len(numbers)-1), end=' ')