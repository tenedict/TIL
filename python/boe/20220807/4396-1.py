n = int(input())
bomb = [list(input()) for _ in range(n)]

user = [list(input()) for _ in range(n)]


gg =[]
count = 0
tf = 0
for i in range(n):
    li = []
    
    for j in range(n):
        if user[i][j] == 'x':
            if bomb[i][j] == '*':
                tf =1
            
            if i != n-1:
                if bomb[i+1][j] == '*':
                    count += 1
            if j != n-1:
                if bomb[i][j+1] == '*':
                    count += 1
            if i != 0:
                if bomb[i-1][j] == '*':
                    count += 1
            if j != 0:
                if bomb[i][j-1] == '*':
                    count += 1
            if i != n-1 and j != n-1:    
                if bomb[i+1][j+1] == '*':
                    count += 1
            if i != n-1 and j != 0 :
                if bomb[i+1][j-1] == '*':
                    count += 1
            if i != 0 and j != n-1:
                if bomb[i-1][j+1] == '*':
                    count += 1
            if i != 0 and j != 0:
                if bomb[i-1][j-1] == '*':
                    count += 1
        else:
            count = '.'
        li.append(count)
        count = 0
    gg.append(li)
if tf == 1:
    for i in range(n):
        for j in range(n):
            if bomb[i][j] == '*':
                gg[i][j] = '*'

for k in gg:
    a = ''
    for h in k:
        a += str(h)
    print(a)