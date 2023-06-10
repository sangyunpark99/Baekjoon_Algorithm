def star(n):
    if n==3:
        return ['***','* *','***']
    stars = star(n//3) # 3개씩 이므로 *3
    arr = []
    for s in stars: # 맨 첫줄 부분
        arr.append(s*3)
    for s in stars: # 가운데 공백 부분
        arr.append(s+' '*(n//3) + s)
    for s in stars: # 아랫 부분
        arr.append(s*3)
    return arr

n = int(input())
print(*star(n),sep='\n')