a = input()
b = input()
c = input()

color = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
d = -1
for i in color:
    d += 1
    if a == i:
        a1 = d
e = -1 
for k in color:
    e += 1
    if b == k:
        b1 = e
f = -1
for j in color:
    f += 1
    if c == j:
        c1 = 10**f
   
print((a1*10+b1)*c1)
