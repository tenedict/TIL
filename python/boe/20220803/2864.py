a, b = input().split()
a1, b1 = a, b
a2, b2 = a, b
if '5' in a:
    a1 = a.replace('5','6')
if '5' in b:
    b1 = b.replace('5','6')


if '6' in a:
    a2 = a.replace('6','5')
if '6' in b:
    b2 = b.replace('6','5')

print(int(a2)+int(b2),int(a1)+int(b1))