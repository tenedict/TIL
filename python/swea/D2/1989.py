u = input()
u = int(u)



for i in range(1,u+1):
    n = input()
    rn = n[::-1]
    
    if rn == n :
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')