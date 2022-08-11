a, b = map(int,input().split())
c= 1
h1= 0
h2 = 0
co = True

for i in range(b):
    t,j = input().split()
    j = int(j)
    if not 0<=h1<=a or not 0<=h2<=a:
        co = False
        break
    if t == 'MOVE':
        if c == 1:
            h1 += j
        if c == 3:
            h1 -= j
        if c == 2:
            h2 += j
        if c == 4:
            h2 -= j
    if t == 'TURN':
        if j == 0:
            c += 1
            if c == 5:
                c = 1
        if j == 1:
            c -= 1
            if c == 0:
                c = 4
   
if 0<=h1<=a and 0<=h2<=a and co == True:
    print(h1, h2)
elif not 0<=h1<=a or not 0<=h2<=a and co == True:
    print(-1)
elif co == False:
    print(-1)


        
