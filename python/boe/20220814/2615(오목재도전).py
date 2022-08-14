import sys

sys.stdin = open("11.txt")
n = [input().split() for _ in range(19)]

c = False


for i in range(19):
    for j in range(19):
      if i == 0:
        if n[i][j] =='1' and  n[i+1][j] =='1' and n[i+2][j] =='1' and n[i+3][j] =='1' and n[i+4][j] == '1' and n[i+5][j] != '1':
                c =True
                print(1)
                print(i+1,j+1)
      elif n[i-1][j] != '1':
        if i < 14:
            if n[i][j] =='1' and  n[i+1][j] =='1' and n[i+2][j] =='1' and n[i+3][j] =='1' and n[i+4][j] == '1' and n[i+5][j] != '1':
                c =True
                print(1)
                print(i+1,j+1)
        if i == 14:
            if n[i][j] =='1' and  n[i+1][j] =='1' and n[i+2][j] =='1' and n[i+3][j] =='1' and n[i+4][j] == '1':
                c =True
                print(1)
                print(i+1,j+1)
      
      
      if j == 0:
        if n[i][j] =='1' and  n[i][j+1] =='1' and n[i][j+2] =='1' and n[i][j+3] =='1' and n[i][j+4] == '1' and n[i][j+5] != '1':
                c =True
                print(1)
                print(i+1,j+1)
      elif n[i][j-1] != '1':
        if j < 14:
            if n[i][j] =='1' and  n[i][j+1] =='1' and n[i][j+2] =='1' and n[i][j+3] =='1' and n[i][j+4] == '1' and n[i][j+5] != '1':
                c =True
                print(1)
                print(i+1,j+1)
        if j == 14:
            if n[i][j] =='1' and  n[i][j+1] =='1' and n[i][j+2] =='1' and n[i][j+3] =='1' and n[i][j+4] == '1':
                c =True
                print(1)
                print(i+1,j+1)
      
      if j == 0:
        if i < 14:
            if n[i][j] =='1' and  n[i+1][j+1] =='1' and n[i+2][j+2] =='1' and n[i+3][j+3] =='1' and n[i+4][j+4] == '1' and n[i+5][j+5] != '1':
                    c =True
                    print(1)
                    print(i+1,j+1)
      if i < 14:
        if j == 0:
            if n[i][j] =='1' and  n[i+1][j+1] =='1' and n[i+2][j+2] =='1' and n[i+3][j+3] =='1' and n[i+4][j+4] == '1' and n[i+5][j+5] != '1':
                    c =True
                    print(1)
                    print(i+1,j+1)
      
      elif n[i-1][j-1] != '1':
        if i < 14 and j < 14:
            if n[i][j] =='1' and  n[i+1][j+1] =='1' and n[i+2][j+2] =='1' and n[i+3][j+3] =='1' and n[i+4][j+4] == '1' and n[i+5][j+5] != '1':
                c =True
                print(1)
                print(i+1,j+1)
        if i == 14 and j == 14:
            if n[i][j] =='1' and  n[i+1][j+1] =='1' and n[i+2][j+2] =='1' and n[i+3][j+3] =='1' and n[i+4][j+4]:
                c =True
                print(1)
                print(i+1,j+1)

      if i == 18:
        if j < 14:
            if n[i][j] =='1' and  n[i-1][j+1] =='1' and n[i-2][j+2] =='1' and n[i-3][j+3] =='1' and n[i-4][j+4] == '1' and n[i-5][j+5] != '1':
                c =True
                print(1)
                print(i+1,j+1)
      elif j == 0:
        if i > 5:
            if n[i][j] =='1' and  n[i-1][j+1] =='1' and n[i-2][j+2] =='1' and n[i-3][j+3] =='1' and n[i-4][j+4] == '1' and n[i-5][j+5] != '1':
                c =True
                print(1)
                print(i+1,j+1)
      elif n[i+1][j-1] != '1':
        if i > 5 and j < 14:
            if n[i][j] =='1' and  n[i-1][j+1] =='1' and n[i-2][j+2] =='1' and n[i-3][j+3] =='1' and n[i-4][j+4] == '1' and n[i-5][j+5] != '1':
                c =True
                print(1)
                print(i+1,j+1)
      if j == 14:
            if n[i][j] =='1' and  n[i-1][j+1] =='1' and n[i-2][j+2] =='1' and n[i-3][j+3] =='1' and n[i-4][j+4] == '1':
                c =True
                print(1)
                print(i+1,j+1)
      if i == 4:
            if n[i][j] =='1' and  n[i-1][j+1] =='1' and n[i-2][j+2] =='1' and n[i-3][j+3] =='1' and n[i-4][j+4] == '1':
                c =True
                print(1)
                print(i+1,j+1)

