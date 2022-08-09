a,b = map(int,input().split())

nn =[list(input()) for _ in range(a)]

ans0 =0
ans1 =0
ans2 =0
ans3 =0
ans4 =0


dx = [0,0,1,1]
dy = [0,1,0,1]

for x in range(a):
    for y in range(b):
        car = 0
        emp = 0
        bul = 0
      
        if nn[x][y] != '#':
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                x1 = nx
                y1 = ny
                    
       
                if 0<=x1<a and 0<= y1 < b:
                    if nn[x1][y1] == '#':
                        bul +=1
                    if nn[x1][y1] == '.':
                        emp += 1
                    if nn[x1][y1] == 'X':
                        car += 1 
            
            if car == 0 and bul == 0 and emp == 4:
                ans0 += 1
            elif car == 1 and bul == 0 and emp == 3:
                ans1 += 1
            elif car == 2 and bul == 0 and emp ==2:
                ans2 += 1
            elif car == 3 and bul == 0 and emp == 1:
                ans3  += 1
            elif car == 4 and bul == 0 and emp == 0:
                ans4 += 1 
            

print(ans0)
print(ans1)
print(ans2)
print(ans3)
print(ans4)
                

                