# . 46
# o 111
# < 60
# > 62
# v 118
# ^ 94

import sys
input = sys.stdin.readline

n = int(input())
while n>0:
  count =0 
  input()
  y, x= map(int, input().split())
  box = eval("input()," * y)

  for i in range(y):
    for j in range(x):
      if box[i][j] == "o" and ( 
                ( 
                    i > 0 
                    and i + 1 < y
                    and box[i - 1][j] == "v"
                    and box[i + 1][j] == "^"
                )
                or ( 
                    j > 0 
                    and j + 1 < x
                    and box[i][j - 1] == ">"
                    and box[i][j + 1] == "<"
                )
            ): count += 1
  
  print(count)
  n -= 1