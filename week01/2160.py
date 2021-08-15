# N(2≤N≤50)개의 그림이 있다. 각각의 그림은 5×7의 크기이고, 두 가지 색으로 되어 있다. 
# 이때 두 가지의 색을 각각 ‘X’와 ‘.’으로 표현하기로 하자. 
# 이러한 그림들이 주어졌을 때, 가장 비슷한 두 개의 그림을 찾아내는 프로그램을 작성하시오. 
# 두 개의 그림에서 다른 칸의 개수가 가장 적을 때, 두 개의 그림이 가장 비슷하다고 하자.


from itertools import combinations 
import sys
input = sys.stdin.readline

n = int(input())
box = [[input() for _ in range(5)] for _ in range(n)]
answer = []

def check(box1, box2):
  count = 0

  for i in range(5):
    for j in range(7):
      if box1[i][j] == box2[i][j]: count +=1
    
  return count

for i in combinations(box, 2):
  answer.append(check(i[0], i[1]))
  answer.append(box.index(list(i)[0]) + 1)
  answer.append(box.index(list(i)[1]) + 1)

best_case = max(answer)
answer = sorted( answer[ answer.index(best_case)+1 : answer.index(best_case)+3 ] )
print(*answer)