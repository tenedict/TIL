n = int(input())

l = []
for i in range(n):
    a = int(input())
    l.append(a)

l.sort()


for j in range(n):
    print(l[j])