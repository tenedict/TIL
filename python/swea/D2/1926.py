n = int(input())
for i in range(1,n+1):
    i = str(i)
    c = i.count('3') + i.count('6') + i.count('9')
    if c == 0:
        print(i,end=' ')
    elif c == 1:
        print('-',end=' ')
    elif c == 2:
        print('--',end=' ')
    else:
        print('---',end=' ')