n = int(input())
for _ in range(n):
    a,b = input().split()
    g = b
    for i in a:
        if i in g:
            g = g.replace(i,'-',1)
           
            c = True
        else:
            c = False
            break
    if c == True and len(a)== len(b):
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')