n = int(input())
t = int(input())
s = list(map(int, input().split()))
score = [0 for i in range(n)]
for i in range(t):
    a = list(map(int, input().split()))
    for j in range(n):
        if s[i] == a[j]:
            score[j] += 1
        else:
            score[s[i] - 1] += 1

print(*score, sep="\n")
