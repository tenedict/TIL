a, b = map(int,input().split())

for i in range(min(a,b),0,-1):
    if a%i == 0 and b%i == 0:
        print(i)
        break


for o in range(1,(a*b)+1):
    if o%a == 0 and o%b == 0:
        print(o)
        break