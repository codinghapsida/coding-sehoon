import sys
input = sys.stdin.readline

for i in range(1, int(input())+1):
    # 단어 추가
    words = [input().rstrip() for _ in range(int(input()))]

    print(f"Scenario #{i}:")
    # 유저별 password index
    for _ in range(int(input())):
        index_for_password = list(map(int, input().split()))

        # 각 유저의 비밀번호 정보를 이용해 password 완성
        index = index_for_password[1:]
        password = ''.join([words[x] for x in index])
        print(password)

    print()
