n = int(input())

a2017 = [0,500,300,300,200,200,200,50,50,50,50,30,30,30,30,30,10,10,10,10,10,10]
a2018 = [0,512,256,256,128,128,128,128,64,64,64,64,64,64,64,64,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32]

firsta = 0
firstb = 0
for i in range(n):
    a, b = map(int,input().split())
    if a < 22: 
        firsta = a2017[a]*10000
        if b < 32:
            firstb = a2018[b]*10000
        else:
            firstb = 0
    if a >= 22:
         firsta = 0
         if b < 32:
            firstb = a2018[b]*10000
         else:
            firstb = 0
           
    print(firsta + firstb)
    