rec = [list(map(int,input().split())) for _ in range(4)]


pan = [[0]*100 for _ in range(100)]


count = 0
li = []
for i in rec:
    for k in range(i[0],i[2]):
        for j in range(i[1],i[3]):
            if (k,j) in li:
                continue 
            elif pan[k][j] == 0:
                count += 1
                li.append((k,j))
            else:
                continue
    
print(count)