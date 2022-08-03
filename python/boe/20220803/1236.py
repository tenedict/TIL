a, b = map(int,input().split())

matrix = []
for _ in range(a):
    line = list(input())
    matrix.append(line)



cou = 0

for i in range(a):
    if 'X' not in matrix[i]:
        cou += 1

matrix1 = []

for j in range(b):
    list_ = []
    for k in matrix:
        list_.append(k[j])
    matrix1.append(list_)


count_ = 0
for l in range(b):
    if 'X' not in matrix1[l]:
        count_ += 1

print(max(count_,cou))


      
