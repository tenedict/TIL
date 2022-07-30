x , y = input().split()
x = list(x)
y = list(y)

c = 0
a = 0
b = 0
for i in x:
    a += int(i)*(10**c)
    c += 1 
c = 0
for i in y:
    b += int(i)*(10**c)
    c +=1 

xy = a + b
xy = str(xy)
xy = list(xy)
c = 0
answer = 0
for i in xy:
    answer += int(i)*(10**c)
    c +=1 

print(answer)