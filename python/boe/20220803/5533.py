a = int(input())

matrix = []
for _ in range(a):
    line = list(map(int,input().split()))
    matrix.append(line)
matrix1 =[]
for j in range(3):
    list_ = []
    for k in matrix:
        list_.append(k[j])
    matrix1.append(list_)
print(matrix1)

aaa = []
for k in range(3):
    aaaa = []
    for i in matrix1[k]:
        cou =  matrix1[k].count(i)
        aaaa.append(cou)
    aaa.append(aaaa)
        
bbb = []
for g in range(a):
    bbbb = []
    for h in range(3):
        if aaa[h][g] ==1:
            bbbb.append(matrix1[h][g])
        else:
            continue
    bbb.append(bbbb)
for jj in bbb:
    print(sum(jj))
    
   


    
        
