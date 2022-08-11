a , b = map(int,input().split())

if a%4 == 0:
    x = a//4
else:
    x = a//4 + 1

if b%4 == 0:
    x1 = b//4
else:
    x1 = b//4 + 1

if a%4 == 0:
    y = 4
else:
    y = a%4

if b%4 == 0:
    y1 = 4
else:
    y1 = b%4

x2 = x - x1
y2 = y - y1
if x2 < 0:
    x2 = -x2
if y2 < 0:
    y2 = -y2

print(x2 + y2)
