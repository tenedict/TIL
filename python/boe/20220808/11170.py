n = int(input())

for _ in range(n):
    a, b = map(int,input().split())
    su = 0
    for i in range(a,b+1):
        i = str(i)
        su += i.count('0')
    print(su)
