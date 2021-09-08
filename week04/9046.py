for _ in range(int(input())):
    alphabet_index = [0] * 26  # 알파벳 인덱스
    password = input()

    for x in password:
        if x.isalpha():  # 공백 미포함하기 위해 isalpha() 사용
            alphabet_index[ord(x)-ord('a')] += 1

    mods = max(alphabet_index)
    print("?" if alphabet_index.count(mods) > 1 else chr(
        alphabet_index.index(mods)+ord('a')))
