for _ in range(int(input())):
    n,m = map(int,input().split())
    k = 1
    h = 1
    for i in range(n):
        k *= m
        m -= 1
    for j in range(n):
        h*=n
        n -=1
    print(int(k/h))
