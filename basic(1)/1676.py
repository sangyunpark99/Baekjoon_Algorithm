n = int(input())

count = 0

def recursive(n):
    if n < 2:
        return 1
    return n * recursive(n-1)


ans = str(recursive(n))

for i in range(len(ans)-1 , 0, -1):
    num = int(ans[i])

    if num != 0:
        break
    else:
        count += 1

print(count)