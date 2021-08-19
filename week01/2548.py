# “대표 자연수는 주어진 모든 자연수들에 대하여 그 차이를 계산하여 그 차이들 전체의 합을 최소로 하는 자연수이다.”

# 6
# 4 3 2 2 9 10 => 2 2 3 4 9 10
# 2 2 3 4 
# => 3
import sys
input = sys.stdin.readline

n = int(input())
lst = sorted(list(map(int, input().split())))

if n % 2 == 0: print(lst[n//2 -1])
else: print(lst[n//2])