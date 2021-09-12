import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    best = 0
    answer = 0
    for i in range(int(input())):
        g, price = map(int, input().split())
        price_per_g = price/g
        if best == 0:
            best = price_per_g
            answer = price
        if best > price_per_g:
            best = price_per_g
            answer = price

    print(answer)
