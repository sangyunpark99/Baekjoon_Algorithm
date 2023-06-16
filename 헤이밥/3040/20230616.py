from itertools import combinations

list = [int(input()) for _ in range(9)]

combis = combinations(list,7)

for combi in combis:
    if sum(combi) == 100:
        for i in combi:
            print(i)

