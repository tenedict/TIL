h = int(input())

for i in range(1,h + 1):
    n = int(input())
    t =[n]
    s = 0
    while len(t) != 11:
        s += 1
        g = n*s
        g= str(g)
        g = list(g)
        t = t + g
        t = list(set(t))

    

    t.remove(n)    
    print(f'#{i} {s*n}')
    