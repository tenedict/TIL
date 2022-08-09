n = input()
co = True
    
while co:   
    pp = 0 
    len_ = len(n)
    for i in n:
        if i == '7' or i == '4':
            pp += 1
        else:
            n = int(n)
            n -= 1
            n = str(n)
            break
    if pp == len_:
        co = False
        print(n)

    