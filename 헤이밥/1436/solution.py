s = list(input())


# 1로 만드는 경우
def makeOne(s):
    cnt = 0
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            cnt += 1

    # 홀수번 뒤집는 경우 +1을 해주고 2를 나눠주어야 원하는 값을 받는다.

    return (cnt+1) // 2


print(makeOne(s))
