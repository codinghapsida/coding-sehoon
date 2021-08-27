# 상근이는 체스판을 만들려고 한다.

# 체스판은 검정칸과 흰칸으로 이루어져 있다.
# 검정색은 'X'로, 흰색은 '.'로 표시한다.

# 상근이의 체스판은 R행 * C열로 이루어져 있어야 한다.
# 또, 각각의 행의 높이는 문자 A개만큼 이며, 각각의 열의 너비는 문자 B개 만큼이다.

# R, C, A, B가 주어졌을 때, 상근이의 체스판을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 두 양의 정수 R과 C가 주어진다. (1 ≤ R, C ≤ 10)

# 둘째 줄에 두 양의 정수 A와 B가 주어진다. (1 ≤ A, B ≤ 10)

# 출력
# 출력은 R * A행 C * B열로 이루어져 있어야 하며, 문제에서 설명한 상근이의 체스판을 출력한다.

# 2 4 -> XX..XX..
# 2 2    XX..XX..
#        ..XX..XX
#        ..XX..XX

import sys
input = sys.stdin.readline

r, c = map(int, input().split())
a, b = map(int, input().split())

for w in range(r):  # 0 1
    for _ in range(a):
        for y in range(c):  # 0 1 2 3
            print('.' * b if (w+y) % 2 else 'X' * b, end="")
        print()
