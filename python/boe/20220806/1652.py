n = int(input())
bed = []
for _ in range(n):
    a = list(input())
    bed.append(a)

cou = 0
coun = 0
ans = 0
ans1 = 0
for i in range(n):
    for j in range(n):
        if bed[i][j] == '.':
            cou += 1
        elif bed[i][j] == 'X':
            cou = 0
        if cou == 2:
            ans += 1
        if  j == n-1:
            cou = 0
    
    for k in range(n):
        if bed[k][i] == '.':
            coun += 1
        elif bed[k][i] == 'X':
            coun = 0
        if  coun ==2:
            ans1 += 1
        if k == n-1:
            coun = 0

print(ans,ans1)


