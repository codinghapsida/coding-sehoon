test = list(open(0))
for i in test:
    print("NY"[int(i) % 6 == 0])
