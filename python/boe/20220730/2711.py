n = int(input())

for j in range(n):
    ind, word = input().split()
    ind = int(ind)
    ind = ind -1
    a = ''
    c = -1
    for i in word:
        c += 1
        if c != ind:
           a += i
        elif c == ind:
            continue
    print(a)       
