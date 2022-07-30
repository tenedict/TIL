a,b = map(int,input().split())
klist = []
c = 0
while len(klist) < 1000:
    c += 1
    for i in range(c): 
        klist.append(c)
sum_ = 0
for j in range(a-1,b):
    sum_ += klist[j]
print(sum_)