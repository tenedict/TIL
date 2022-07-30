n = input()
z = 0
for i in n:
    z += 1
    if i == '(':
        break

c = 0
for i in n[0:z]:
    if i == '@':
        c += 1
    else:
        continue

d = 0
for i in n[z:]:
    if i == '@':
        d += 1
    else:
        continue
print(c,d)
    