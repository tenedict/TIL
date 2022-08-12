import sys

sys.stdin = open("_퍼펙트셔플.txt")
l = int(input())
for num in range(1,l+1):
    n = int(input())
    li = input().split()
    if n%2 == 0:
        h = n/2
        g = n/2
    else:
        h = n//2 + 1
        g = n//2 

    top = []
    bot = []
    for i in range(len(li)):
        if i <= h-1:
            top.append(li[i])
        else:
            bot.append(li[i])

    top.reverse()
    bot.reverse()
    answer = []
    while top:
        co = False
        a = top.pop()
        if bot:    
            b = bot.pop()
            co = True
        answer.append(a)
        if co == True:
            answer.append(b)
    
    if num > 1:
        print(f'\n#{num}',end=' ')
    elif num == 1:
        print(f'#{num}',end=' ')
    for t in answer:
        print(t,end = ' ')
    
        




