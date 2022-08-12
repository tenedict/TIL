# import sys

# sys.stdin = open("_반반.txt")
u = int(input())

for _ in range(1,u+1):
    ans = 0
    n = input()
    if len(n) == 4:
        co = True
    else:
        co = False
    g = 0
    for k in n:
        if k == n[0]:
            g += 1
    if g != 2:
        co = False
    
    li = []
    for i in n:
        if i not in li:
            li.append(i)
        else:
            ans += 1
    if len(li) == 2 and co == True and ans == 2:
        print(f'#{_} Yes')
    else:
        print(f'#{_} No')

