n = int(input())
bomb = [list(input()) for _ in range(n)]

user = [list(input()) for _ in range(n)]


gg =[]
count = 0
for i in range(n):
    li = []
    if gg == bomb:
        break
    for j in range(n):
        if user[i][j] == 'x':
            if bomb[i][j] == '*':
                
                gg = bomb
                
                break
            elif bomb[i][j] == '.':
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
        elif user[i][j] == '.':
            count = '.'
        li.append(count)
        count = 0
    if gg != bomb:
        gg.append(li)
    else:
        continue

for k in gg:
    a = ''
    for h in k:
        a += str(h)
    print(a)
    

        
        
        
        