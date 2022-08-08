n = int(input())

c= 0

p = []
pe = list(input().split())
for i in pe:
    if i in p:
        c += 1
    else:
        p.append(i)

print(c)
