list_ = list(range(1,10001))

for i in range(1,10001):
    a = i
    for j in str(i):
        a += int(j)
    
    if a in list_:
        list_.remove(a)
        
for ij in list_:
    print(ij)