n = int(input())
c = 99
if n < 99:
    answer = n
    print(answer)
elif n == 1000:
    answer = 144
    print(answer)

elif n < 1000 and n > 99:
    for i in range(100,n+1):
        a1 = i // 100
        a2 = (i - a1*100)//10
        a3 = (i - a1*100 -a2*10)
        if a1 - a2 == a2 - a3:
            c += 1
        else:
            continue
    print(c)

