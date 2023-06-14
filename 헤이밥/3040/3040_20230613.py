from itertools import combinations

nums = []

for i in range(9):
    nums.append(int(input()))

combi = list(combinations(nums,7))

for j in combi:
    if sum(j) == 100:
        print(*list(j),sep="\n")
