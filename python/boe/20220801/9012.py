n = int(input())

for i in range(n):
    a = input()
    ss = a.count('(')
    sss = a.count(')')
    if  ss == sss:
        
        print('YES')
    else:
        print('NO')