for i in range(19):
    for j in range(19):
      if i == 0:
        if n[i][j] =='2' and  n[i+1][j] =='2' and n[i+2][j] =='2' and n[i+3][j] =='2' and n[i+4][j] == '2' and n[i+5][j] != '2':
                c =True
                print(2)
                print(i+1,j+1)
      elif n[i-1][j] != '2':
        if i < 14:
            if n[i][j] =='2' and  n[i+1][j] =='2' and n[i+2][j] =='2' and n[i+3][j] =='2' and n[i+4][j] == '2' and n[i+5][j] != '2':
                c =True
                print(2)
                print(i+1,j+1)
        if i == 14:
            if n[i][j] =='2' and  n[i+1][j] =='2' and n[i+2][j] =='2' and n[i+3][j] =='2' and n[i+4][j] == '2':
                c =True
                print(2)
                print(i+1,j+1)
      
      
      if j == 0:
        if n[i][j] =='2' and  n[i][j+1] =='2' and n[i][j+2] =='2' and n[i][j+3] =='2' and n[i][j+4] == '2' and n[i][j+5] != '2':
                c =True
                print(2)
                print(i+1,j+1)
      elif n[i][j-1] != '2':
        if j < 14:
            if n[i][j] =='2' and  n[i][j+1] =='2' and n[i][j+2] =='2' and n[i][j+3] =='2' and n[i][j+4] == '2' and n[i][j+5] != '2':
                c =True
                print(2)
                print(i+1,j+1)
        if j == 14:
            if n[i][j] =='2' and  n[i][j+1] =='2' and n[i][j+2] =='2' and n[i][j+3] =='2' and n[i][j+4] == '2':
                c =True
                print(2)
                print(i+1,j+1)
      
      if j == 0:
        if i < 14:
            if n[i][j] =='2' and  n[i+1][j+1] =='2' and n[i+2][j+2] =='2' and n[i+3][j+3] =='2' and n[i+4][j+4] == '2' and n[i+5][j+5] != '2':
                    c =True
                    print(2)
                    print(i+1,j+1)
      elif i < 14:
        if j == 0:
            if n[i][j] =='2' and  n[i+1][j+1] =='2' and n[i+2][j+2] =='2' and n[i+3][j+3] =='2' and n[i+4][j+4] == '2' and n[i+5][j+5] != '2':
                    c =True
                    print(2)
                    print(i+1,j+1)
      
      elif n[i-1][j-1] != '2':
        if i < 14 and j < 14:
            if n[i][j] =='2' and  n[i+1][j+1] =='2' and n[i+2][j+2] =='2' and n[i+3][j+3] =='2' and n[i+4][j+4] == '2' and n[i+5][j+5] != '2':
                c =True
                print(2)
                print(i+1,j+1)
        if i == 14 and j == 14:
            if n[i][j] =='2' and  n[i+1][j+1] =='2' and n[i+2][j+2] =='2' and n[i+3][j+3] =='2' and n[i+4][j+4]:
                c =True
                print(2)
                print(i+1,j+1)

      if i == 18:
        if j < 14:
            if n[i][j] =='2' and  n[i-1][j+1] =='2' and n[i-2][j+2] =='2' and n[i-3][j+3] =='2' and n[i-4][j+4] == '2' and n[i-5][j+5] != '2':
                c =True
                print(2)
                print(i+1,j+1)
      elif j == 0:
        if i > 5:
            if n[i][j] =='2' and  n[i-1][j+1] =='2' and n[i-2][j+2] =='2' and n[i-3][j+3] =='2' and n[i-4][j+4] == '2' and n[i-5][j+5] != '2':
                c =True
                print(2)
                print(i+1,j+1)
      elif n[i+1][j-1] != '2':
        if i > 5 and j < 14:
            if n[i][j] =='2' and  n[i-1][j+1] =='2' and n[i-2][j+2] =='2' and n[i-3][j+3] =='2' and n[i-4][j+4] == '2' and n[i-5][j+5] != '2':
                c =True
                print(2)
                print(i+1,j+1)
      if i == 4:
            if n[i][j] =='2' and  n[i-1][j+1] =='2' and n[i-2][j+2] =='2' and n[i-3][j+3] =='2' and n[i-4][j+4] == '2':
                c =True
                print(2)
                print(i+1,j+1)
      if j == 14:
            if n[i][j] =='2' and  n[i-1][j+1] =='2' and n[i-2][j+2] =='2' and n[i-3][j+3] =='2' and n[i-4][j+4] == '2':
                c =True
                print(2)
                print(i+1,j+1)
        
if c == False:
    print(0)
        
                        
                
