n, w, h, l = map(int, input().split())
if (w // l) * (h // l) >= n:
    print(n)
else:
    print((w // l) * (h // l))
