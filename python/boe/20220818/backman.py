# import sys

# sys.stdin = open("input.txt")

for _ in range(1,int(input())+1):
    n = int(input())
    c = 0
    cost = 0
    plus = 0
    li = list(map(int,input().split()))
    a = li[n-1]
    for i in range(n-1,-1,-1):
        if li[i] <= a:
            cost += li[i]
            c+= 1
            print
        elif li[i] > a:
            plus += (a*c - cost)
            cost = 0
            c = 0
            a = li[i]
        else:
            continue
    print(plus)

        