a = map(int,input().split())
a1 = 0
for i in a:
    a1 += i

b = map(int,input().split())
b1 = 0
for i in b:
    b1 += i

c = map(int,input().split())
c1 = 0
for i in c:
    c1 += i

d = map(int,input().split())
d1 = 0
for i in d:
    d1 += i

e = map(int,input().split())
e1 = 0
for i in e:
   e1 += i

k = 0
l = 0
e = 0
for i in (a1,b1,c1,d1,e1):
    if l < i:
        l = i
        k +=1
        k += e
    else:
        e += 1
        continue
print(k,l)
