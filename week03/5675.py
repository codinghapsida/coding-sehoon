test = list(open(0))  # 읽고 리스트로 변환
for i in test:
    print("NY"[int(i) % 6 == 0])
