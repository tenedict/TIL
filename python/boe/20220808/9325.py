n = int(input())

for i in range(n):
    don = 0
    car = int(input())
    nn = int(input())
    for _ in range(nn):
        su, money = map(int,input().split())
        don += su*money
    don += car
    print(don)
    