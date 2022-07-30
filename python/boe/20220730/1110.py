a1 = input()

a1sum = 0

for i in a1:
    a1sum += int(i)
a2 = (int(a1)%10)*10 + a1sum%10

c = 1
while int(a1) != a2:
    a2sum = 0
    for i in str(a2):
        a2sum += int(i)
    a2 = (int(a2)%10)*10 + a2sum%10
    c += 1
    
print(c)

