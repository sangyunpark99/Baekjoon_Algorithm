a,b = map(int,input().split())
m = int(input())
nums = input().split()
ans = []

def change(a,b,nums):
    numA = list(nums)
    tenNum = 0
    for i in range(len(numA)):
        tenNum += int(numA.pop())*(a**i)
    while tenNum // b: # 몫이 1일때 까지 나눠
        ans.append(tenNum % b) # 나머지 값 추가해
        tenNum //= b
    ans.append(tenNum) #마지막 몫 추가


change(a, b, nums)
print(*reversed(ans))