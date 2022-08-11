a, b, c = map(int,input().split())
li = []
for i in range(3):
    x, y = map(int,input().split())
    gg = [x,y-1]
    li.append(gg)

    k = 0
for i in range(3):
    for j in range(2):
        if li[i][j] > k:
            k = li[i][j]


matrix = [[] for _ in range(k+1)]

for i in range(3):
    for h in range(li[i][0],li[i][1]+1):
        matrix[h].append('-')
answer = 0

for hh in matrix:
    if len(hh) == 0:
        continue 
    elif len(hh) == 1:
        answer += a
    elif len(hh) == 2:
        answer += b*2
    elif len(hh) == 3:
        answer += c*3
print(answer)


        

    