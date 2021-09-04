n = list(map(int, input()))
half = len(n)//2
print("LUCKY" if sum(n[:half]) == sum(n[half:]) else "READY")
