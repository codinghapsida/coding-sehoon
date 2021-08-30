# 10
# 3
# 2 4
# 7 8
# 6 9

# 3 -> 6789
# 1

import sys
from collections import Counter as C
input = sys.stdin.readline

cake = [0] * int(input())
people = int(input())
people_needs = []
expected = []
counted = []

for _ in range(people):
    people_needs.append(list(map(int, input().split())))

for i in people_needs: # 2 4, 1 1
    expected.append(i[1]-i[0]+1) # 처음의 예상했던 케이크 조각 개수
    for x in range(i[0], i[1]+1):
        if not cake[x]: # 0,0,0,0,0,
            cake[x] = people_needs.index(i) + 1 # 0 1 1 1 0 0 2 3 3 2
        else:
            continue
    counted.append(cake.count(people_needs.index(i) + 1))

print(expected.index(max(expected))+1)
print(counted.index(max(counted))+1)
