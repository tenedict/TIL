
a, b = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))


k1 = set(A+B)
k2 = set(A+B)
for i in B:
    if i in k1:
        k1.remove(i)
for j in A:
    if j in k2:
        k2.remove(j)

k3 = list(k1) + list(k2)
print(len(k3))