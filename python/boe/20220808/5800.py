n = int(input())

for _ in range(1,n+1):
    g = list(map(int,input().split()))
    gesu = g[0]
    g.remove(g[0])
    g.sort()
 
    maxx = max(g)
    minn = min(g)
    op = 0
    for i in range(gesu-1):
        gap = g[i+1] - g[i]
        if gap > op:
            op = gap
    print(f'Class {_}')
    print(f'Max {maxx}, Min {minn}, Largest gap {op}')