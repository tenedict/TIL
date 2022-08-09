n = input()
c = True
for _ in range(100):
    n = str(n)
    g = 0
    for i in n:
        len_ = len(str(n))
        print(n)
        if i == '7' or i == '4':
            g += 1
        else:
            n = int(n)
            print(n)
            n -= 1
            g = 0
        if g == len_:
            print(n)
        
            