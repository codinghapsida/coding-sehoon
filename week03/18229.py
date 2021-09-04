import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
lst = []
count = [0] * n
hand = 0

for _ in range(n):
    lst.append(list(map(int, input().split())))

for i in range(m):
    for j in range(n):
        hand = sum(lst[j][:i+1])
        count[j] += 1
        if hand >= k:
            print(j+1, count[j])
            quit()
